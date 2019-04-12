from flask import Blueprint, render_template, request, abort
from .folder_browser import FolderBrowser

bp = Blueprint('file_slot', __name__, url_prefix='/')

@bp.route('/<slot_url>', methods=('GET', 'POST'))
def file_slot(slot_url):
    root = FolderBrowser('D:\\prezentace\\')
    root.list_folders()
    folder_names = root.folder_names

    if slot_url in folder_names:
        return render_file_slot(slot_url, folder_names)
    else:
        return abort(404)

def render_file_slot(slot_url, folder_names):
    current_dir = FolderBrowser('D:\\prezentace\\' + slot_url + '\\')
    current_dir.list_files()
    file_names = current_dir.file_names
    return render_template('file_slot/file_slot.html',
                            menu = folder_names,
                            file_names = file_names
                          )
