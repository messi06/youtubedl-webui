FROM alpine:3.7

LABEL maintainer "Phil/ucode1337 <phil@ucode.space>"

RUN mkdir /yt
COPY . /yt/.

RUN apk --no-cache add python3 ffmpeg && \
    pip3 install --no-cache-dir youtube-dl flask
