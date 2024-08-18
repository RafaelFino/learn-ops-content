FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pygments \
    ttyd \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get autoremove

RUN git clone https://github.com/RafaelFino/learn-ops-content 

WORKDIR /learn-ops-content/src

CMD [ "ttyd", "-p", "8080", "-w", "./start.py" ]