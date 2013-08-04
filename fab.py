from fabric.api import *
from fabric.context_managers import cd

env.hosts = ['pyhackers']
env.root = '/var/www/pythonhackers.com/'
env.user = 'root'


def restart_nginx():
    run("/service nginx restart")


def restart_process():
    sudo("supervisorctl restart pythonhackers")


def show_git_log():
    with cd(env.root):
        run("git log -2")


def update_code():
    with cd(env.root):
        run("git pull")


def install(*packages):
    assert packages is not None
    sudo("apt-get -y install %s" % packages)


def deploy():
    update_code()
    restart_process()


def super(mode=""):
    sudo("supervisorctl %s" % mode)


def hostname_check():
    run("hostname")


def disc_status():
    run("df -h")
