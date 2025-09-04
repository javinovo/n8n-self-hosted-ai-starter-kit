FROM python:3.11-slim

# Install antiword and Flask
RUN apt-get update && apt-get install -y antiword && \
    pip install Flask && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the Flask app code
COPY antidoc_service.py .

# The shared folder will be mounted at /data/shared
VOLUME ["/data/shared"]

EXPOSE 5000

CMD [ "python", "antidoc_service.py" ]
