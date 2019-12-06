from flask import Flask, render_template, request
from flask import redirect, url_for
from werkzeug.utils import secure_filename
import argv
import sys # print log 찍기용
#print('This is error output', file=sys.stderr)
#import argv
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    #ocr_data = request.args.get('ocr_data')
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_name = secure_filename(f.filename) # 보안 요소 
        f.save(file_name)                       # 파일 이름에 코드 삽입 금지.

        lang = request.form['lang']
        opencv = request.form['opencv']

        return redirect(url_for('get_ocr', file_name=file_name, 
                                lang=lang, opencv=opencv)) 
        #return redirect(url_for('test', code=302, ocr_data='hello')) 

    elif request.method == 'GET':
        return 'not allow'

@app.route('/ocr', methods = ['GET', 'POST'])
def get_ocr():
    file_name = request.args.get('file_name')
    lang = request.args.get('lang')
    opencv = request.args.get('opencv')

    ocr = argv.OcrParser(file_name, lang)

    #print('lang {}'.format(lang), file=sys.stderr)
    #print('ocr_data {}'.format(opencv), file=sys.stderr)
    
    return ocr.img2text()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
