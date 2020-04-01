# youtubedl-webui
## A very simple Dockerimage for an yotube-dl webui
**PLEASE DONT RUN THIS EXPOSED TO INTERNET! IS USES OS.SYSTEM AND IS NOT 100% SECURE**

### Start via docker-hub
```bash
docker run -d --rm -p 5000:5000/tcp ucode1337/youtubedl-webui
```

### Build by Dockerfile
```bash
git clone https://git.ucode.space/Phil/youtubedl-webui.git
cd youtubedl-webui
docker build . -t ytdlwebui
docker run -d --rm -p 5000:5000/tcp ytdlwebui
```