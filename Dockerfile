FROM python:alpine

WORKDIR /home/

ENV BRANCH master
ENV HOST 0.0.0.0

RUN apk add --update \
    git \
    python3 \
    py3-pip \
 && git clone --branch ${BRANCH} https://github.com/seven48/hubot-mongo-bridge \
 && cd hubot-mongo-bridge \
 && pip3 install -r requirements.txt

RUN apk del git

WORKDIR /home/hubot-mongo-bridge/

CMD [ "python3", "app.py" ]
