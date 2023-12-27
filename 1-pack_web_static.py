#!/usr/bin/python3
"""Module that generates a `.tgz` archive from the contents of the `web_static`
directory of the AirBnB clone repo using `Fabric`
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function that generates a `.tgz` archive"""
    date_t = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    filename = f"versions/web_static_{date_t}.tgz"
    local(f"tar -cvzf (filename) web_static")
    if filename:
        return filename
    return None
