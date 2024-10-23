import pandas as pd
df = pd.read_csv('Playground/scraping/stusorted.csv')

unique = []

for i in df['first']:
    if i not in unique:
        unique.append(i)

print(unique)
