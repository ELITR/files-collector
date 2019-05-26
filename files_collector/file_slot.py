from flask import Blueprint, render_template, request, abort
from werkzeug.utils import secure_filename
from .folder_browser import FolderBrowser
from .paths import Paths
import os

bp = Blueprint('file_slot', __name__, url_prefix='/')
documents_path = Paths().documents_path
delimiter = Paths().delimiter

@bp.route('<regex("(.*?)"):url>/', methods=('GET', 'POST'))
def file_slot(url):
    fd = FolderBrowser(documents_path)
    fd.set_root_from_url(request.path)
    fd.list_folders()
    folder_names = fd.get_urls_from_paths()
    fd.list_files()
    file_names = fd.file_names

    if request.method == 'POST':
        if 'delete' in request.form:
            delete_files(fd.root_folder)
        else:
            upload_file(fd.root_folder)

    fd.list_files()
    file_names = fd.file_names
    return render_template('file_slot/file_slot.html',
                            menu = folder_names,
                            file_names = file_names
                          )

def get_file_slot(url):
    i = url.rfind('/')
    j = url[:i-1].rfind('/') + 1
    return url[j:i]

def upload_file(slot_url):
    file = request.files['file']
    file_path = slot_url + delimiter + secure_filename(file.filename)
    file.save(file_path)

def delete_files(slot_url):
    files = request.form.getlist('to_delete')
    for file in files:
        file_path = slot_url + delimiter + file
        os.remove(file_path)
