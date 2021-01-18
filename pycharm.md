pycharm 模板 live templates 中设置

```
class $class_name$(nn.Module):
    def __init__(self, $arg1$, $arg2$,$arg3$,$arg4$):
        super($class_name$,self).__init__()
        self.$arg1$ = $arg1$
        self.$arg2$ = $arg2$
        self.$arg3$ = $arg3$
        self.$arg4$ = $arg4$

    def forward(self):
        pass
$END$
```