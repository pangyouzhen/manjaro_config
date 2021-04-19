import re
from subprocess import run

#  对pycharm/ idea 增加输入法的脚本
sh_path = "/usr/share/idea/bin/idea.sh"
# sh_path = "/usr/share/pycharm/bin/pycharm.sh"
cat_cmd = "cat %s" % sh_path
print(cat_cmd)
cat_out = run([cat_cmd], shell=True, capture_output=True)
output = run(['grep -n  Run'], input=cat_out.stdout, capture_output=True, shell=True)
o = output.stdout.decode("utf-8")
g = re.match("\d+", o).group()
print("第%s行" % g)
sed_cmd = "sed -i '%siexport GTK_IM_MODULE=fcitx' %s" % (int(g) - 2, sh_path)
sed_cmd2 = "sed -i '%siexport QT_IM_MODULE=fcitx' %s" % (int(g) - 2, sh_path)
sed_cmd3 = "sed -i '%siexport XMODIFIERS=@im=fcitx' %s" % (int(g) - 2, sh_path)
print(sed_cmd)
print(sed_cmd2)
print(sed_cmd3)
# a = run([sed_cmd], shell=True, capture_output=True)
# ab = run([sed_cmd2], shell=True, capture_output=True)
# abc = run([sed_cmd3], shell=True, capture_output=True)
