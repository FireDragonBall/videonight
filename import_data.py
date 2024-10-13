#python dict {'number' : 1}
#json        {"number" : "1"}

'''
Get the % of the amount of descriptions that has more than 140 characters

Acceptance Criteria (AC):

1. make json from the file to a dictionary
2. find how to iterate through the 'description' variable of the json (remember to convert to a dict in python!)
3. when iterating, find a way to count each of the descriptions (should be 8807)
4. following that, find a way to count the amount of characters (letters, special characters, space ect.) in each description string
5. use that for iterate through all descriptions and only count the ones that have 140 characters or more (or try 140, 50, 20, ect... if that gives you 0 or 8808)
B. bonus: use the new data to make a graph to display to your future boss for through github :)
'''

import pandas as pd
import json
from matplotlib import pyplot as plt

df = pd.read_csv("netflix_titles.csv")

json_data = df.to_json(orient='records')


with open("netflix_titles.json", "w") as f:
    f.write(json_data)

df = pd.read_json("netflix_titles.json")
# df.to_excel("netflix_titles.xlsx", index=False)

netflix_dict = json.loads(json_data)

final_data = {}
result = []
count = 0
char_count = []
title = []
for a in netflix_dict:
    result.append(a['description'])
    if len(a['description']) >= 140:
        char_count.append(len(a['description']))
        title.append(a['title'])
    count += 1

calculation = {len(a['description'])/len(char_count) * 100}
number_char = len(char_count)
print(number_char)
#print(len(result))
#print(count)
print(f'percentage of descriptions with over 140 characters is {calculation} %\n')

# barplot to show the amount that are more than 140 of characters for a single description. in assending order

df = pd.DataFrame(dict(title=title,description_char_count=char_count), columns=['title','description_char_count'])
df_sorted = df.sort_values('description_char_count')
print(df_sorted)
fig = plt.figure(figsize =(10, 7))
plt.bar('title','description_char_count', data=df_sorted)
plt.show()


