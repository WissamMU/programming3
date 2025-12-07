لهذا القسم انشء اشئلة على نفس هذا الشكل وارسل كل شي باللغة بايثون للنسخ جاهز
```python
# ==========================================================
# Comprehensive Test: Chapter 6 - Collection Types in Python
# ==========================================================


# ----------------------------------------------------------
# Q1: القوائم (Lists) الأساسية
# ----------------------------------------------------------
# أنشئ قائمة تحتوي على: [10, 20, 30, 40, 50]
# ثم قم بما يلي:
# 1. أضف الرقم 60 في النهاية
# 2. أضف الرقم 5 في البداية
# 3. احذف الرقم 30
# 4. اطبع القائمة النهائية وطولها

print("=== Q1 ===")
numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.insert(0, 5)
numbers.remove(30)
print(numbers)

# Expected output: [5, 10, 20, 40, 50, 60]
print()


# ----------------------------------------------------------
# Q2: عمليات الترتيب على القوائم
# ----------------------------------------------------------
# للقائمة: [45, 12, 89, 34, 67, 23, 90, 1]
# قم بما يلي:
# 1. رتب القائمة تصاعدياً (باستخدام sort())
# 2. رتب القائمة تنازلياً (باستخدام sorted())
# 3. اطبع كل من القائمة الأصلية والمترتبة تنازلياً

print("=== Q2 ===")
unsorted_list = [45, 12, 89, 34, 67, 23, 90, 1]

unsorted_list.sort()
print("using sort : ", unsorted_list)
useSorted = sorted(unsorted_list, reverse=True)
print("using sorted : ", useSorted)

print()


# ----------------------------------------------------------
# Q3: التجميعات (Tuples) والتفريغ
# ----------------------------------------------------------
# أنشئ تجميعة تحتوي على معلومات طالب:
# ("bob", 20, "average", 85.5)
# ثم:
# 1. فك التجميعة إلى 4 متغيرات
# 2. بدل قيم المتغيرين الأول والثالث
# 3. اطبع جميع القيم بعد التبديل

print("=== Q3 ===")
student_info = ("bob", 20, "ITE", 85.5)

name, age, major, grade = student_info
print(f"variables before swap: name:{name}, age:{age}, major:{major}, grade:{grade}")

name, major = major, name
print(f"after swap: name:{name}, age:{age}, major:{major}, grade:{grade}")

print()


# ----------------------------------------------------------
# Q4: المجموعات (Sets) والعمليات المجموعية
# ----------------------------------------------------------
# لدينا مجموعتين:
# set1 = {1, 2, 3, 4, 5, 6}
# set2 = {4, 5, 6, 7, 8, 9}
# قم بحساب:
# 1. اتحاد المجموعتين
# 2. تقاطع المجموعتين
# 3. الفرق بين المجموعتين (set1 - set2)

print("=== Q4 ===")
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

union_set = set1.union(set2)
print(f"union sets: {union_set}")

inter_set = set1.intersection(set2)
print(f"intersection sets: {inter_set}")

difference_set = set1.difference(set2)
print(f"difference sets: {difference_set}")

print()


# ----------------------------------------------------------
# Q5: القواميس (Dictionaries) الأساسية
# ----------------------------------------------------------
# أنشئ قاموساً لمعلومات طالب يحتوي على:
# - id: 101
# - name: "sara"
# - age: 21
# - grades: [85, 90, 78]
# ثم:
# 1. أضف حقل "major" بقيمة "ITE"
# 2. عدل قيمة العمر إلى 22
# 3. احسب متوسط الدرجات
# 4. اطبع جميع المفاتيح ثم القيم ثم كليهما 

print("=== Q5 ===")
student = {"id": 101, "name": "sara", "age": 21, "grades": [85, 90, 78]}

student['major'] = "ITE"
student["age"] = 22
grades = student["grades"]
averageGrades = sum(grades) / len(grades)
student["average"] = round(averageGrades, 2)

print("keys:")
for key in student.keys():
    print(f"- {key}")

print("\nvalues:")
for value in student.values():
    print(f"- {value}")

print("\nkeys and values:")
for key, value in student.items():
    print(f"{key}: {value}")
print()


# ----------------------------------------------------------
# Q6: التوابع المسبقة على جميع الأنماط
# ----------------------------------------------------------
# طبّق التوابع التالية على هياكل البيانات المختلفة:
# 1. len() على list, tuple, set, dict
# 2. sum() على list, tuple, set
# 3. max(), min() على list, tuple, set, dict
# 4. any(), all() على list, tuple, set, dict

print("=== Q6 ===")
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40, 50)
my_set = {5, 10, 15, 20, 25}
my_dict = {"a": 100, "b": 200, "c": 300}

# 1. تطبيق len()
print("len() function:")
print(f"  list length: {len(my_list)}")
print(f"  tuple length: {len(my_tuple)}")
print(f"  set length: {len(my_set)}")
print(f"  dict length: {len(my_dict)}")

# 2. تطبيق sum() (لا تعمل على dict)
print("\nsum() function:")
print(f"  list sum: {sum(my_list)}")
print(f"  tuple sum: {sum(my_tuple)}")
print(f"  set sum: {sum(my_set)}")

# 3. تطبيق max() و min()
print("\nmax() function:")
print(f"  list max: {max(my_list)}")
print(f"  tuple max: {max(my_tuple)}")
print(f"  set max: {max(my_set)}")
print(f"  dict max (keys): {max(my_dict)}")

print("\nmin() function:")
print(f"  list min: {min(my_list)}")
print(f"  tuple min: {min(my_tuple)}")
print(f"  set min: {min(my_set)}")
print(f"  dict min (keys): {min(my_dict)}")

# 4. تطبيق any() و all()
bool_list = [True, False, True]
bool_tuple = (False, False, False)
bool_set = {True, True, True}
bool_dict = {"": False, "a": True}

print("\nany() function:")
print(f"  list any: {any(bool_list)}")
print(f"  tuple any: {any(bool_tuple)}")
print(f"  set any: {any(bool_set)}")
print(f"  dict any: {any(bool_dict)}")

print("\nall() function:")
print(f"  list all: {all(bool_list)}")
print(f"  tuple all: {all(bool_tuple)}")
print(f"  set all: {all(bool_set)}")
print(f"  dict all: {all(bool_dict)}")
print()


# ----------------------------------------------------------
# Q7: التحويل بين الأنماط المختلفة
# ----------------------------------------------------------
# 1. حول القائمة [1, 2, 3, 4, 5] إلى tuple, set, dict
# 2. حول التجميعة (10, 20, 30) إلى list, set
# 3. حول المجموعة {1, 2, 3, 4} إلى list, tuple
# 4. حول القاموس {"a": 1, "b": 2} إلى list, tuple, set (المفاتيح فقط)

print("=== Q7 ===")

# 1. من list إلى أنواع أخرى
list_data = [1, 2, 3, 4, 5]
list_to_tuple = tuple(list_data)
list_to_set = set(list_data)
list_to_dict = dict(enumerate(list_data, start=1))

print("From list to other types:")
print(f"  list: {list_data}")
print(f"  tuple: {list_to_tuple}")
print(f"  set: {list_to_set}")
print(f"  dict: {list_to_dict}")

# 2. من tuple إلى أنواع أخرى
tuple_data = (10, 20, 30)
tuple_to_list = list(tuple_data)
tuple_to_set = set(tuple_data)

print("\nFrom tuple to other types:")
print(f"  tuple: {tuple_data}")
print(f"  list: {tuple_to_list}")
print(f"  set: {tuple_to_set}")

# 3. من set إلى أنواع أخرى
set_data = {1, 2, 3, 4}
set_to_list = list(set_data)
set_to_tuple = tuple(set_data)

print("\nFrom set to other types:")
print(f"  set: {set_data}")
print(f"  list: {set_to_list}")
print(f"  tuple: {set_to_tuple}")

# 4. من dict إلى أنواع أخرى (المفاتيح فقط)
dict_data = {"a": 1, "b": 2}
dict_to_list = list(dict_data)
dict_to_tuple = tuple(dict_data)
dict_to_set = set(dict_data)

print("\nFrom dict to other types (keys only):")
print(f"  dict: {dict_data}")
print(f"  list: {dict_to_list}")
print(f"  tuple: {dict_to_tuple}")
print(f"  set: {dict_to_set}")
print()


# ----------------------------------------------------------
# Q8: التوابع الخاصة بكل نمط
# ----------------------------------------------------------
# طبّق التوابع الخاصة على كل نمط من أنماط البيانات:
# - للقوائم: append(), insert(), remove(), sort(), reverse()
# - للتجميعات: count(), index()
# - للمجموعات: add(), remove(), union(), intersection()
# - للقواميس: keys(), values(), items(), get(), pop()

print("=== Q8 ===")

# 1. توابع القوائم
print("List functions:")
my_list = [3, 1, 4, 2]
print(f"  Original list: {my_list}")

my_list.append(5)
print(f"  After append(5): {my_list}")

my_list.insert(1, 0)
print(f"  After insert(1, 0): {my_list}")

my_list.remove(3)
print(f"  After remove(3): {my_list}")

my_list.sort()
print(f"  After sort(): {my_list}")

my_list.reverse()
print(f"  After reverse(): {my_list}")

# 2. توابع التجميعات
print("\nTuple functions:")
my_tuple = (1, 2, 2, 3, 3, 3, 4)
print(f"  Original tuple: {my_tuple}")

count_3 = my_tuple.count(3)
print(f"  count(3): {count_3}")

index_4 = my_tuple.index(4)
print(f"  index(4): {index_4}")

# 3. توابع المجموعات
print("\nSet functions:")
my_set = {1, 2, 3}
print(f"  Original set: {my_set}")

my_set.add(4)
print(f"  After add(4): {my_set}")

my_set.remove(2)
print(f"  After remove(2): {my_set}")

another_set = {3, 4, 5}
union_result = my_set.union(another_set)
print(f"  union({another_set}): {union_result}")

intersection_result = my_set.intersection(another_set)
print(f"  intersection({another_set}): {intersection_result}")

# 4. توابع القواميس
print("\nDictionary functions:")
my_dict = {"name": "Ahmed", "age": 25, "city": "Damascus"}
print(f"  Original dictionary: {my_dict}")

keys = my_dict.keys()
print(f"  keys(): {list(keys)}")

values = my_dict.values()
print(f"  values(): {list(values)}")

items = my_dict.items()
print(f"  items(): {list(items)}")

name = my_dict.get("name", "Unknown")
print(f"  get('name'): {name}")

age = my_dict.pop("age")
print(f"  After pop('age'): {my_dict} (Deleted age: {age})")
print()



# ----------------------------------------------------------
# Q9: مثال متكامل - إدارة الطلاب
# ----------------------------------------------------------
# أنشئ نظاماً لإدارة الطلاب باستخدام القواميس والقوائم:
# 1. قائمة من القواميس (كل قاموس يمثل طالباً)
# 2. حساب متوسط الدرجات لكل طالب
# 3. ترتيب الطلاب حسب المتوسط
# 4. إيجاد الطالب الأعلى والأقل درجة

print("=== Q9 ===")

# قاعدة بيانات الطلاب
students = [
    {"id": 101, "name": "Ahmed", "grades": [85, 90, 78]},
    {"id": 102, "name": "Sara", "grades": [92, 88, 95]},
    {"id": 103, "name": "Mohammed", "grades": [76, 85, 80]},
    {"id": 104, "name": "Fatima", "grades": [88, 92, 90]},
    {"id": 105, "name": "Yousef", "grades": [70, 75, 68]},
]

print("Original student database:")
for student in students:
    print(f"  {student}")

# 1. حساب المتوسط لكل طالب
for student in students:
    grades = student["grades"]
    student["average"] = sum(grades) / len(grades)

print("\nAfter adding average:")
for student in students:
    print(f"  {student['name']}: {student['average']:.2f}")

# 2. ترتيب الطلاب حسب المتوسط (تنازلياً)
sorted_students = sorted(students, key=lambda x: x["average"], reverse=True)

print("\nStudents sorted by average (descending):")
for i, student in enumerate(sorted_students, 1):
    print(f"  {i}. {student['name']}: {student['average']:.2f}")

# 3. إيجاد الطالب الأعلى والأقل درجة
highest_student = max(students, key=lambda x: x["average"])
lowest_student = min(students, key=lambda x: x["average"])

print(
    f"\nHighest student: {highest_student['name']} ({highest_student['average']:.2f})"
)
print(f"Lowest student: {lowest_student['name']} ({lowest_student['average']:.2f})")

# 4. استخدام set لإيجاد المواد الفريدة (افتراضية)
subjects = ["Math", "Physics", "Programming", "Math", "Physics"]
unique_subjects = set(subjects)
print(f"\nUnique subjects: {unique_subjects}")
print()


# ----------------------------------------------------------
# Q10: العمليات على القواميس المتقدمة
# ----------------------------------------------------------
# اكتب برنامجاً يحسب تكرار الكلمات في جملة باستخدام قاموس
# الجملة: "التعلم في بايثون سهل وممتع والتعلم في بايثون مفيد"

print("=== Q10 ===")

sentence = "التعلم في بايثون سهل وممتع والتعلم في بايثون مفيد"

# تحويل الجملة إلى قائمة كلمات
words = sentence.split()
print(f"Words: {words}")

# حساب تكرار الكلمات باستخدام قاموس
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord frequency:")
for word, count in word_count.items():
    print(f"  '{word}': {count} times")

# ترتيب الكلمات حسب التكرار
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("\nWords sorted by frequency:")
for word, count in sorted_words:
    print(f"  {word}: {count}")

# استخدام Counter من collections للحصول على نفس النتيجة
from collections import Counter

counter_result = Counter(words)
print(f"\nUsing Counter: {counter_result}")
print()


# ----------------------------------------------------------
# Q11: مقارنة بين جميع الأنماط التجميعية
# ----------------------------------------------------------
# قارن بين الأنماط الأربعة من حيث:
# 1. قابلية الفهرسة (indexing)
# 2. قابلية التغيير (mutability)
# 3. السماح بالتكرار (allow duplicates)
# 4. الترتيب (order preservation)

print("=== Q11 ===")

print("Comparison between collection types:")
print("-" * 60)
print("Type        | Indexing | Mutable | Duplicates | Ordered")
print("-" * 60)

# القوائم (Lists)
list_example = [1, 2, 3, 2]
print(f"list        |   Yes    |   Yes   |    Yes     |   Yes   | Example: {list_example}")

# التجميعات (Tuples)
tuple_example = (1, 2, 3, 2)
print(f"tuple       |   Yes    |   No    |    Yes     |   Yes   | Example: {tuple_example}")

# المجموعات (Sets)
set_example = {1, 2, 3}  # لا يسمح بالتكرار
print(f"set         |   No     |   Yes   |    No      |   No    | Example: {set_example}")

# القواميس (Dictionaries)
dict_example = {"a": 1, "b": 2, "c": 3}
print(f"dict        |   Yes*   |   Yes   |    No*     |   Yes   | Example: {dict_example}")
print("             (by key)             (*in keys)")
print("-" * 60)

# شرح إضافي
print("\nNotes:")
print("1. Tuples are faster than lists and more secure")
print("2. Sets are ideal for element search and mathematical operations")
print("3. Dictionaries are ideal for data associated with keys")
print("4. Lists are the most flexible and common")
print()


# ==========================================================
# End of Chapter 6 Comprehensive Test
# ==========================================================
```
واجلب الاسئلة من هنا تاكد من وجدو سؤال واحد لكل فكرة على الاقل 

