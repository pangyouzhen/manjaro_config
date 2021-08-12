import subprocess

# 安装软件
# touchegg 多点触控
pacman_pkgs = ["git", "gvim",
               "fcitx5-im", "fcitx5-rime",
               "community/pycharm-community-edition",
               "docker",
               "yay",
               "conky", "touchegg", ]
install_cmd = "pacman -S %s"
for i in pacman_pkgs:
    install = install_cmd % i
    ins = subprocess.run(install.split())
    if ins != 0:
        print("安装软件失败 %s" % i)

yay_pkgs = ["you-get", "vlc"]
yay_install_cmd = "yay -S %s"
for i in yay_pkgs:
    install = yay_install_cmd % i
    ins = subprocess.run(install.split())
    if ins != 0:
        print("安装软件失败 %s" % i)

#  下载配置文件
git_clone = "git clone git@github.com:pangyouzhen/manjaro_config.git"
clone_config = subprocess.run(git_clone.split())
if clone_config != 0:
    print("下载配置文件失败")

#  更新配置文件
# /home/pang/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
# 修改配置文件，防止和idea等软件冲突


# sudo cp ./daemon.json /etc/docker/
