from flask import request
from flask_httpauth import HTTPBasicAuth
import hashlib
from .paths import Paths
from .folder_browser import FolderBrowser

auth = HTTPBasicAuth()

def needs_auth(url):
    #config = Paths().config_path
    slot = get_file_slot(url)
    dir = get_current_dir(url)
    config = dir + 'config.conf'
    try:
        with open(config, 'r') as conf:
            # for line in conf:
            #     line = line.split(":")
            #     if line[0] == slot:
            return True
    except FileNotFoundError:
        return False

def get_current_dir(url):
    fd = FolderBrowser(Paths().documents_path)
    fd.set_root_from_url(url)
    return fd.root_folder

def get_file_slot(url):
    i = url.rfind('/')
    j = url[:i-1].rfind('/') + 1
    return url[j:i]

@auth.verify_password
def verify_pw(username, password):
    source = hashlib.sha256()
    source.update(password.encode('utf-8'))
    target = get_target_pw(username)
    return source.hexdigest() == target

def get_target_pw(username):
    filename = request.path[0:len(request.path)]
    i = filename.rfind('/') + 1
    url = filename[:i]

    fd = FolderBrowser(Paths().documents_path)
    fd.set_root_from_url(url)

    #conf = Paths().config_path
    conf = fd.root_folder + 'config.conf'
    url_username = request.path.split("/")[2]
    with open(conf, 'r') as c:
        for line in c:
            line = line.replace(" ", "")
            line = line.replace("\n", "").split(":")
            if line[0] == username:
                return line[1].lower()
