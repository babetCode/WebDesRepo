import pandas as pd
df = pd.read_csv('Playground/scraping/stusorted.csv')

unique = []
frame_list = []

for i in df['first']:
    if i not in unique:
        unique.append(i)

for i in unique:
    frame_list.append({'name': i})

name_frame = pd.DataFrame(frame_list)

name_frame.to_csv('C:/Users/goper/Downloads/stunames.csv')

