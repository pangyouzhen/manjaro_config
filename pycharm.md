pycharm 模板 live templates 中设置

1. pytorch 常用模板 torchclass 

```
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import DataLoader

torch.manual_seed(1)

class $class_name$(nn.Module):
    def __init__(self, num_embeddings, embedding_dim,$arg3$,$arg4$):
        super($class_name$,self).__init__()
        self.embedding = nn.Embedding(num_embeddings=num_embeddings, embedding_dim=embedding_dim)
        self.$arg3$ = $arg3$
        self.$arg4$ = $arg4$

    def forward(self):
        pass
$END$
```


1. 数据分析常用模板 dataimport


```
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn import metrics



np.random.seed(0)
torch.manual_seed(0)


```

1. 数据结构常用模板 sol 

```
from typing import List


class Solution:
    def $func_name$(self,$arg3$):
        pass
        
if __name__ == '__main__':
    $arg3$ = $arg4$
    sol = Solution()
    print(sol.$func_name$($arg3$))
    
```