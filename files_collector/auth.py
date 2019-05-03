from flask_httpauth import HTTPBasicAuth
import hashlib
from .paths import Paths

auth = HTTPBasicAuth()

@auth.verify_password
def verify_pw(username, password):
    source = hashlib.sha256()
    source.update(password.encode('utf-8'))
    target = get_target_pw(username)
    return source.hexdigest() == target

def get_target_pw(username):
    conf = Paths().config_path
    with open(conf, 'r') as c:
        for line in c:
            line = line.replace(" ", "")
            line = line.replace("\n", "").split(":")
            if line[0] == username:
                return line[1].lower()
