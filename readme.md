manjaro 自动化安装软件和更改配置脚本

sudo gedit /etc/X11/xorg.conf.d/30-touchpad.conf

sudo gedit ~/.xprofile

mv ./default.yaml ~/.config/fcitx/rime/build/

1. xfce4-keyboard-shortcuts.xml xcfe4快捷键
1. settings.xml maven配置文件
1. daemon.json docker配置文件
1. default.yaml 输入法fcitx-rime配置文件
1.

wechat 输入法

```
env locale=zh_CN

export XIM="fcitx"
export XMODIFIERS="@im=fcitx"
export GTK_IM_MODULE="fcitx"
export QT_IM_MODULE="fcitx"
```