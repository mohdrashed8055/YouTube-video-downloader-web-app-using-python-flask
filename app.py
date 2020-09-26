from flask import Flask, render_template, redirect, url_for, request
import youtube_dl
global link

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
 
    link=request.form.get("link")
    
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['{}'.format(link)])
        return render_template('index.html', status_text='Video Downloaded succesfully! : )')
    except:
        return render_template('index.html', status_text='Download Unsuccessful : (')


if __name__ == '__main__':
	app.run(debug=True)    