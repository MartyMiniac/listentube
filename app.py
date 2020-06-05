from flask import *
import youtube_dl
import pafy

app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        try:
            input_url = request.form['url']
            ydl_opts = {
                'format': 'bestaudio',
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(input_url, download=False)
                f=open('url.txt','w')
                ouf=open('ourl.txt','w')
                url=info['formats'][0]['url']
                f.write(url)
                f.close()
                ouf.write(input_url)
                ouf.close()
        except:
            return redirect('/')
        return redirect('/listen')
    else:
        return render_template('index.html')

@app.route('/listen', methods=['GET'])
def listen():    
    g=open('url.txt','r')
    ouf=open('ourl.txt','r')
    video = pafy.new(ouf.read())
    name=video.title
    return render_template('listen.html', url=g.read(),title=name)

@app.route('/<string:id>', methods=['GET'])
def receive(id):
    input_url='https://www.youtube.com/watch?v='+id
    try:
        ydl_opts = {
            'format': 'bestaudio',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(input_url, download=False)
            f=open('url.txt','w')
            url=info['formats'][0]['url']
            f.write(url)
            f.close()
            ouf=open('ourl.txt','w')
            ouf.write(input_url)
            ouf.close()
    except:
        return redirect('/')
    return redirect('/listen')

if __name__ == '__main__':
    app.run()