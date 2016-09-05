from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
import os
from compare import doit

ALLOWED_EXTENSIONS = set(['jpg', 'png'])
UPLOAD_FOLDER = '/'

names = []
message = False
first= False
second= False

def add(filename):
    if len(names) != 2: 
        names.append(filename)
    if len(names) == 2:
        global message 
        message = doit(names)
        
app = Flask(__name__, static_url_path = "", static_folder = "/home/rabinzon/Desktop/cv/imgs")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global first, second
        first = request.files['first']
        second = request.files['second']
        print first, second
        for file in [first, second]: 
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                add(file.filename)
        return redirect(url_for('index'))
    return render_template('index.html', msg=message, first=first, second=second)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
