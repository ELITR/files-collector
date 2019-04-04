from flask import Blueprint, render_template, request

bp = Blueprint('daily_schedule', __name__, url_prefix='/daily_schedule')

@bp.route('/', methods=('GET', 'POST'))
def presenters():
    return render_template('daily_schedule/daily_schedule.html')
