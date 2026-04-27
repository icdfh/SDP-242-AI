import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# 1. Датасет
data = {
    "hours": [
        1, 2, 2, 3, 4, 5, 6, 7, 8, 9,
        3, 6, 5, 7, 9, 10, 1, 4, 6, 9,
        2, 3, 4, 5, 6, 7, 8, 2, 10, 1,
        3, 4, 5, 6, 7, 8, 9, 10, 2, 3,
        4, 5, 6, 7, 8, 9, 10, 1, 2, 3,
        4, 5, 6, 7, 8, 9, 10, 2, 5, 7
    ],

    "attendance": [
        40, 50, 55, 60, 65, 75, 80, 85, 90, 95,
        58, 78, 82, 88, 91, 96, 35, 62, 79, 94,
        80, 45, 90, 50, 60, 70, 55, 92, 65, 88,
        52, 68, 73, 81, 86, 89, 93, 97, 48, 66,
        72, 77, 83, 87, 90, 92, 98, 38, 57, 63,
        69, 74, 84, 86, 91, 95, 99, 54, 71, 76
    ],

    "tasks": [
        1, 2, 3, 3, 5, 6, 7, 8, 10, 12,
        4, 7, 8, 9, 11, 13, 1, 5, 8, 12,
        6, 2, 4, 9, 3, 5, 6, 1, 7, 4,
        3, 5, 6, 7, 8, 9, 10, 12, 2, 4,
        6, 7, 8, 9, 10, 11, 13, 2, 3, 5,
        6, 7, 8, 9, 10, 12, 14, 4, 5, 7
    ],

    "passed": [
        0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
        0, 1, 1, 1, 1, 1, 0, 0, 1, 1,
        1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 1
    ]
}

df = pd.DataFrame(data)

print("Первые строки датасета:")
print(df.head())

print("\nРазмер датасета:")
print(df.shape)

print("\nКоличество классов:")
print(df["passed"].value_counts())


# 2. Делим данные на признаки и целевую переменную
X = df[["hours", "tasks", "attendance"]]
y = df["passed"]


# 3. Делим данные на train и test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


# 4. Масштабирование данных
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 5. Создаем модели
log_model = LogisticRegression()
knn_model = KNeighborsClassifier(n_neighbors=3)


# 6. Обучаем модели
log_model.fit(X_train_scaled, y_train)
knn_model.fit(X_train_scaled, y_train)


# 7. Делаем предсказания
log_pred = log_model.predict(X_test_scaled)
knn_pred = knn_model.predict(X_test_scaled)


# 8. Метрики Logistic Regression
print("\n" + "=" * 50)
print("LOGISTIC REGRESSION")
print("=" * 50)

print("Accuracy:", accuracy_score(y_test, log_pred))
print("Precision:", precision_score(y_test, log_pred))
print("Recall:", recall_score(y_test, log_pred))
print("F1:", f1_score(y_test, log_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, log_pred))

print("\nClassification Report:")
print(classification_report(y_test, log_pred))


# 9. Метрики KNN
print("\n" + "=" * 50)
print("KNN")
print("=" * 50)

print("Accuracy:", accuracy_score(y_test, knn_pred))
print("Precision:", precision_score(y_test, knn_pred))
print("Recall:", recall_score(y_test, knn_pred))
print("F1:", f1_score(y_test, knn_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, knn_pred))

print("\nClassification Report:")
print(classification_report(y_test, knn_pred))


# 10. Таблица сравнения моделей
comparison = pd.DataFrame({
    "Метрика": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1-score"
    ],

    "Перевод": [
        "Общая точность модели",
        "Точность положительных предсказаний",
        "Полнота / способность находить всех сдавших",
        "Средний баланс между Precision и Recall"
    ],

    "Logistic Regression": [
        accuracy_score(y_test, log_pred),
        precision_score(y_test, log_pred),
        recall_score(y_test, log_pred),
        f1_score(y_test, log_pred)
    ],

    "KNN": [
        accuracy_score(y_test, knn_pred),
        precision_score(y_test, knn_pred),
        recall_score(y_test, knn_pred),
        f1_score(y_test, knn_pred)
    ]
})

print("\n" + "=" * 50)
print("СРАВНЕНИЕ МОДЕЛЕЙ")
print("=" * 50)

print(comparison)


# 11. Определяем лучшую модель по F1-score
log_f1 = f1_score(y_test, log_pred)
knn_f1 = f1_score(y_test, knn_pred)

print("\n" + "=" * 50)
print("ВЫВОД")
print("=" * 50)

if log_f1 > knn_f1:
    print("Лучше сработала Logistic Regression, потому что у нее выше F1-score.")
elif knn_f1 > log_f1:
    print("Лучше сработала KNN, потому что у нее выше F1-score.")
else:
    print("Обе модели показали одинаковый F1-score.")


# 12. Новый студент
new_student = pd.DataFrame({
    "hours": [6],
    "tasks": [7],
    "attendance": [80]
})

print("\n" + "=" * 50)
print("НОВЫЙ СТУДЕНТ")
print("=" * 50)

print(new_student)


# 13. Масштабируем нового студента
new_student_scaled = scaler.transform(new_student)


# 14. Предсказание Logistic Regression
log_new_pred = log_model.predict(new_student_scaled)
log_new_proba = log_model.predict_proba(new_student_scaled)


# 15. Предсказание KNN
knn_new_pred = knn_model.predict(new_student_scaled)
knn_new_proba = knn_model.predict_proba(new_student_scaled)


# 16. Таблица с вероятностями для нового студента
new_student_result = pd.DataFrame({
    "Модель": [
        "Logistic Regression",
        "KNN"
    ],

    "Предсказание": [
        "Сдал" if log_new_pred[0] == 1 else "Не сдал",
        "Сдал" if knn_new_pred[0] == 1 else "Не сдал"
    ],

    "Вероятность не сдать": [
        round(log_new_proba[0][0] * 100, 2),
        round(knn_new_proba[0][0] * 100, 2)
    ],

    "Вероятность сдать": [
        round(log_new_proba[0][1] * 100, 2),
        round(knn_new_proba[0][1] * 100, 2)
    ]
})

print("\n" + "=" * 50)
print("ПРЕДСКАЗАНИЕ ДЛЯ НОВОГО СТУДЕНТА")
print("=" * 50)

print(new_student_result)