import pandas as pd
df= pd.read_csv('testtest.csv')

from sklearn.model_selection import train_test_split

train, test = train_test_split(df, test_size=0.2)

train.to_csv('train_ita.csv', index = False)
test.to_csv('test_ita.csv', index = False)

