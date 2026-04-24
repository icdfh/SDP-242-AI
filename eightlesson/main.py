# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# data = {
#     "experience": [1, 2, 3, 4, 5, 6, 7, 8],
#     "salary": [150000, 180000, 210000, 250000, 280000, 320000, 360000, 400000]
# }

# df = pd.DataFrame(data)

# X = df[["experience"]]
# y = df["salary"]

# model = LinearRegression()
# model.fit(X, y)

# print("Weight:", model.coef_)
# print("Bias:", model.intercept_)

# new_person = [[10]]
# prediction = model.predict(new_person)

# print("Predicted salary:", prediction)

# predicted_salary = model.predict(X)

# plt.scatter(df["experience"], df["salary"], label="Real data")
# plt.plot(df["experience"], predicted_salary, label="Regression line")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.title("Experience vs Salary")
# plt.legend()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df[["passed"]]

model = LogisticRegression()
model.fit(X,y)

new_student = [[4.5]]

predicton = model.predict(new_student)
probability = model.predict_proba(new_student)

print("Prediction", prediction)
print("Probabilty", probability)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "tasks": [2,3,5,4,6,8,9,10],
    "passed": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["hours", "tasks"]]
y = df[["passed"]]

model = LogisticRegression()
model.fit(X,y)

new_student = [[3.5, 2]]

pre = model.predict(new_student)
probability = model.predict_proba(new_student)

print("Prediction", pre)
print("Probabilty", probability)

import math

students = [
    {"name": "A", "hours": 1, "tasks": 2, "passed": 0},
    {"name": "B", "hours": 2, "tasks": 3, "passed": 0},
    {"name": "C", "hours": 3, "tasks": 4, "passed": 0},
    {"name": "D", "hours": 5, "tasks": 8, "passed": 1},
    {"name": "E", "hours": 6, "tasks": 9, "passed": 1},
    {"name": "F", "hours": 7, "tasks": 10, "passed": 1},
]

new_student = {
    "hours": 1.5,
    "tasks": 1
}

def distance(student, new_student):
    hours_diff = student["hours"] - new_student["hours"]
    task_diff = student["tasks"] - new_student["tasks"]

    result = math.sqrt(hours_diff ** 2 + task_diff ** 2)
    return result

for student in students:
    student["distance"] = distance(student, new_student)

for student in students:
    print(student)

sorted_students = sorted(students, key = lambda student: student["distance"])

for student in sorted_students:
  print(student["name"], student["distance"], student["passed"])

k = 3
nearest_neighbors = sorted_students[:k]
print(nearest_neighbors)

votes = []
for neighbor in nearest_neighbors:
  votes.append(neighbor["passed"])
print(votes)

prediction = max(set(votes), key = votes.count)
print("Predict", prediction)


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = {
    "hours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 3, 6, 5, 7, 8],
    "tasks": [2, 3, 5, 4, 6, 8, 9, 10, 12, 14, 3, 7, 9, 11, 13],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["hours", "tasks"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Real values:", y_test.values)
print("Accuracy:", accuracy)

# Новый студент
new_student = pd.DataFrame({
    "hours": [1],
    "tasks": [2]
})

# Масштабируем нового студента тем же scaler
new_student_scaled = scaler.transform(new_student)

# Предсказываем результат
new_prediction = model.predict(new_student_scaled)

print("New student prediction:", new_prediction[0])

if new_prediction[0] == 1:
    print("Новый студент, скорее всего, сдаст")
else:
    print("Новый студент, скорее всего, не сдаст")


    import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score

data = {
    "age": [18, 22, 25, 30, 35, 40, 45, 50, 21, 28, 33, 38, 44, 52, 60],
    "income": [100000, 150000, 180000, 250000, 300000, 400000, 500000, 600000, 120000, 220000, 270000, 350000, 480000, 620000, 700000],
    "approved": [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["age", "income"]]
y = df["approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression()
knn_model = KNeighborsClassifier(n_neighbors=3)

log_model.fit(X_train_scaled, y_train)
knn_model.fit(X_train_scaled, y_train)

log_pred = log_model.predict(X_test_scaled)
knn_pred = knn_model.predict(X_test_scaled)

print("Logistic accuracy:", accuracy_score(y_test, log_pred))
print("KNN accuracy:", accuracy_score(y_test, knn_pred))

new_client = [[29, 260000]]
new_client_scaled = scaler.transform(new_client)

print("Logistic prediction:", log_model.predict(new_client_scaled))
print("Logistic probability:", log_model.predict_proba(new_client_scaled))

print("KNN prediction:", knn_model.predict(new_client_scaled))
print("KNN probability:", knn_model.predict_proba(new_client_scaled))