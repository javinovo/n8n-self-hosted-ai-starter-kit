# Doc to Text conversion service

Docker image running a Flask service that listens for POST requests at port 5000 with a filename and returning the text representation of the file. It also saves a text version of the file.


## Enable the service in docker compose

Setup [docker-compose.yaml](../docker-compose.yaml) by adding the following to `services`:

```
  doc-to-text:
    build:
      context: ./doc-to-text
    image: doc-to-text:1.0.0
    hostname: doc-to-text
    container_name: doc-to-text
    networks: ['demo']
    volumes:
      - ./shared:/data/shared
    ports:
      - "5000:5000"
    working_dir: /app
```


## How to use from n8n

Add a **HTTP Request** node.
- *Method* = *POST*
- *URL* = `http://doc-to-text:5000/convert`
- *Body Content Type* = *JSON*
- *Specify Body* = *Using Fields Below*
- *Body Parameters* > *Name* = `filename` and proper *Value*
