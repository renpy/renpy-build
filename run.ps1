$ErrorActionPreference = "Stop"
Push-Location $PSScriptRoot
try {
    python3 run.py @args
    exit $LASTEXITCODE
} finally {
    Pop-Location
}
