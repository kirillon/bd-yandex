
import os
from flask import Flask, render_template,request,redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'galerea/static/img/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
paints = []

@app.route('/galery', methods=["GET"])
def index():
    paths = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename[filename.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                paths.append("/static/img/"+filename)
    
    return render_template('image_mars.html',paths=paths)
    
@app.route('/galery', methods=['POST'])
def my_form_post():
    file = request.files['file']
    filename = file.filename
    print(filename)
    if 'file' not in request.files:
            
            return redirect(request.url)
    file = request.files['file']
    
    if file.filename == '':
        
        return redirect('/galery')
    if file:
        
        
        
        filename = secure_filename(file.filename)
        file.save(app.config['UPLOAD_FOLDER'] + filename)
             
    
    return redirect('/galery')
    
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')