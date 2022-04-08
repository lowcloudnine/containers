FROM redhat/ubi8:latest


RUN \
    # Update the System
    # ---- first add the epel repo
    dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm && \
    # ---- then update
    dnf -y update && \
    \
    # Install necessary System packages
    dnf -y install dnf-plugins-core wget curl git sudo procps htop &&\
    \
    # Add C/C++ tools
    dnf -y install glibc-static glibc-langpack-en glibc-devel glibc* && \
    dnf -y install libtool bzip2 ncurses-devel && \
    dnf -y install gcc gcc-c++ gdb make automake autoconf cmake && \
    # Valgrind -- a tool for debugging
    # wget https://sourceware.org/pub/valgrind/valgrind-3.18.1.tar.bz2 &&\
    # tar -xf valgrind-3.18.1.tar.bz2 && \
    # cd valgrind-3.18.1/ && \
    # ./configure && make && make install && \
    # \
    # Add Java 11
    dnf -y install java-11-openjdk java-11-openjdk-devel && \
    \
    # Add Node JS
    curl -sL https://rpm.nodesource.com/setup_17.x | bash - && \
    dnf -y install nodejs && \
    \
    # Add GoLang to the System
    wget https://go.dev/dl/go1.18.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.18.linux-amd64.tar.gz && \
    \
    # Install docker and docker-compose, 'cuz it's containers all the way down
    dnf -y config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
    dnf -y install docker-ce docker-ce-cli containerd.io && \
    curl -s https://api.github.com/repos/docker/compose/releases/latest \
        | grep browser_download_url \
        | grep docker-compose-linux-x86_64 \
        | cut -d '"' -f 4 \
        | wget -qi - && \
    chmod 755 docker-compose-linux-x86_64 && \
    mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose && \
    \
    # Add the OpenVSCode Server
    wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v1.66.0/openvscode-server-v1.66.0-linux-x64.tar.gz && \
    tar -xzf openvscode-server-v1.66.0-linux-x64.tar.gz && \
    mv openvscode-server-v1.66.0-linux-x64 /usr/local/bin/openvscode && \
    ln -s /usr/local/bin/openvscode/bin/openvscode-server /usr/local/bin/openvscode-server && \
    ln -s /usr/local/bin/openvscode/bin/helpers /usr/local/bin/helpers && \
    ln -s /usr/local/bin/openvscode/bin/remote-cli /usr/local/bin/remote-cli && \
    rm -f /opt/openvscode-server-v1.66.0.tar.gz && \
    \
    # Add user "devloper" with password "devloper" and give sudo permissions
    useradd -m devloper && \
    echo "devloper:devloper" | chpasswd  && \
    usermod -aG wheel devloper && \
    # This doesn't seem to work to allow for non-sudo docker :(
    usermod -aG docker devloper

# Switch to the devloper user and then use it to install user specific things
USER devloper
WORKDIR /home/devloper

RUN \
    # Add Extensions for VSCode
    # =========================================================================
    # ---- Python Extensions
    openvscode-server --install-extension ms-python.python && \
    # ---- Container Extensions
    openvscode-server --install-extension ms-azuretools.vscode-docker && \
    # ---- RedHat Extensions
    openvscode-server --install-extension redhat.java && \
    openvscode-server --install-extension redhat.vscode-openshift-connector && \
    openvscode-server --install-extension redhat.vscode-tekton-pipelines && \
    openvscode-server --install-extension redhat.ansible && \
    # ---- Misc Extensions
    openvscode-server --install-extension alefragnani.project-manager && \
    # openvscode-server --install-extension formulahendry.code-runner && \
    # ---- Themes
    openvscode-server --install-extensionrokoroku.vscode-theme-darcula && \
    openvscode-server --install-extension Equinusocio.vsc-community-material-theme && \
    # =========================================================================
    \
    # Add Rust via rustup
    curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain nightly && \
    \
    # Add GoLang to bashrc for user
    echo 'export PATH="${PATH}:/usr/local/go/bin"' >> /home/devloper/.bashrc && \
    \
    # Add Miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
        -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -f -p $HOME/.miniconda && rm -rf ./miniconda.sh && \
    ~/.miniconda/bin/conda init bash && \
    ~/.miniconda/bin/conda create -n dev python=3.10 && \
    ~/.miniconda/envs/dev/bin/pip install --upgrade pip && \
    ~/.miniconda/envs/dev/bin/pip install glances && \
    ~/.miniconda/envs/dev/bin/pip install jupyterlab && \
    ~/.miniconda/envs/dev/bin/pip install awscli && \
    ~/.miniconda/envs/dev/bin/pip install boto3 && \
    echo "conda activate dev" >> /home/devloper/.bashrc
