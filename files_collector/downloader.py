from flask import Blueprint, send_file, abort
from .folder_browser import FolderBrowser
from .auth import auth, needs_auth
from .paths import Paths

bp = Blueprint('downloader', __name__, url_prefix='/<regex("(.*?)"):url>')

@bp.route('<regex("(.*?)[.].+"):filename>/')
def downloader(url, filename):
    i = filename.rfind('/') + 1
    url = url + '/' + filename[:i]
    filename = filename[i:]

    fd = FolderBrowser(Paths().documents_path)
    fd.set_root_from_url(url)
    path = fd.root_folder + filename

    try:
        if needs_auth(url):
            return send_file_with_auth(path)
        else:
            return send_file(path, as_attachment = True)
    except FileNotFoundError:
        return abort(404)

@auth.login_required
def send_file_with_auth(path):
    return send_file(path, as_attachment = True)
