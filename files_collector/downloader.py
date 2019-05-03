from flask import Blueprint, send_file, abort
from .folder_browser import FolderBrowser
from .auth import auth
from .paths import Paths

bp = Blueprint('downloader', __name__, url_prefix='/<slot_url>/<filename>')

@bp.route('/')
def downloader(slot_url, filename):
    documents_folder = Paths().documents_path
    delimiter = Paths().delimiter
    root = FolderBrowser(documents_folder)
    root.list_folders()
    folder_names = root.folder_names

    if slot_url in folder_names:
        current_dir = FolderBrowser(documents_folder + slot_url + delimiter)
        current_dir.list_files()
        files_list = current_dir.file_names

    if slot_url in folder_names and filename in files_list:
        path = documents_folder + slot_url + delimiter + filename
        if needs_auth():
            return send_file_with_auth(path)
        else:
            return send_file(path, as_attachment = True)
    else:
        return abort(404)

@auth.login_required
def send_file_with_auth(path):
    return send_file(path, as_attachment = True)

def needs_auth():
    config = Paths().config_path
    try:
        open(config, 'r')
        return True
    except FileNotFoundError:
        return False
