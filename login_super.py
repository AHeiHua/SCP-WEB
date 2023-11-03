import hashlib
from configparser import ConfigParser

config = ConfigParser()
config.read('Admin.ini')

def it_md5(name):
    md5 = hashlib.md5()
    md5.update(name.encode('utf-8'))
    return md5.hexdigest()

def is_admin(user,password):
    if it_md5(user) == it_md5(config.get(user.upper(),"name")) and it_md5(password) == it_md5(config.get(user.upper(),"password")):
        return True
    else:
        return False
