import numpy as np
import pandas as pd
from time import time

data = pd.read_csv("census.csv")

# Success - Display the first record
#print(data.head(n=1))
print(len(data.loc[data['income'] == '<=50K']))