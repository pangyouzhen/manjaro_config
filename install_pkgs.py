import subprocess

# TODO 暂时还不能用，容器内测试 Syuu 更新404
# 替换整体源
source = "echo Server=https://mirrors.tuna.tsinghua.edu.cn/manjaro/stable > /etc/pacman.d/mirrorlist"
update_source = subprocess.Popen(source.split(), stdout=subprocess.PIPE)
source_output, source_error = update_source.communicate()
print("finish replace source")

#  更新整个系统
pacman_update = "pacman -Syuu"
update = subprocess.Popen(pacman_update.split(), stdout=subprocess.PIPE)
update_output, update_error = update.communicate()
print("finish update system")

# 安装软件
pacman_pkgs = ["git", "gvim", "fcitx", "fcitx-configtool", "fcitx-rime",
               "you-get", "community/pycharm-community-edition",
               "docker", ]
install_cmd = "pacman -S %s"
for i in pacman_pkgs:
    install = install_cmd % (i)
    ins = subprocess.Popen(install.split(), stdout=subprocess.PIPE)
    ins_output, ins_error = ins.communicate()

#  下载配置文件
git_clone = "git clone git@github.com:pangyouzhen/manjaro_config.git"
clone_config = subprocess.Popen(git_clone.split(), stdout=subprocess.PIPE)
output, error = clone_config.communicate()

#  更新配置文件
