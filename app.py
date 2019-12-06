from flask import Flask, render_template, request
from flask import redirect, url_for
from werkzeug.utils import secure_filename
import sys # print log 찍기용
#import argv
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    ocr_data = request.args.get('ocr_data')
    return render_template('index.html', output=ocr_data)

@app.route('/upload', methods =['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        a = 'changed'
        f = request.files['file']
        file_name = secure_filename(f.filename) # 보안 요소 
        f.save(file_name)                       # 파일 이름에 코드 삽입 금지.
        print(file_name)
        return redirect(url_for('tt')) 
        #return redirect(url_for('test', code=302, ocr_data='hello')) 

    elif request.method == 'GET':
        return 'not allow'

@app.route('/test')
def tt():
    return "test page"

if __name__ == '__main__':
    app.run(debug = True)
