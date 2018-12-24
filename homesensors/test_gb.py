#%%
import pandas as pd

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                    'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                    'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})
df

#%%
grouped = df.groupby('A')
#print(grouped)
print(grouped.first())
print(grouped.last())
print(grouped.sum())
