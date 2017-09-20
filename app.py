import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/test/uploads'
ALLOWED_EXTENSIONS = set(['cc','txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def compile(filepath):
    subprocess.call("rm -f ./a.out", shell=True)
    retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True) 
    if retcode:
        print("failed to compile walk.cc") 
        exit
    subprocess.call("rm -f ./output", shell=True) 
    retcode = subprocess.call("./test.sh", shell=True)
    print ("Score: " + str(retcode) + " out of 2 correct.")
    print ("*************Original submission*************" )
    with open('uploads/walk.cc','r') as fs:
      print (fs.read())
    return "Score:" + str(retcode) + " out of 2 correct."

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output = compile(filepath)
           # return redirect(url_for('uploaded_file', filename=filename))
    return render_template('uploaded.html', output=output)


if __name__ == '__main__':
   app.run(host = '0.0.0.0')


