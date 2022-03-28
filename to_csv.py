import pandas as pd
import json

with open('en.json', encoding="utf8") as f:
    data = json.load(f)

df = pd.json_normalize(data)
df.to_csv(r'test.csv', index = None)


