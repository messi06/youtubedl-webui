from flask import Flask, send_file, render_template, request
from os import system

app = Flask(__name__)

iph = "0.0.0.0"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/assets/<path:path>')
def send_js(path):
    return send_file('/yt/templates/assets/'+path)

@app.route('/download', methods=['POST'])
def dwn():
    error = 0
    url = request.form['url']
    ext = request.form['ext']
    qal = request.form['qal']

    if (url[0:16] == "https://www.yout"):
        name = url[32:43]
    elif (url[0:16] == "https://youtube."):
        name = url[28:39]
    elif (url[0:16] == "https://m.youtub"):
        name = url[30:41]
    elif (url[0:16] == "https://youtu.be"):
        name = url[17:28]
    else:
        error = 1

    if (ext == "mp3"):
        system('youtube-dl --extract-audio --add-metadata --audio-format "mp3" --embed-thumbnail -o "/yt/'+name+'.%(ext)s" '+url)
    elif (ext == "mp4"):
        if(qal == "720"):
            system('youtube-dl --add-metadata -f "best[height<=720]" --recode-video mp4 -o "/yt/'+name+'.%(ext)s" '+url)
        elif(qal == "1080"):
            system('youtube-dl --add-metadata -f "best[height<=1080]" --recode-video mp4 -o "/yt/'+name+'.%(ext)s" '+url)
        elif(qal == "9999"):
            system('youtube-dl --add-metadata -f "best" --recode-video mp4 -o "/yt/'+name+'.%(ext)s" '+url)
        else:
            error = 1
    else:
        error = 1

    if(error == 0):
        ret = send_file('/yt/'+name+'.'+ext, as_attachment=True)
    else:
        ret = render_template("error.html")

    return ret

if __name__ == '__main__':
    app.run(host=iph)

# youtube-dl -o 1.%(ext)s
# -f "bestvideo[height<=720]+bestaudio/best[height<=720]" --merge-output-format mp4
# --merge-output-format mp4