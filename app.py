from flask import Flask, render_template, request
from flask import redirect, url_for
from werkzeug.utils import secure_filename
#import argv
app = Flask(__name__)

a = 'a'

@app.route('/', methods = ['GET'])
def index():
    global a
    return render_template('index.html', output=a)

@app.route('/upload', methods =['GET', 'POST'])
def upload_file():
    global a
    if request.method == 'POST':
        a = 'changed'
        f = request.files['file']
        file_name = secure_filename(f.filename) # 보안 요소 
        f.save(file_name)                       # 파일 이름에 코드 삽입 금지.
        print(file_name)
        return redirect(url_for('index')) 

    elif request.method == 'GET':
        return 'not allow'

if __name__ == '__main__':
    app.run(debug = True)
