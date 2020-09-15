轻点单击：
sudo gedit /etc/X11/xorg.conf.d/30-touchpad.conf
输入法配置
sudo gedit ~/.xprofile
合上盖子休眠

sudo vim /etc/systemd/logind.conf
sudo systemctl restart systemd-logind
docker 配置
sudo cp ./daemon.json /etc/docker/

安装软件
sudo pacman -S community/pycharm-community-edition
sudo yay -S you-get 


sudo pacman -S fcitx
sudo pacman -S fcitx-configtool
fcitx
sudo pacman -S fcitx-rime
mv ./default.yaml ~/.config/fcitx/rime/build/

sudo pacman -S gvim
注意： 这里是gvim 才支持 剪切板

xmodmap -e 'keycode  68 = Tab ISO_Left_Tab Tab ISO_Left_Tab'
xmodmap -e 'keycode  67 = w W w W'

sudo cp mirrorlist /etc/pacman.d/
