from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods =['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return '파일 업로드 성공'
    elif request.method == 'GET':
        return 'not allow'

if __name__ == '__main__':
    app.run(debug = True)
