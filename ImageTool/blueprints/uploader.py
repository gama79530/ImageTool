from flask import (
    Blueprint, render_template, request, redirect, url_for, current_app, g, send_from_directory, flash
)
import os
import re

bp = Blueprint('uploader', __name__, url_prefix='/')

@bp.route('/')
def upload_page() :
    return render_template('upload_page.html')

@bp.route('/uploader', methods = ["POST"])
def uploader() :
    img_01_file = request.files['img_01']
    # if user does not select file, browser also submit an empty part without filename
    if img_01_file.filename == '' :
        return redirect(url_for(''))

    file_name = str(hash(g)) + img_01_file.filename
    img_01_file.save(os.path.join(current_app.config['INSTANCE_PATH'], file_name))

    # from ..widgts.IRE_Keras import query_online
    # results = query_online.query_online(
    #     os.path.join(current_app.config['IMG_DATABASE_PATH'], 'imgset.file'), 
    #     os.path.join(current_app.config['INSTANCE_PATH'], file_name)
    # )
    import subprocess
    query = os.path.join(current_app.config['INSTANCE_PATH'], file_name)
    index = os.path.join(current_app.config['IMG_DATABASE_PATH'], 'imgset.file')
    result = current_app.config['IMG_DATABASE_PATH']
    cwd = os.path.join(os.getcwd(), 'widgts\\IRE_Keras')
    command = 'python -m query_online -query %s -index %s -result %s' % (query, index, result)

    cp = subprocess.run(command, stdout=subprocess.PIPE, shell=True, cwd=cwd, text=True)
    results = list()
    for result_str in cp.stdout.split(',') :
        results.append(result_str.strip('[]\'\n '))

    os.remove(os.path.join(current_app.config['INSTANCE_PATH'], file_name))
    return render_template('result.html', results = results)

@bp.route('/image/<img_name>', methods = ["GET","POST"])
def img_render(img_name) :
    return send_from_directory(current_app.config['IMG_DATABASE_PATH'], img_name, mimetype='image/jpeg')