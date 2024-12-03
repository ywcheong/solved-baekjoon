FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y gcc gdb make g++ git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /ps-env