import subprocess

# 创建data文件夹
mkdir_data = "mkdir /data/conda"
mkdir_data_docker = "mkdir /data/docker"
mkdir_data_ = subprocess.call(mkdir_data.split())
mkdir_data_docker_ = subprocess.call(mkdir_data_docker.split())
if mkdir_data_docker_ != 0:
    print("创建文件失败")
print("finish replace source")

# 替换整体源
source = "echo 'Server=https://mirrors.tuna.tsinghua.edu.cn/manjaro/stable/$repo/$arch' > /etc/pacman.d/mirrorlist"
update_source = subprocess.call(source.split())
if update_source != 0:
    print("替换源失败")
print("finish replace source")

#  更新整个系统
pacman_update = "pacman -Syuu"
update = subprocess.call(pacman_update.split())
if update_source != 0:
    print("更新源失败")
print("finish update system")

# 安装软件
pacman_pkgs = ["git", "gvim",
               "fcitx", "fcitx-configtool", "fcitx-rime",
               "community/pycharm-community-edition",
               "docker",
               "yay"]
install_cmd = "pacman -S %s"
for i in pacman_pkgs:
    install = install_cmd % (i)
    ins = subprocess.call(install.split())
    if ins != 0:
        print("安装软件失败 %s" % i)

yay_pkgs = ["you-get", ]
yay_install_cmd = "yay -S %s"
for i in yay_pkgs:
    install = yay_install_cmd % (i)
    ins = subprocess.call(install.split())
    if ins != 0:
        print("安装软件失败 %s" % i)

#  下载配置文件
git_clone = "git clone git@github.com:pangyouzhen/manjaro_config.git"
clone_config = subprocess.call(git_clone.split())
if clone_config != 0:
    print("下载配置文件失败")

#  更新配置文件
# /home/pang/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
# 修改配置文件，防止和idea等软件冲突

# 好像不需要再进行添加了
# export GTK_IM_MODULE=fcitx
# export QT_IM_MODULE=fcitx
# export XMODIFIERS=@im=fcitx


# sudo cp ./daemon.json /etc/docker/