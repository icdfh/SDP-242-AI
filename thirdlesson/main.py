# with open('thirdlesson/data/input.txt', "r", encoding='utf-8') as f:
#     text = f.read()

# print(text)
# with open('thirdlesson/data/input.txt', "r", encoding='utf-8') as f:
#     for line in f:
#         print(line)

# with open('thirdlesson/data/input.txt', "r", encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())

# s = "    hello"
# print(s.strip())

# text = "hi         there          friend"
# clean  = " ".join(text.split())
# print(clean)

# text = "Python AI"
# example = text.split()
# print(example)

# text = "Python AI"
# print(text.upper())
# text = "Python AI"
# print(text.lower())

# with open("thirdlesson/data/input.txt", "w", encoding="utf-8") as f:
#     f.write("Line 1\n")
#     f.write("Line 2\n")

# with open("thirdlesson/data/input.txt", "a", encoding="utf-8") as f:
#     f.write("New action")

# with open("thirdlesson/data/raw.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# text = text.lower()
# text = " ".join(text.split())

# with open("thirdlesson/data/clean.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# print("Готово! Сохранено в clean.txt ")

# counts = {}

# with open("thirdlesson/data/shop.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         item = line.strip()
#         if item == "":
#             continue

#         if item not in counts:
#             counts[item] = 0
#         counts[item] += 1

# best_item = None
# best_count = -1

# for item, c in counts.items():
#     if c > best_count:
#         best_count = c
#         best_item = item

# print("Частоты: ", counts)
# print("Топ товар", best_item, best_count)

# with open("thirdlesson/data/report.txt", "w", encoding="utf-8") as f:
#     f.write("===REPORT===\n")
#     for item,c in counts.items():
#         f.write(f"{item}: {c}\n")
#     f.write(f"\nTOP: {best_item}: ({best_count})")


# google 
# youtube
# google
# instagram
# youtube
# tiktok
# tiktok
# google
# youtube

# Прочитать файл
# Посчитать сколько раз встретился каждый сайт
# Найти самый посещаемый сайт
# Вывести статистику в консоль
# Сохранить отчет в visits_report.txt

# visits = {}
# with open("thirdlesson/data/visits.txt","r", encoding="utf-8") as f:
#     for line in f:
#         site = line.strip()

#         if site == "":
#             continue
        
#         if site not in visits:
#             visits[site] = 0
        
#         visits[site] += 1

# total = sum(visits.values())

# top_site = None
# top_count = -1

# for site,count in visits.items():
#     if count > top_count:
#         top_count = count
#         top_site = site

# print("===VISITS REPORT===")
# print(f"Total visits: {total}\n")

# for site, count in visits.items():
#     percent = round(count / total * 100, 1)
#     print(f"{site}: {count} ({percent}%)")

# print(f"\nTOP SITE: {top_site} ({top_count})")

# with open("thirdlesson/data/visits_report.txt", "w", encoding="utf-8") as f:
#     f.write(f"{site}: {count} ({percent})")
#     f.write(f"\nTOP: {top_site}: ({top_count}) ({percent})")

# import csv
# students =  []
# with open("thirdlesson/data/students.csv", "r", encoding ="utf-8") as f:
#     reader = csv.DictReader(f)
#     # for row in reader:
#     #     students.append(row)
#     for row in reader:
#         row["age"] = int(row["age"])
#         row["grade"] = int(row["grade"])
#         students.append(row)
# print(students)



# students = [
#     {"name": "Ali", "age": 18, "grade": 90},
#     {"name": "Diana", "age": 19, "grade": 87},
# ]

# with open("thirdlesson/data/out_students.csv", "w", encoding="utf-8", newline="") as f:
#     fieldnames = ["name", "age", "grade"]
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(students)

# import json
# import csv
# with open("thirdlesson/data/profile.json", "r",encoding="utf-8") as f:
#     data = json.load(f)

# print(data)
# print(type(data))


# data = {
#     "course": "Питон",
#     "lesson": 3,
#     "topics": ["files", "csv", "json"],
#     "students": 13
# }
# with open("thirdlesson/data/meta.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=1)


import json, csv

students = []
with open("thirdlesson/data/students.csv", "r", 
          encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])
        row["grade"] = int(row["grade"])
        students.append(row)

count = len(students)

total = 0
for s in students:
    total += s["grade"]

avg_grade = total/count if count > 0 else 0

report = {
    "count": count,
    "avg_grade": avg_grade,
    "students": students,
}
with open("thirdlesson/data/students_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=1)

print("Запушено")


