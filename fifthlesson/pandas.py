import pandas as pd

# ages = pd.Series([17,18,19,20])
# print(ages)
# print(type(ages))

data = {
    "name": ["Alina", "Ruslan", "Alex"],
    "age": [17,18,19],
    "score": [85,72,96],
    "group": ["A", "B", "A"]
}
df = pd.DataFrame(data)
# print(df)
# print(type(df))
# print(df.head())
# print(df.info())
# print(df.shape)
# print(df.columns)
# print(df["name"])
# print(df["score"])
# print(df(["name", "score"]))
# print(df.iloc[0])
# print(df.iloc[1])
# print(df.iloc[0:2])
# print(df[df["score"] > 80])
# print(df[(df["score"] > 80) & (df["age"] >= 18)])
# print(df.sort_values("score"))
# print(df.sort_values("score", ascending=False))
# df['passed'] = df['score'] >= 75 
# print(df)

# print((df['score']).mean())
# print((df['score']).max())
# print((df['score']).min())
print(df.groupby('group') ["score"].mean())



print(df.head())
print(df.info())
print(df.shape)
print(df.columns)