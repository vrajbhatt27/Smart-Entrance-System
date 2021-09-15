import json

data = {}
with open('data.json') as f:
    data = json.load(f)

lst = list(data.keys())
if "18it113" in lst:
    print("Ok")


