轻点单击：
sudo gedit /etc/X11/xorg.conf.d/30-touchpad.conf
输入法配置
sudo gedit ~/.xprofile
合上盖子休眠
sudo vim /etc/systemd/logind.conf
sudo systemctl restart systemd-logind
docker 配置
sudo cp ./daemon.json /etc/docker/
