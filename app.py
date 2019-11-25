from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#import argv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods =['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_name = secure_filename(f.filename) # 보안 요소 
        f.save(file_name)                       # 파일 이름에 코드 삽입 금지.
        print(file_name)
        return '파일 업로드 성공'

    elif request.method == 'GET':
        return 'not allow'

if __name__ == '__main__':
    app.run(debug = True)
