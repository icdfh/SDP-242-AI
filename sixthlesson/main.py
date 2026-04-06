# import numpy as np

# scores = np.array([85,90,78,92,100])

# print(scores)
# print(type(print))
# print(scores.shape)
# print(scores.mean())
# print(scores.max())
# print(scores.min())

# ages = np.array([17,18,np.nan,19,20])
# print(ages)
# print(np.isnan(ages))

# import pandas as pd

# df = pd.DataFrame({
#     "name": ["Alice","Bob","Charlie"],
#     "age": [25,30,35],
#     "score": [85,90,78]
# })
# print(df)
# print(df.head())
# print()
# print(df.info())
# print()
# print(df.describe())


# import numpy as np
# import pandas as pd


# data = {
#     "student_id": [101,102,103,104,105,106,107,108],
#     "name": ["Ali", "Aruzhan", "Mansur", "Dana", "Dana", None, "Nurlan", "Aizhan"],
#     "age":[17,18,np.nan,17,17,19,"18",20],
#     "city":["aktobe", "Astana", "Aktobe",None,None,"Aktobe","Almaty", "astana"],
#     "math_score": [85,90,78,None,None,92,88,"91"],
#     "attendance": [95,99,70,100,100,None,85,93],
#     "passed": ["yes","yes","no","yes","yes","yes","no","yes"]
# }

# df = pd.DataFrame(data)
# print(df)
# print()
# # print(df.head())
# # print()
# # print(df.info())
# # print()
# # print(df.isnull().sum())
# # df_dropna = df.dropna()
# # print(df_dropna)

# df_fixed = df.copy()

# df_fixed["age"] = pd.to_numeric(df_fixed["age"], errors="coerce")
# df_fixed["math_score"] = pd.to_numeric(df_fixed["math_score"], errors = "coerce")
# print(df_fixed)
# print()
# print(df_fixed.info())
# print()

# df_filled = df_fixed.copy()

# df_filled["age"] = df_filled["age"].fillna(df_filled["age"].mean())
# df_filled["math_score"] = df_filled["math_score"].fillna(df_filled["math_score"].mean())
# df_filled["attendance"] = df_filled["attendance"].fillna(df_filled["attendance"].mean())
# df_filled["city"] = df_filled["city"].fillna("Unknown")
# print(df_filled)





# import matplotlib.pyplot as plt

# plt.hist(df_filled["math_score"], bins=5, edgecolor ="black")
# plt.xlabel("Math score")
# plt.ylabel("Count")
# plt.title("Распределение баллов по математике")
# plt.show()


# import matplotlib.pyplot as plt

# city_counts = df_filled["city"].value_counts()

# plt.bar(city_counts.index, city_counts.values)
# plt.xlabel("City")
# plt.ylabel("Count")
# plt.title("Количество студентов по городам")
# plt.show()

# import matplotlib.pyplot as plt

# plt.boxplot(df_filled["attendance"].dropna())
# plt.ylabel("Atteandance")
# plt.title("Boxplot посещаемость")
# plt.show()



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "student_id": [101,102,103,104,105,106,107,108],
    "name": ["Ali", "Aruzhan", "Mansur", "Dana", "Dana", None, "Nurlan", "Aizhan"],
    "age":[17,18,np.nan,17,17,19,"18",20],
    "city":["aktobe", "Astana", "Aktobe",None,None,"Aktobe","Almaty", "astana"],
    "math_score": [85,90,78,None,None,92,88,"91"],
    "attendance": [95,99,70,100,100,None,85,93],
    "passed": ["yes","yes","no","yes","yes","yes","no","yes"]
}

df = pd.DataFrame(data)

# копия датафрейма
df_city = df.copy()

# очистка city
df_city["city"] = df_city["city"].str.strip().str.lower()

# если нужно убрать пустые значения
city_counts = df_city["city"].value_counts()

print(city_counts)

plt.figure(figsize=(8,5))
plt.bar(city_counts.index, city_counts.values)
plt.xlabel("City")
plt.ylabel("Count")
plt.title("Количество студентов по городам")
plt.show()

# df_level = pd.DataFrame({
#     "level": ["low","medium","high","medium","low"]
# })

# level_map = {"low":1, "medium":2, "high":3}

# df_level["level_encoded"] = df_level["level"].map(level_map)

# print(df_level)
