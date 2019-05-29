from flask import Blueprint, render_template
from .paths import Paths
from .folder_browser import FolderBrowser

bp = Blueprint('index', __name__, url_prefix='/')
@bp.route('', methods=['GET'])
def index():
    fd = FolderBrowser(Paths().documents_path)
    paths = fd.get_urls_from_paths()
    names = fd.get_last_url_part()
    menu = zip(paths, names)
    return render_template('/index.html', menu = menu)
