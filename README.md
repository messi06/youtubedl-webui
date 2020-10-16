# youtubedl-webui
![ydaft](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)
<br>
![Maintenance](https://raster.shields.io/badge/Maintained-not--really-red.png) 
<br>
[![Mirroredfromucode](https://img.shields.io/badge/Mirrored-from%20ucodespace--git-blue)](https://git.ucode.space/Phil/youtubedl-webui)
<br>
[![DeployonHeroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2Fmessi06%2Fyoutubedl-webui%2Ftree%2Fheroku)
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
