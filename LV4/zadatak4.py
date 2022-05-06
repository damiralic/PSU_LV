import pandas as pd

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

# print(df.sort_values(by=['selling_price']).head(3))
# print(df.sort_values(by=['selling_price']).tail(3))

print(sum(df['year']==2012))

print(df.sort_values(by=['km_driven']).head(3))
print(df.sort_values(by=['km_driven']).tail(3))