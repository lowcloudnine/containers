#!/usr/bin/env bash

NAME="vscode"
INTERNAL_PORT="3000"
EXTERNAL_PORT="3000"
IMAGE="my_base"
PROJ_DIR="/mnt/f/Projects"

docker run -d \
    --name="${NAME}" \
    -e TZ=Americas/New_York \
    -p "${EXTERNAL_PORT}":"${INTERNAL_PORT}" \
    -v "${PROJ_DIR}":/projects \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --restart unless-stopped \
    -it "${IMAGE}" \
    openvscode-server --port "${INTERNAL_PORT}" --host 0.0.0.0 --without-connection-token
