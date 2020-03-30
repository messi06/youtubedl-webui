FROM alpine:latest

LABEL maintainer "Phil/ucode1337 <phil@ucode.space>"
Maintainer "Phil/ucode1337 <phil@ucode.space>"

EXPOSE 5000

VOLUME /yt
COPY . /yt/.

RUN apk --no-cache add python3 ffmpeg && \
    pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir youtube-dl flask

CMD ["python3", "/yt/main.py"]