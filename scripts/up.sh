#!/bin/bash -xeu

cd "$(dirname "$(readlink -f "$0")")/.."
sudo docker compose --profile gpu-nvidia up

