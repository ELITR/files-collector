from flask import Blueprint, render_template, request, flash
from werkzeug.utils import secure_filename
from .folder_structure import FolderStructure
from .folder_browser import FolderBrowser
import mimetypes

bp = Blueprint('daily_schedule', __name__, url_prefix='/daily_schedule')

@bp.route('/', methods=('GET', 'POST'))
def upload_daily_schedule():
    menu = []
    if request.method == 'POST':
        file = request.files['file']
        file_path = 'D:\\program_dne\\' + secure_filename(file.filename)
        file.save(file_path)
        flash(create_folders(file_path))
        fd = FolderBrowser('D:\\prezentace\\')
        menu = fd.folder_names

    return render_template('daily_schedule/daily_schedule.html', menu = menu)

def create_folders(daily_schedule):
    message = 'Načtení programu dne se povedlo'

    try:
        fd = FolderStructure(daily_schedule)
        fd.create_folders()
    except:
        message = 'Prosím nastavte kódování souboru na utf a zopakujte'

    mime = mimetypes.guess_type(daily_schedule)
    if mime[0] != 'text/plain':
        message = "Prosím vkládejte pouze textové soubory (ne word, excel apod.)"

    return message
