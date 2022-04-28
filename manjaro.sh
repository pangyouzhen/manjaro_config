pacman-mirrors -c China && sudo pacman -Syuu --noconfirm && sudo pacman -S --noconfirm  yay git
cat pkgs.txt | xargs yay -S --noconfirm


# 快捷键设置
mkdir -p ~/.config/xfce4/xfconf/xfce-perchannel-xml/ && cp xfce4-keyboard-shortcuts.xml ~/.config/xfce4/xfconf/xfce-perchannel-xml/
# python源
mv .pip ~
mv .condarc ~
# 字体设置
mkdir -p ~/.config/fontconfig/ &&  mv fonts.conf ~/.config/fontconfig/

# 触摸板设置 不起作用，需要在鼠标和触摸板的gui中设置
# mkdir /etc/X11/xorg.conf.d/ && mv 30-touchpad.conf  /etc/X11/xorg.conf.d/

# docker config
mkdir /etc/docker/ && mv daemon.json /etc/docker/

# python 
python3.8 get-pip.py
pip3.8 install virutalenv

# virtual reload
sudo vboxreload

## .bashrc
cat .bashrc >> ~/.bashrc && source ~/.bashrc

## 
mkdir -pv /data/bak/ && mv  ~/.local/share/keyrings/ /data/bak

sudo mv 01-skip_auth /etc/sudoers.d/