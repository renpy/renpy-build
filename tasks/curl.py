from renpybuild.model import task

version = "7.78.0"


@task(platforms="windows,mac,linux")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/curl-{{version}}.tar.gz")


@task(platforms="windows,mac,linux")
def build(c):
    c.var("version", version)
    c.chdir("curl-{{version}}")

    c.run("""
    ./configure
    {{ cross_config }}
    --disable-shared
    --prefix="{{ install }}"

    --disable-ftp
    --disable-file
    --disable-ldap
    --disable-ldaps
    --disable-rtsp
    --disable-dict
    --disable-telnet
    --disable-tftp
    --disable-pop3
    --disable-imap
    --disable-smb
    --disable-smtp
    --disable-gopher
    --disable-mqtt

    --with-openssl
    """)

    c.run("""{{ make }}""")
    c.run("""make install""")
