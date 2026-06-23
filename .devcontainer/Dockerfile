FROM mcr.microsoft.com/devcontainers/base:ubuntu26.04

# Fix yarn GPG key issue by removing its repository
RUN rm -f /etc/apt/sources.list.d/yarn.list

USER vscode

WORKDIR /tmp/prepare
ADD prepare.sh .
ADD prebuilt prebuilt
RUN chmod +x prepare.sh && ./prepare.sh
