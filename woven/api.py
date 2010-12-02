#!/usr/bin/env python
"""
The full public woven api
"""
from woven.deployment import deploy_files, mkdirs
from woven.deployment import upload_template, run_once_per_host_version

from woven.environment import check_settings, deployment_root, set_env, patch_project, get_project_version, server_state, set_server_state

from woven.project import deploy_static, deploy_media, deploy_project, deploy_db, deploy_templates

from woven.linux import add_user, install_package, port_is_open, skip_disable_root
from woven.linux import install_packages, post_install_package, post_setupnode
from woven.linux import upgrade_packages, setup_ufw, disable_root
from woven.linux import add_repositories, restrict_ssh, upload_ssh_key
from woven.linux import change_ssh_port, set_timezone, lsb_release, upload_etc

from woven.virtualenv import activate, active_version
from woven.virtualenv import mkvirtualenv, rmvirtualenv, pip_install_requirements
from woven.virtualenv import post_deploy

from woven.webservers import deploy_wsgi, deploy_webconf, start_webservers, stop_webservers, reload_webservers
from woven.webservers import has_webservers

def deploy(overwrite=False):
    """
    deploy a versioned project on the host
    """
    check_settings()
    if overwrite:
        rmvirtualenv()
    deploy_funcs = [deploy_project,deploy_templates, deploy_static, deploy_media,  deploy_webconf, deploy_wsgi]
    if not patch_project() or overwrite:
        deploy_funcs = [deploy_db,mkvirtualenv,pip_install_requirements] + deploy_funcs
    for func in deploy_funcs: func()


def setupnode(overwrite=False):
    """
    Install a baseline host. Can be run multiple times

    """
    if not port_is_open():
        if not skip_disable_root():
            disable_root()
        port_changed = change_ssh_port()
      
    upload_ssh_key()
    restrict_ssh()
    add_repositories()
    upgrade_packages()
    setup_ufw()
    install_packages()
    upload_etc()
    post_install_package()
    
    set_timezone()
    #stop and start apache - and reload nginx
    if has_webservers():
        stop_webservers()
        start_webservers()

