from flask import Blueprint, render_template, request, abort
from werkzeug.utils import secure_filename
from .folder_browser import FolderBrowser
from .paths import Paths
import os

bp = Blueprint('file_slot', __name__, url_prefix='/')
documents_path = Paths().documents_path
delimiter = Paths().delimiter

@bp.route('/data-collector/presentations/<slot_url>/', methods=('GET', 'POST'))
def file_slot(slot_url):
    root = FolderBrowser(documents_path)
    root.list_folders()
    folder_names = root.folder_names

    if request.method == 'POST' and slot_url in folder_names:
        if 'delete' in request.form:
            delete_files(slot_url)
        else:
            upload_file(slot_url)

    if slot_url in folder_names:
        return render_file_slot(slot_url, folder_names)
    else:
        return abort(404)

def upload_file(slot_url):
    file = request.files['file']
    file_path = documents_path + slot_url + delimiter + secure_filename(file.filename)
    file.save(file_path)

def delete_files(slot_url):
    files = request.form.getlist('to_delete')
    for file in files:
        file_path = documents_path + slot_url + delimiter + file
        os.remove(file_path)

def render_file_slot(slot_url, folder_names):
    current_dir = FolderBrowser(documents_path + slot_url + delimiter)
    current_dir.list_files()
    file_names = current_dir.file_names
    return render_template('file_slot/file_slot.html',
                            menu = folder_names,
                            file_names = file_names
                          )
