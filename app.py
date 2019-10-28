from flask import Flask, request, send_from_directory, send_file
import urllib.request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__, static_url_path='')
UPLOAD_FOLDER = ""
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

import FYO
import FormatTransformation

ALLOWED_EXTENSIONS = set(['xlsx', 'csv'])

def allowed_file(filename):
    test = False
    filename = str(filename.rsplit('.', 1)[1]).lower()
    if filename in ALLOWED_EXTENSIONS:
        test = True
    return test

@app.route('/')
def home():
    return send_from_directory('templates', 'index.html')

@app.route('/process', methods = ['POST'])
def process():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        name = FYO.process_file(filename)
        name = FormatTransformation.transform_file(name)
        return send_file(name, as_attachment=True, attachment_filename='FYO-processed.xlsx')
    #Check if Post Request
    #Send to the Python

if __name__ =="__main__":
    app.run(debug=True, port=8080)