echo 'Server=https://mirrors.tuna.tsinghua.edu.cn/manjaro/stable/$repo/$arch' > /etc/pacman.d/mirrorlist
yes y | sudo pacman -Syuu
yes y | sudo pacman -S python
yes y | sudo pacman -S yay
yes y | sudo pacman -S git
yes y | sudo pacman -S docker
yes y | sudo pacman -S
yay -Ss pycharm+ | grep profession | xargs yay -S