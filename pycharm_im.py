import shlex
from typing import Union
from subprocess import run, CompletedProcess
import re

cat_cmd = "cat /tmp/test.txt"
cat_out: Union[CompletedProcess, CompletedProcess[bytes]] = run(shlex.split(cat_cmd),
                                                                capture_output=True)
output = run(['grep', '-n', 'Run'], input=cat_out.stdout, capture_output=True)
o = (output.stdout.decode("utf-8"))
g = re.match("\d+", o).group()
print(g)
#TODO
sed_cmd = "sed -i '%s;export GTK_IM_MODULE=fcitx' /tmp/pycharm.sh" % (int(g) - 2)
print(sed_cmd)
a = run(["sed", " -i ", r'%s;export GTK_IM_MODULE=fcitx' % (int(g) - 2),
         "/tmp/pycharm.sh"], capture_output=True, shell=True)
print(a.stdout)
