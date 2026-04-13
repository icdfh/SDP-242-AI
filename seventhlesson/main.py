import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "hours_study": [1,2,3,4,5,6,7,8],
    "score": [42,48,55,61,67,72,79,85]
}

df = pd.DataFrame(data)



print(df)

X = df[["hours_study"]]
y = df[["score"]]

model = LinearRegression()
model.tfi(X,y)

predictions = model.predict(X)

new_data = pd.DataFrame({"hours_study": [9]})
predicted_score = model.predict(new_data)
print("Predicted score for 9 hours", predicted_score[0])

print("Coeff", model.coef_[0])


plt.scatter(X,y, label = "Real data")
plt.plot(X,predictions, label = "Regression line")
plt.xlabel("Hours Study")
plt.ylabel("Score")
plt.title("Linear Regresion")
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "exp_years": [1,2,3,4,5,6,7],
    "salary": [180000, 220000,260000,300000,340000,390000,430000]
}

df = pd.DataFrame(data)

X = df[["exp_years"]]
y = df["salary", "qerty"]

model = LinearRegression()
model.fit(X,y)

predictions = model.predict(X)

print("Coeff", model.coef_[0])

plt.scatter(X,y, label = "Real data")
plt.plot(X,predictions, label = "Regression line")
plt.xlabel("Exp (years)")
plt.ylabel("Salary")
plt.title("Salary prediction")
plt.legend()
plt.show()

new_employee = pd.DataFrame({"exp_years": [8]})
predicted_salary = model.predict(new_employee)

print("Predicted salary for 8 years exp:", predicted_salary[0])


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "exp_years": [1, 2, 3, 4, 5, 6, 7],
    "salary": [180000, 220000, 260000, 300000, 340000, 390000, 430000],
    "bonus": [10000, 15000, 20000, 25000, 30000, 35000, 40000],
    "vacation_days": [20, 21, 22, 23, 24, 25, 26]
}

df = pd.DataFrame(data)

X = df[["exp_years"]]
y = df[["salary", "bonus", "vacation_days"]]

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

# 1 график salary
plt.scatter(df["exp_years"], df["salary"], label="Real salary")
plt.plot(df["exp_years"], predictions[:, 0], label="Predicted salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary prediction")
plt.legend()
plt.show()

# 2 график bonus
plt.scatter(df["exp_years"], df["bonus"], label="Real bonus")
plt.plot(df["exp_years"], predictions[:, 1], label="Predicted bonus")
plt.xlabel("Experience")
plt.ylabel("Bonus")
plt.title("Bonus prediction")
plt.legend()
plt.show()

# 3 график vacation_days
plt.scatter(df["exp_years"], df["vacation_days"], label="Real vacation days")
plt.plot(df["exp_years"], predictions[:, 2], label="Predicted vacation days")
plt.xlabel("Experience")
plt.ylabel("Vacation days")
plt.title("Vacation days prediction")
plt.legend()
plt.show()