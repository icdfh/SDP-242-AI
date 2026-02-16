# list
# nums = [1,2,3,4]
# nums.append(5)
# nums[0] = 99
# print(nums)
# nums[0:3]


# tuple
# point = (10,3)
# print[0] = 99 ОШИБКА ТАК ДЕЛАТЬ НЕЛЬЗЯ

# dict
# student = {
#     "name": "Ali",
#     "age": 16
# }
# print(student["name"])
# student["age"] += 1

# nums = [5,5,2,2,2,3,3,3,5,1,1,1]
# freq = {}

# for i in nums:
#     freq[i] = freq.get(i, 0) + 1
# print(freq)

# set

# bad_words = {"spam", "scam", "fake"}
# word = "spam"
# print(word in bad_words) True O(1) 

# A = {"python", "sql", "ml"}
# B = {"python", "react", "sql"}
# print(A & B)
# print(A | B) {"python","sql", "ml", "react"}
# print(B - A) 
# tuple, str, int, float


# students = [
#     {"name": "Ali", "grades": [90,80,79]},
#     {"name": "Dana", "grades": [100, 95]}
# ]
# print(students[0]["grades"][2])
# for i in students:
#     avg = sum(i["grades"]) / len(i["grades"])
#     print(i["name"], "avg=", avg)

# data = {
#     "age": [10,20,16,14,18],
#     "city": ["Almaty", "Astana", "Aktobe","Shymkent"]
# }
# pandas DataFrame

# Условие дан список email/слов -> вывсти уникальные и количество дублей

# items = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com", "b@gmail.com", "b@gmail.com"]

# unique = set(items)
# duplicates_count = len(items) - len(unique)
# print("unique:", unique)
# print("duplicates:", duplicates_count)

# items = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com", "b@gmail.com", "b@gmail.com"]

# seen = set()
# dups = set()

# for i in items:
#     if i in seen:
#         dups.add(i)
#     else:
#         seen.add(i)
# print("unique:", seen)
# print("duplicates_count:", len(items) - len(seen))
# print("duplicated_values", dups)

# Частоты слов в строке str -> split []

# text = "AI Is cool and AI is useful"
# words = text.lower().split()

# freq = {}
# for i in words:
#     freq[i] = freq.get(i,0) + 1

# print("freq:", freq)
# условие список словарей товаров {category, price} ->собрать dict category -> list prices
# products = [
#     {"title": "Iphone", "category":"mobile", "price":500000},
#     {"title": "Pixel", "category":"mobile", "price":450000},
#     {"title": "Macbook", "category":"laptop", "price":650000},
#     {"title": "Lenovo", "category":"laptop", "price":550000},
#     {"title": "Ipad", "category":"tablet", "price":300000}
# ]

# group = {}
# for i in products:
#     cat = i["category"]
#     price = i["price"]

#     if cat not in group:
#         group[cat] = []
#     group[cat].append(price)
# print(group)

# person1 = {"python", "sql", "ml","react"}
# person2 = {"react", "design", "python","figma"}

# common = person1 & person2
# only = person1 - person2
# only2 = person2 - person1
# all_interests = person1 | person2

# print("Common:", common)
# print("only person1:",only)
# print("only person2:",only2)
# print("all:",all_interests)



# class Student:
#     def __init__(self,name,grades):
#         self.name = name
#         self.grades = grades
    
#     def info(self):
#         print(f"Студент: {self.name}, Оценки: {self.grades}")
    
#     def avg(self):
#         return sum(self.grades) / len(self.grades)
    
# s1 = Student("Mansur", [90,80,70])
# s2 = Student("Aisha", [100,95,100])

# print(s1.name)
# s1.info()
# print(s1.avg())
# print(s2.name)
# s2.info()
# print(s2.avg()) 