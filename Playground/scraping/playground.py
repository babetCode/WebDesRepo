import pandas as pd
download_path = 'C:/Users/goper/Downloads/stusorted.csv'
df = pd.read_csv('Playground\scraping\stuscraped.csv')

if df.columns[1] == 'first':
    print('same')

sf = df.sort_values(by=['first', 'last'])

sf.to_csv(download_path)