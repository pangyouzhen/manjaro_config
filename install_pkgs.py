import subprocess

# 替换整体源
source = "echo Server=https://mirrors.tuna.tsinghua.edu.cn/manjaro/stable > /etc/pacman.d/mirrorlist"
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
pacman_pkgs = ["git", "gvim", "fcitx", "fcitx-configtool", "fcitx-rime",
               "you-get", "community/pycharm-community-edition",
               "docker", ]
install_cmd = "pacman -S %s"
for i in pacman_pkgs:
    install = install_cmd % (i)
    ins = subprocess.call(install.split())
    if ins != 0:
        print("安装软件失败 %s" % i)

#  下载配置文件
git_clone = "git clone git@github.com:pangyouzhen/manjaro_config.git"
clone_config = subprocess.call(git_clone.split())
if clone_config != 0:
    print("下载配置文件失败")

#  更新配置文件
