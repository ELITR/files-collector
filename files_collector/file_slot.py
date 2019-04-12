from flask import Blueprint, render_template, request, abort
from .folder_browser import FolderBrowser

bp = Blueprint('file_slot', __name__, url_prefix='/')

@bp.route('/<slot_url>', methods=('GET', 'POST'))
def file_slot(slot_url):
    root = FolderBrowser('D:\\prezentace\\')
    root.list_folders()
    folder_names = root.folder_names

    if slot_url in folder_names:
        return render_template('file_slot/file_slot.html', menu = folder_names)

    return abort(404)
