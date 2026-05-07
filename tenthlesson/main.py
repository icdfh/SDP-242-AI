import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# =========================
# 1. ДАТАСЕТ
# =========================

data = {
    "attendance": [95, 88, 70, 60, 98, 45, 80, 75, 90, 55,
                   85, 67, 92, 50, 78, 83, 40, 96, 72, 65,
                   89, 58, 76, 99, 62, 81, 47, 93, 69, 87],

    "homeworks_done": [10, 9, 6, 4, 10, 2, 8, 7, 9, 3,
                       8, 5, 10, 2, 7, 8, 1, 10, 6, 5,
                       9, 4, 7, 10, 4, 8, 2, 9, 6, 9],

    "test_score": [92, 85, 68, 55, 96, 40, 78, 72, 88, 50,
                   80, 63, 91, 45, 74, 79, 35, 97, 69, 60,
                   86, 52, 73, 99, 58, 81, 42, 90, 66, 84],

    "practice_hours": [25, 20, 12, 8, 30, 5, 18, 15, 22, 7,
                       19, 10, 24, 6, 14, 17, 4, 28, 13, 9,
                       21, 8, 16, 32, 10, 18, 5, 23, 11, 20],

    "missed_classes": [1, 2, 5, 8, 0, 12, 3, 4, 2, 9,
                       3, 6, 1, 10, 4, 3, 14, 0, 5, 7,
                       2, 8, 4, 0, 7, 3, 11, 1, 6, 2],

    "activity_score": [9, 8, 6, 4, 10, 3, 7, 7, 9, 4,
                       8, 5, 9, 3, 7, 8, 2, 10, 6, 5,
                       8, 4, 7, 10, 5, 8, 3, 9, 6, 8],

    "passed": [1, 1, 1, 0, 1, 0, 1, 1, 1, 0,
               1, 0, 1, 0, 1, 1, 0, 1, 1, 0,
               1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print("DATASET:")
print(df)

print("\nINFO:")
print(df.info())

print("\nDESCRIBE:")
print(df.describe())

print("\nTARGET BALANCE:")
print(df["passed"].value_counts())


# =========================
# 2. X И y
# =========================

X = df.drop("passed", axis=1)
y = df["passed"]


# =========================
# 3. TRAIN / TEST
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


# =========================
# 4. DECISION TREE
# =========================

tree_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

tree_model.fit(X_train, y_train)

y_pred_tree = tree_model.predict(X_test)


# =========================
# 5. RANDOM FOREST
# =========================

forest_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)

forest_model.fit(X_train, y_train)

y_pred_forest = forest_model.predict(X_test)


# =========================
# 6. СРАВНЕНИЕ ПРЕДСКАЗАНИЙ
# =========================

print("\nREAL VALUES:")
print(y_test.values)

print("\nDECISION TREE PRED:")
print(y_pred_tree)

print("\nRANDOM FOREST PRED:")
print(y_pred_forest)


# =========================
# 7. МЕТРИКИ DECISION TREE
# =========================

print("\n==============================")
print("DECISION TREE RESULTS")
print("==============================")

print("Accuracy:", accuracy_score(y_test, y_pred_tree))
print("Precision:", precision_score(y_test, y_pred_tree))
print("Recall:", recall_score(y_test, y_pred_tree))
print("F1-score:", f1_score(y_test, y_pred_tree))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_tree))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_tree))


# =========================
# 8. МЕТРИКИ RANDOM FOREST
# =========================

print("\n==============================")
print("RANDOM FOREST RESULTS")
print("==============================")

print("Accuracy:", accuracy_score(y_test, y_pred_forest))
print("Precision:", precision_score(y_test, y_pred_forest))
print("Recall:", recall_score(y_test, y_pred_forest))
print("F1-score:", f1_score(y_test, y_pred_forest))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_forest))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_forest))


# =========================
# 9. ОБЩАЯ ТАБЛИЦА СРАВНЕНИЯ
# =========================

results = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [
        accuracy_score(y_test, y_pred_tree),
        accuracy_score(y_test, y_pred_forest)
    ],
    "Precision": [
        precision_score(y_test, y_pred_tree),
        precision_score(y_test, y_pred_forest)
    ],
    "Recall": [
        recall_score(y_test, y_pred_tree),
        recall_score(y_test, y_pred_forest)
    ],
    "F1-score": [
        f1_score(y_test, y_pred_tree),
        f1_score(y_test, y_pred_forest)
    ]
})

print("\n==============================")
print("MODEL COMPARISON")
print("==============================")
print(results)


# =========================
# 10. ВИЗУАЛИЗАЦИЯ DECISION TREE
# =========================

plt.figure(figsize=(18, 10))

plot_tree(
    tree_model,
    feature_names=X.columns,
    class_names=["not passed", "passed"],
    filled=True,
    rounded=True
)

plt.title("Decision Tree Visualization")
plt.show()


# =========================
# 11. ВАЖНОСТЬ ПРИЗНАКОВ RANDOM FOREST
# =========================

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": forest_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n==============================")
print("RANDOM FOREST FEATURE IMPORTANCE")
print("==============================")
print(feature_importance)


plt.figure(figsize=(10, 6))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.show()