#!/bin/bash -xeu

sudo docker exec -it ollama bash -c "ollama list | tail -n +2 | awk '{print \$1}' | xargs -t -n 1 ollama pull"
