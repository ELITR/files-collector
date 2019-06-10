from flask import request
from flask_httpauth import HTTPBasicAuth
import hashlib
from .paths import Paths
from .folder_browser import FolderBrowser

auth = HTTPBasicAuth()

@auth.verify_password
def verify_pw(username, password):
    source = hashlib.sha256()
    source.update(password.encode('utf-8'))
    target = get_target_pw(username)
    return source.hexdigest() == target

def get_target_pw(username):
    filename = request.path[0:len(request.path)-1]
    i = filename.rfind('/') + 1
    url = filename[:i]
    fd = FolderBrowser(Paths().documents_path)
    fd.set_root_from_url(url)
    print(fd.root_folder)

    #conf = Paths().config_path
    conf = fd.root_folder + 'config.conf'
    url_username = request.path.split("/")[2]
    with open(conf, 'r') as c:
        for line in c:
            line = line.replace(" ", "")
            line = line.replace("\n", "").split(":")
            if line[0] == username == url_username:
                return line[1].lower()
