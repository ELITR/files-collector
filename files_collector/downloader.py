from flask import Blueprint, send_file, abort
from .folder_browser import FolderBrowser
from .auth import auth

bp = Blueprint('downloader', __name__, url_prefix='/<slot_url>/<filename>')

@bp.route('/')
def downloader(slot_url, filename):
    root = FolderBrowser('D:\\prezentace\\')
    root.list_folders()
    folder_names = root.folder_names

    if slot_url in folder_names:
        current_dir = FolderBrowser('D:\\prezentace\\' + slot_url + '\\')
        current_dir.list_files()
        files_list = current_dir.file_names

    if slot_url in folder_names and filename in files_list:
        path = 'D:\\prezentace\\' + slot_url + '\\' + filename
        return send_file_with_auth(path)
    else:
        return abort(404)

@auth.login_required
def send_file_with_auth(path):
    return send_file(path, as_attachment = True)
