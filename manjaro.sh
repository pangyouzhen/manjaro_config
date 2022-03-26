pacman-mirrors -c China && sudo pacman -Syuu --noconfirm && sudo pacman -S --noconfirm  yay git
cat pkgs.txt | xargs yay -S --noconfirm
mv xfce4-keyboard-shortcuts.xml ~/config/xfce4/xfconf/xfce-perchannel-xml/
mv .pip ~
mv .condarc ~
mv fonts.conf ~/.config/fontconfig/
python3.8 get-pip.py
sudo vboxreload
