FROM ubuntu:latest

RUN apt update -y \
    && apt install -y git ttyd vim python3 python3-pygments \
    && apt autoremove -y \
    && apt autoclean -y \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/RafaelFino/learn-ops-content 

WORKDIR /learn-ops-content/src

EXPOSE 8080

ENTRYPOINT [ "ttyd-server.sh" ]