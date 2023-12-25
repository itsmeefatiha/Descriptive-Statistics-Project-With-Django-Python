import pandas as pd 
df = pd.read_csv('pokemon.csv')
print(df.head(5))
#print(df.info())
for col in df.columns :
 print(f'la colonne {col} est de type:{df[[col]].dtypes}')


#print(df[['Name']].info())
df2 = df.copy()
print(df2.describe())
df2[['Type 1']] = df2[['Type 1']].astype('category')

print(df2[['Type 1']].describe())

"""
import pandas as pd 
df = pd.read_csv('https://www.kaggle.com/code/kanncaa1/data-sciencetutorial-for-beginners/input?select=pokemon.csv')
print(df.head())"""