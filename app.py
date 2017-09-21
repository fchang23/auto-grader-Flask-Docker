import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/test/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def compile():
    subprocess.call("rm -f ./a.out", shell=True)
    retcode = subprocess.call("/usr/bin/g++ /home/ubuntu/test/uploads/walk.cc", shell=True) 
    if retcode:
        print("failed to compile walk.cc") 
        exit
    subprocess.call("rm -f ./output", shell=True) 
    retcode = subprocess.call("/home/ubuntu/test/test.sh", shell=True)
    print "Score: " + str(retcode) + " out of 2 correct."
    print "*************Original submission*************" 
    with open('uploads/walk.cc','r') as fs:
      print fs.read()
    return "Score:" + str(retcode) + " out of 2 correct."

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            output = compile()
    return render_template('uploaded.html', output=output)


if __name__ == '__main__':
   app.run(host='0.0.0.0')



