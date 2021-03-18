import re
from subprocess import run

#  对pycharm 增加输入法的脚本
cat_cmd = "cat /usr/share/pycharm/bin/pycharm.sh"
cat_out = run([cat_cmd], shell=True, capture_output=True)
output = run(['grep -n  Run'], input=cat_out.stdout, capture_output=True, shell=True)
o = output.stdout.decode("utf-8")
g = re.match("\d+", o).group()
sed_cmd = "sed -i '%siexport GTK_IM_MODULE=fcitx' /usr/share/pycharm/bin/pycharm.sh" % (int(g) - 2)
sed_cmd2 = "sed -i '%siexport QT_IM_MODULE=fcitx' /usr/share/pycharm/bin/pycharm.sh" % (int(g) - 2)
sed_cmd3 = "sed -i '%siexport XMODIFIERS=@im=fcitx' /usr/share/pycharm/bin/pycharm.sh" % (int(g) - 2)
a = run([sed_cmd], shell=True, capture_output=True)
ab = run([sed_cmd2], shell=True, capture_output=True)
abc = run([sed_cmd3], shell=True, capture_output=True)
