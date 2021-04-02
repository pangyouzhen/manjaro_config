pycharm 模板 live templates 中设置

```
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import DataLoader

torch.manual_seed(1)

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

```
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn import metrics
```