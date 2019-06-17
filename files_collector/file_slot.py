from flask import Blueprint, render_template, request, abort
from werkzeug.utils import secure_filename
from .folder_browser import FolderBrowser
from .paths import Paths
from .sidebar import Sidebar
from .auth import auth, needs_auth
import os

bp = Blueprint('file_slot', __name__, url_prefix='/')
documents_path = Paths().documents_path
delimiter = Paths().delimiter

@bp.route('<regex("(.*?)/"):url>', methods=('GET', 'POST'))
def file_slot(url):
    fd = FolderBrowser(documents_path)
    fd.set_root_from_url(request.path)

    try:
        fd.list_folders()
    except FileNotFoundError:
        return abort(404)

    paths = fd.get_urls_from_paths()

    if needs_auth(url) and request.method == 'POST' and 'delete' in request.form:
        return render_with_delete(fd)
    elif request.method == 'POST' and 'delete' in request.form:
        delete_files(fd.root_folder)
    elif request.method == 'POST':
        upload_file(fd.root_folder)

    return render(fd)


def upload_file(slot_url):
    file = request.files['file']
    file_path = slot_url + delimiter + secure_filename(file.filename)
    file.save(file_path)

def delete_files(slot_url):
    files = request.form.getlist('to_delete')
    for file in files:
        file_path = slot_url + delimiter + file
        try:
            os.remove(file_path)
        except FileNotFoundError: #file already deleted
            pass

@auth.login_required
def render_with_delete(fd):
    delete_files(fd.root_folder)
    fd.list_files()
    file_names = fd.file_names
    return render_template('file_slot/file_slot.html',
                            menu = Sidebar(fd).menu,
                            file_names = file_names
                          )

def render(fd):
    fd.list_files()
    file_names = fd.file_names
    return render_template('file_slot/file_slot.html',
                            menu = Sidebar(fd).menu,
                            file_names = file_names
                          )
