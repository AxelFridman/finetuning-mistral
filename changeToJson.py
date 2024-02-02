import pandas as pd
import json
df = pd.read_csv("evaluationWithQueries.csv")
listOfDict = []
for index, row in df.iterrows():
    dict = {}
    dict["input"] = row["humanQuery"]
    dict["output"] = row["query"]
    listOfDict.append(dict)

jsonStr = json.dumps(listOfDict)
with open("evaluationWithQueries.json", "w") as f:
    f.write(jsonStr)