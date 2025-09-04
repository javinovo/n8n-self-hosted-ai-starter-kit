#!/bin/bash

cd "$(dirname "$(readlink -f "$0")")/.."

sudo docker compose --profile gpu-nvidia down
sudo docker compose --profile gpu-nvidia pull
sudo docker compose create

echo -e "\nWARNING: check that credentials have the URL set and with the proper container\
 names as hostnames instead of 'localhost' (this usually gets reset after updating)" >&2
