from flask import Flask, send_file, render_template, request
from os import system

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
cle
@app.route('/download', methods=['POST'])
def dwn():
    url = request.form['name']
    ext = request.form['ext']
    # if m.youtube.com or youtu.be change it
    name = url[32:43]
    system('youtube-dl -o "'+name+ext+'"')
return send_file('/yt/'+name+ext, as_attachment=True)

if __name__ == '__main__':
    app.run()
#  youtube-dl -o 1.%(ext)s