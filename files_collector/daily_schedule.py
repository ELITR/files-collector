from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from .folder_structure import FolderStructure

bp = Blueprint('daily_schedule', __name__, url_prefix='/daily_schedule')

@bp.route('/', methods=('GET', 'POST'))
def upload_daily_schedule():
    if request.method == 'POST':
        file = request.files['file']
        file_path = 'D:\\program_dne\\' + secure_filename(file.filename)
        file.save(file_path)
        fd = FolderStructure(file_path)
        fd.create_folders()

    return render_template('daily_schedule/daily_schedule.html')
