import pytest, os, shutil
from files_collector import create_app

@pytest.fixture
def app():

    app = create_app({
        'TESTING': True
    })
    clean_root_directory()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def clean_root_directory():
    folder = 'D:\\prezentace\\'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
