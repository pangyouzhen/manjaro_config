pacman-mirrors -c China && sudo pacman -Syuu --noconfirm && sudo pacman -S --noconfirm  yay git
cat pkgs.txt | xargs yay -S --noconfirm
# 快捷键设置
mkdir -p ~/.config/xfce4/xfconf/xfce-perchannel-xml/
mv xfce4-keyboard-shortcuts.xml ~/.config/xfce4/xfconf/xfce-perchannel-xml/
mv .pip ~
mv .condarc ~
# 字体设置
mv fonts.conf ~/.config/fontconfig/
python3.8 get-pip.py
pip3.8 install virutalenv
sudo vboxreload
