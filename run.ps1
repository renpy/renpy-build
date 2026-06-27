$ErrorActionPreference = "Stop"

Push-Location $PSScriptRoot

$ImageName = "renpy-build"
$Branch = (git rev-parse --abbrev-ref HEAD) -replace '/', '-'
$Sha = git rev-parse --short=7 HEAD
$Tag = "${Branch}-${Sha}"

function Show-Usage {
    Write-Host @"
Usage: run.ps1 <mode> [args...]

Modes:
  build   Run container in production mode, tagging the image with the current
          commit hash of renpy-build.
  dev     Run container in dev mode, mounting the renpy-build directory so that
          changes to the source are reflected in the container.

Examples:
  .\run.ps1 build --platform windows build
  .\run.ps1 dev clean
"@
}

function Assert-Image {
    param([string]$ImageTag)
    $null = podman image exists "${ImageName}:${ImageTag}" 2>&1
    if (-not $?) {
        $env:TAG = $ImageTag
        podman compose build $ImageName
        if (-not $?) { exit 1 }
    }
}

function Assert-Renpy {
    $RenpyPath = (Resolve-Path "./renpy" -ErrorAction SilentlyContinue)
    if (-not $RenpyPath -or -not (Test-Path $RenpyPath.Path -PathType Container)) {
        Write-Error "Renpy path not found. Please link or clone Ren'Py repository into renpy-build."
        exit 1
    }
    return $RenpyPath.Path
}

if ($args.Count -lt 1) {
    Show-Usage
    exit 1
}
$Mode, [string[]]$BuildArgs = $args

$envVars = @(
    "-e", "UV_PROJECT_ENVIRONMENT=/cache/venv"
    "-e", "RENPY_VIRTUAL_ENV=/cache/venv"
    "-e", "PYTHONUNBUFFERED=1"
    "-e", "PYTHONHASHSEED=0"
    "-e", "RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/"
)

switch ($Mode) {
    "dev" {
        $RenpyPath = Assert-Renpy

        $Volumes = @(
            "-v", "${RenpyPath}:/build/renpy"
            # Store venv in a volume, so build system doesn't change venv in renpy
            # directory that could be a link to repository with existing venv.
            # uv sync will make sure installed packages are up to date.
            "-v", "renpy-build-venv:/cache/venv"
            # Add tmp dir as a volume, to keep its content for incremental builds.
            "-v", "renpy-build-dev-tmp:/build/tmp"
        )

        Assert-Image -ImageTag "dev"

        # In dev mode, mount each non-ignored directory in renpy-build as a
        # volume shadowing files in the container that could be stale.
        $entries = git ls-tree --name-only HEAD
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to list git tree entries."
            exit 1
        }
        $DevVolumes = @(
            "-v", "${PSScriptRoot}/docker-entrypoint.sh:/build/docker-entrypoint.sh"
        )
        foreach ($entry in $entries) {
            $hostPath = Join-Path $PSScriptRoot $entry
            if (Test-Path $hostPath -PathType Container) {
                $DevVolumes += "-v", "${hostPath}:/build/${entry}"
            }
        }

        podman run --rm -it `
            @DevVolumes `
            @Volumes `
            @envVars `
            "${ImageName}:dev" `
            @BuildArgs
    }

    "build" {
        $RenpyPath = Assert-Renpy

        $Volumes = @(
            "-v", "${RenpyPath}:/build/renpy"
            "-v", "renpy-build-venv:/cache/venv"
        )

        $dirty = git status --porcelain
        if ($dirty) {
            Write-Error "renpy-build working tree is dirty. Commit or stash changes before building."
            exit 1
        }

        Assert-Image -ImageTag $Tag

        podman run --rm `
            @Volumes `
            @envVars `
            "${ImageName}:${Tag}" `
            @BuildArgs
    }

    default {
        Show-Usage
        exit 1
    }
}

Pop-Location
exit $LASTEXITCODE
