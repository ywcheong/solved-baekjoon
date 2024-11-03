FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    gcc \
    gdb \
    lldb \
    make \
    g++ \
    git

CMD ["/usr/sbin/sshd", "-D"]
