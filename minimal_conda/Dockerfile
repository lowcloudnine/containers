FROM bitnami/minideb:latest

RUN \
    # Update and any needed packages
    apt-get update && apt-get upgrade -y && \
    apt-get install -y wget sudo && \
    \
    # Add user "devloper" with password "devloper" and give sudo permissions
    useradd -m devloper && \
    echo "devloper:devloper" | chpasswd  && \
    usermod -aG sudo devloper

# Switch to the devloper user and then use it to install user specific things
USER devloper
WORKDIR /home/devloper

RUN \
    # Add Miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
        -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -f -p $HOME/.miniconda && rm -rf ./miniconda.sh && \
    ~/.miniconda/bin/conda init bash && \
    ~/.miniconda/bin/conda create -n dev python=3.10 && \
    ~/.miniconda/envs/dev/bin/pip install jupyterlab && \
    echo "conda activate dev" >> /home/devloper/.bashrc

EXPOSE 8880

# ENTRYPOINT [ "~/.miniconda/envs/dev/bin/jupyter lab" ]
