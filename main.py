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

            if(qal == "720"):
                system('youtube-dl -f '+url)
            elif(qal == "1080"):
                system('youtube-dl -f -o "/yt/vid" '+url)
            elif(qal == "9999"):
                system('youtube-dl --add-metadata -f "best" --recode-video mp4 -o "/yt/'+name+'.%(ext)s" '+url)

ret = send_file('/yt/'+name+'.'+ext, as_attachment=True)
return ret

if __name__ == '__main__':
    app.run(host=iph)

# youtube-dl -o 1.%(ext)s
# -f "bestvideo[height<=720]+bestaudio/best[height<=720]" --merge-output-format mp4
# --merge-output-format mp4
