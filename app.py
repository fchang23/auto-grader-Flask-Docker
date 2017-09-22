import os
import subprocess
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug import secure_filename, SharedDataMiddleware

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})


def compile():
    subprocess.call("rm -f ./a.out", shell=True)
    retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True) 
    if retcode:
        print("failed to compile walk.cc") 
        exit
    subprocess.call("rm -f ./output", shell=True) 
    retcode = subprocess.call("./test.sh", shell=True)
<<<<<<< HEAD
    print ("Score: " + str(retcode) + " out of 2 correct.")
    print ("*************Original submission*************")
=======
    print "Score: " + str(retcode) + " out of 2 correct."
    print "*************Original submission*************" 
>>>>>>> 1b613b2beaf7878d02580f6ee93a6ae0251ce3c3
    with open('uploads/walk.cc','r') as fs:
      print (fs.read())
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



