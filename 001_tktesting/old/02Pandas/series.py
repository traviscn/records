import numpy as np
import pandas as pd

a = pd.Series(data=[11,22,33,44,55,66],index=["aa","bb","cc","dd","ee","ff"],dtype=int,name="SeriesName",copy=True,fastpath=False)
print(a)
print(a.index)
print(a.values)
print(a.name)
print("="*10)
a.name="Rename_name"
a.index.name="index_name"
a.index=["A","B","C","D","E",'F']
print(a)

