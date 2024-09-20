import numpy as np
import pandas as pd

# BASICS
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data = data, index = labels)
df.info

df_6 = df.head(3)
df_7 = df[["animal","age"]]
df_8 = df.iloc[[3, 4, 8], [0,1]]
df_9 = df[df["visits"] > 3]
df_10 = df[df["age"].isnull()]
df_11 = df.loc[(df["animal"] == "cat") & (df["age"] < 3)]
df_12 = df[df["age"].between(2, 4)]
# df.loc['f', 'age'] = 1.5
df_14 = df["visits"].sum()
df_15 = df.groupby("animal")["age"].mean()
df.loc['k'] = {'animal': 'fish', 'age': 7.5, 'visits': 3, 'priority': 'yes'}
df = df.drop('k')

df_17 = df.groupby(["animal"])['animal'].count()
df_18 = df.sort_values(by=['age','visits'], ascending=[False,True])
df_19 = df.replace(to_replace=['yes', 'no'], value=[True, False], inplace=False)
df_20 = df.replace(to_replace='snake', value='python')
df_21 = df.pivot_table(values='age', index='animal', columns='visits', aggfunc='mean')

# BEYOND THE BASICS
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})

df_22 = df.drop_duplicates(subset='A')

df = pd.DataFrame(np.random.random(size=(5, 3))) # a 5x3 frame of float values
df_23 = df.sub(df.mean(axis=1), axis=0)

# Which column of numbers has the smallest sum? Return that column's label.
df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
df_24 = df.sum().idxmin()
# print(df.sum(), df_24)

# How do you count how many unique rows a DataFrame has 
# (i.e. ignore all rows that are duplicates)?
df = pd.DataFrame(np.random.randint(0, 2, size=(10, 3)))
df_25 = df.nunique(axis=1)

# For each row of the DataFrame, find the column which contains the third NaN value.
nan = np.nan
data = [[0.04,  nan,  nan, 0.25,  nan, 0.43, 0.71, 0.51,  nan,  nan],
        [ nan,  nan,  nan, 0.04, 0.76,  nan,  nan, 0.67, 0.76, 0.16],
        [ nan,  nan, 0.5 ,  nan, 0.31, 0.4 ,  nan,  nan, 0.24, 0.01],
        [0.49,  nan,  nan, 0.62, 0.73, 0.26, 0.85,  nan,  nan,  nan],
        [ nan,  nan, 0.41,  nan, 0.05,  nan, 0.61,  nan, 0.48, 0.68]]
columns = list('abcdefghij')
df = pd.DataFrame(data, columns=columns)
df_26 = (df.isna().cumsum(axis=1) == 3).idxmax(axis=1)

# For each group, find the sum of the three greatest values
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df_27 = df.groupby('grps').apply(lambda x: x.vals.nlargest(3).sum())

# For each group of 10 consecutive integers in 'A' (i.e. (0, 10], (10, 20], ...), 
# calculate the sum of the corresponding values in column 'B'.
df = pd.DataFrame(np.random.RandomState(8765).randint(1, 101, size=(100, 2)), columns = ["A", "B"])
df_28 = df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()


# HARDER PROPLEMS


print(df_28)