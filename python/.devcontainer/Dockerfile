FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# install just (make alternative) with bash autocomplete
RUN wget -qO - 'https://proget.makedeb.org/debian-feeds/prebuilt-mpr.pub' | gpg --dearmor | sudo tee /usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg 1> /dev/null && \
    echo "deb [arch=all,$(dpkg --print-architecture) signed-by=/usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg] https://proget.makedeb.org prebuilt-mpr $(lsb_release -cs)" | sudo tee /etc/apt/sources.list.d/prebuilt-mpr.list && \
    sudo apt update && \
    sudo apt install just && \
    just --completions bash > just.sh && \
    /bin/bash -c "source just.sh"


# install pip, poetry and project dependencies
RUN python -m ensurepip --upgrade
RUN pip install poetry