echo 'Server=https://mirrors.tuna.tsinghua.edu.cn/manjaro/stable/$repo/$arch' > /etc/pacman.d/mirrorlist
yes y | pacman -Syuu
yes y | pacman -S python
yes y | pacman -S yay
python install_pkgs.py