from flask import Blueprint, render_template
from .paths import Paths
from .folder_browser import FolderBrowser

bp = Blueprint('index', __name__, url_prefix='/')
@bp.route('', methods=['GET'])
def index():
    fd = FolderBrowser(Paths().documents_path)
    menu = fd.folder_names
    return render_template('/index.html', menu = menu)
