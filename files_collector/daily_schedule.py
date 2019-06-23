from flask import Blueprint, render_template, request, flash
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException
from .folder_structure import FolderStructure
from .folder_browser import FolderBrowser
from .paths import Paths
from .sidebar import Sidebar
import mimetypes

bp = Blueprint('daily_schedule', __name__, url_prefix='/daily_schedule')

@bp.route('/', methods=('GET', 'POST'))
def upload_daily_schedule():
    if request.method == 'POST':
        try:
            file = request.files['file']
        except HTTPException:
            flash('Please click on "browse" to select a file')
        else:
            file_path = Paths().schedule_backup_path + secure_filename(file.filename)
            file.save(file_path)
            flash(create_folders(file_path))

    fd = FolderBrowser(Paths().documents_path)
    return render_template('daily_schedule/daily_schedule.html', menu = Sidebar(fd).menu)

def create_folders(daily_schedule):
    message = 'Daily schedule has been uploaded successfully'

    try:
        fd = FolderStructure(daily_schedule)
        fd.create_folders()
    except:
        message = 'An error has occured. Please set the encoding to utf-8 and repeat'

    mime = mimetypes.guess_type(daily_schedule)
    if mime[0] is not None and mime[0] != 'text/plain':
        message = "An error has occured. Please upload text files only (no word, pptx...)"

    return message
