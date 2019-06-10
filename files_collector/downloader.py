from flask import Blueprint, send_file, abort
from .folder_browser import FolderBrowser
from .auth import auth
from .paths import Paths

bp = Blueprint('downloader', __name__, url_prefix='/<regex("(.*?)"):url>')

@bp.route('<regex("(.*?)[.].+"):filename>/')
def downloader(url, filename):
    i = filename.rfind('/') + 1
    url = url + '/' + filename[:i]
    filename = filename[i:]

    fd = FolderBrowser(Paths().documents_path)
    fd.set_root_from_url(url)

    file_slot = get_file_slot(url)
    path = fd.root_folder + filename

    try:
        if needs_auth(file_slot, fd.root_folder):
            return send_file_with_auth(path)
        else:
            return send_file(path, as_attachment = True)
    except FileNotFoundError:
        return abort(404)

def get_file_slot(url):
    i = url.rfind('/')
    j = url[:i-1].rfind('/') + 1
    return url[j:i]

@auth.login_required
def send_file_with_auth(path):
    return send_file(path, as_attachment = True)

def needs_auth(slot, dir):
    #config = Paths().config_path
    config = dir + 'config.conf'
    try:
        with open(config, 'r') as conf:
            for line in conf:
                line = line.split(":")
                if line[0] == slot:
                    return True
    except FileNotFoundError:
        return False
