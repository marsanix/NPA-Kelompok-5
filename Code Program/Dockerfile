FROM python:3.11-slim

# Install cryptography library untuk AES-128-GCM
RUN pip install --no-cache-dir cryptography

# Install tools untuk debugging jaringan (opsional, berguna saat demo)
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
