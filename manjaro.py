import subprocess
from pathlib import Path

def pre_install():
    update_manjaro = \
    """pacman-mirrors -c China \
    && sudo pacman -Syuu --noconfirm   \
    && sudo pacman -S --noconfirm  yay git \
    && cd /tmp/ && git clone git@github.com:pangyouzhen/manjaro_config.git 
    """
    subprocess.run(update_manjaro.split())

def install_pkgs():
    pkgs = None
    with open("/tmp/manjaro_config/pkgs.txt") as f:
        pkgs = f.readlines()
    for pkg in pkgs:
        subprocess.run(["yay","-S","--noconfirm",f"{pkg}"])
    pass

def config_xfce4():
    configs = None
    with open("/tmp/manjaro_config/manajro.csv") as f:
        configs = f.readlines()
    for config in configs:
        file,usages,path,cmd = config.split(",")
        if path:
            path = Path(path)
            if not path.exists():
                path.mkdir(parents=True)
            subprocess.run(["mv",f"{file}",f"{path}"])
        if cmd:
            subprocess.run([f"{cmd}",f"{file}"])

def post_install():
    reload_vbox = "sudo vboxreload"
    subprocess.run(reload_vbox.split())


if __name__ == "__main__":
    pre_install()
    install_pkgs()
    config_xfce4()
    post_install()
    