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


df = pd.read_csv("netflix_titles.csv")

json_data = df.to_json(orient='records')


with open("netflix_titles.json", "w") as f:
    f.write(json_data)

df = pd.read_json("netflix_titles.json")
# df.to_excel("netflix_titles.xlsx", index=False)

netflix_dict = json.loads(json_data)

result = []
count = 0
char_count = []
for a in netflix_dict:
    result.append(a['description'])  
    if len(a['description']) >= 140:
        char_count.append(len(a['description']))
    count += 1   
# print(result)
# print(count)
print(f'{len(a['description'])/len(char_count) * 100} %')

    

 