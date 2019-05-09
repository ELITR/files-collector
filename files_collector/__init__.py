import os
from flask import Flask
from .regex_converter import RegexConverter

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    app.url_map.converters['regex'] = RegexConverter

    load_blueprints(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    return app

def load_blueprints(app):
    from . import daily_schedule
    app.register_blueprint(daily_schedule.bp)

    from . import file_slot
    app.register_blueprint(file_slot.bp)

    from . import downloader
    app.register_blueprint(downloader.bp)

    from . import index
    app.register_blueprint(index.bp)
