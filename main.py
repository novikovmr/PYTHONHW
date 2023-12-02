
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
# print(data)

data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[data['whoAmI'] != 'human', 'human'] = '0'

data.drop(columns='whoAmI')

print(data)