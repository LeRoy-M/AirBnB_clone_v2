#!/usr/bin/python3
"""Module (based on the file `2-do_deploy_web_static.py`) that creates and
distributes the archived package to the web servers, using `Fabric`
"""
from AirBnB_clone_v2/1-pack_web_static import do_pack
from fabric.api import env, put, run
from os import path, symlink
env.hosts = ["54.236.43.83", "54.164.92.21"]


def deploy():
    """Function that creates and distributes the archive package"""
    archive_path = do_pack()
    if not path.exists(archive_path):
        return False
    try:
        filename_ext = archive_path.split("/")[-1]
        filename = filename_ext.split(".")[0]
        path_fn = f"/data/web_static/releases/{filename}"
        put(archive_path, "/tmp/{filename_ext}")
        run(f"mkdir -p {path_fn}/")
        run(f"tar -xvzf /tmp/{filename_ext} -C {path_fn}")
        run(f"rm /tmp/{filename_ext}")
        run(f"mv {path_fn}/web_static/* {path_fn}")
        run(f"rm -rf {path_fn}/web_static")
        run(f"rm -rf /data/web_static/current")
        symlink(f"{path_fn}/", "/data/web_static/current")
        return True
    except Exception:
        return False
