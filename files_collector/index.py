from flask import Blueprint, render_template
from .paths import Paths
from .folder_browser import FolderBrowser
from .sidebar import Sidebar

bp = Blueprint('index', __name__, url_prefix='/')
@bp.route('', methods=['GET'])
def index():
    fd = FolderBrowser(Paths().documents_path)
    return render_template('/index.html', menu = Sidebar(fd).menu)
