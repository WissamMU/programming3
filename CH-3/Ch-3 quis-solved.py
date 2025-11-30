# ==========================================================
# اختبار الفصل الثالث: السلاسل الحرفية والملفات النصية
# ==========================================================
# قُم بكتابة الكود المطلوب في الأماكن المخصصة تحت كل سؤال
# لا تُعدّل على التعليقات أو هيكل الملف
# ==========================================================


# ----------------------------------------------------------
# Q1: تعريف السلاسل الحرفية واستخدام المحارف الخاصة
# ----------------------------------------------------------
# أنشئ السلاسل التالية:
# 1. سلسلة عادية تحتوي على مسار: C:\Users\Documents
# 2. سلسلة raw string لنفس المسار
# 3. سلسلة تحتوي على سطرين باستخدام \n

print("=== Q1 ===")
path1 = "C:\\Users\\Documents"
path2 = r"C:\Users\Documents"
multiline = "Line One\nLine Two"

print("1.", path1)
print("2.", path2)
print("3.", multiline)
print()


# ----------------------------------------------------------
# Q2: صياغة السلاسل باستخدام طرق مختلفة
# ----------------------------------------------------------
# أنشئ نفس السلسلة "لدي 5 كتب و 3 أقلام" باستخدام:
# 1. طريقة الجمع (+)
# 2. طريقة format()
# 3. طريقة printf-style (%)

print("=== Q2 ===")
# الطريقة 1: الجمع
str1 = "I have " + "5" + " books and " + "3" + " pens"

# الطريقة 2: format()
str2 = "I have {} books and {} pens".format(5, 3)

# الطريقة 3: printf-style
str3 = "I have %d books and %d pens" % (5, 3)

print("1.", str1)
print("2.", str2)
print("3.", str3)
print()


# ----------------------------------------------------------
# Q3: تنسيق الأرقام في السلاسل
# ----------------------------------------------------------
# للرقم x = 1234.56789
# اطبع القيمة بالتنسيقات التالية:
# 1. محصور في 10 خانات مع منزلتين عشريتين
# 2. محصور في 12 خانة مع 4 منازل عشرية
# 3. مع فواصل الآلاف ومنزلتين عشريتين

print("=== Q3 ===")
x = 1234.56789

print("1 = {:010.2f}".format(x))
print("2 = {:012.4f}".format(x))
print("3 = {:010,.2f}".format(x))

print()


# ----------------------------------------------------------
# Q4: العمليات الأساسية على السلاسل
# ----------------------------------------------------------
# للسلاسل: s1 = "Hello", s2 = "WORLD"
# قم بما يلي:
# 1. ادمج السلسلتين مع فراغ بينهما
# 2. حوّل s1 لأحرف كبيرة و s2 لأحرف صغيرة
# 3. اطبع طول السلسلة الناتجة

print("=== Q4 ===")
s1 = "Hello"
s2 = "WORLD"

# 1. الدمج
combined = s1 + " " + s2

# 2. التحويل
upper_s1 = s1.upper()
lower_s2 = s2.lower()

# 3. الطول
length = len(combined)

print("Combined:", combined)
print("s1 uppercase:", upper_s1)
print("s2 lowercase:", lower_s2)
print("Length:", length)
print()


# ----------------------------------------------------------
# Q5: البحث في السلاسل
# ----------------------------------------------------------
# للسلسلة: text = "Python programming is fun and Python is powerful"
# ابحث عن:
# 1. أول ظهور لكلمة "Python"
# 2. آخر ظهور لكلمة "Python"
# 3. هل تبدأ السلسلة بـ "Python"؟
# 4. هل تنتهي السلسلة بـ "powerful"؟

print("=== Q5 ===")
text = "Python programming is fun and Python is powerful"

first_index = text.index("Python")
last_index = text.rindex("Python")
starts_with = text.startswith("Python")
ends_with = text.endswith("powerful")

print("First occurrence of Python:", first_index)
print("Last occurrence of Python:", last_index)
print("Starts with Python:", starts_with)
print("Ends with powerful:", ends_with)
print()


# ----------------------------------------------------------
# Q6: تقسيم السلاسل ودمجها
# ----------------------------------------------------------
# للسلسلة: data = "apple,banana,orange,grape"
# 1. قسم السلسلة باستخدام الفاصلة
# 2. ادمج القائمة الناتجة باستخدام - كفاصل
# 3. أزل الفراغات الزائدة من السلسلة: "  hello world  "

print("=== Q6 ===")
data = "apple,banana,orange,grape"

# 1. التقسيم
fruits_list = data.split(",")

# 2. الدمج
joined_fruits = "-".join(fruits_list)

# 3. إزالة الفراغات
spaced_text = "  hello world  "
stripped_text = spaced_text.strip()

print("Split:", fruits_list)
print("Joined:", joined_fruits)
print("After stripping:", repr(stripped_text))
print()


# ----------------------------------------------------------
# Q7: الشرائح (Slicing) في السلاسل
# ----------------------------------------------------------
# للسلسلة: s = "Hello World"
# اطبع:
# 1. الأحرف من 2 إلى 7
# 2. الأحرف من البداية إلى 5
# 3. الأحرف من 6 إلى النهاية
# 4. كل حرف ثاني في السلسلة

print("=== Q7 ===")
s = "Hello World"

print("1. [2:7]:", s[2:7])
print("2. [:5]:", s[:5])
print("3. [6:]:", s[6:])
print("4. [::2]:", s[::2])
print()


# ----------------------------------------------------------
# Q8: ضرب السلاسل (خاصية بايثون)
# ----------------------------------------------------------
# 1. كرر السلسلة "Hi " 3 مرات
# 2. اطبع جدول الضرب للرقم 3 باستخدام ضرب السلاسل (من 1 إلى 5)

print("=== Q8 ===")
# 1. التكرار
repeated = "Hi " * 3

# 2. جدول الضرب
print("1.", repeated)
print("2. Multiplication table for 3:")
for i in range(1, 6):
    result = "3" * i
    print(f"3 x {i} = {result}")
print()


# ----------------------------------------------------------
# Q9: معالجة بيانات الطلاب من الإدخال
# ----------------------------------------------------------
# اكتب برنامجاً يطلب إدخال بيانات طالب بالصيغة: "id eng math prog name"
# ثم يقسم المدخلات ويحولها للأنواع المناسبة ويطبع أعلى درجة

print("=== Q9 ===")


def process_student_data():
    # محاكاة الإدخال - في الواقع نستخدم input()
    # line = input("Enter student data: ")
    line = "20510 85 60 80 Sami"  # لمحاكاة الإدخال

    items = line.split()
    id = int(items[0])
    eng = float(items[1])
    math = float(items[2])
    prog = float(items[3])
    name = items[4]

    max_grade = max(eng, math, prog)
    print(f"{id} {name} Highest grade: {max_grade}")


process_student_data()
print()


# ----------------------------------------------------------
# Q10: البحث عن كلمة وعد تكراراتها
# ----------------------------------------------------------
# اكتب برنامجاً يبحث عن كلمة "the" في النص التالي ويعد مرات ظهورها:
# text = "The cat is on the table and the dog is under the table"

print("=== Q10 ===")
text = "The cat is on the table and the dog is under the table"
search_word = "the"

# البحث مع تجاهل حالة الحرف
lower_text = text.lower()
count = lower_text.count(search_word)

print(f"Word '{search_word}' appears {count} times")
print()


# ----------------------------------------------------------
# Q11: عرض الترميز Unicode للأحرف
# ----------------------------------------------------------
# اطبع الترميز Unicode للأحرف من 1570 إلى 1580 مع الأحرف العربية المقابلة

print("=== Q11 ===")
print("Arabic Unicode characters:")
for i in range(1570, 1581):
    print(f"{i} = {chr(i)}")
print()


# ----------------------------------------------------------
# Q12: الكتابة في ملف نصي
# ----------------------------------------------------------
# 1. أنشئ ملفاً جديداً واكتب فيه 3 أسطر
# 2. أضف سطرين إضافيين للملف نفسه

print("=== Q12 ===")

loc = "CH-3/testing.txt"

with open(loc, "w") as file:
    file.write("Hello, World!\n")

with open(loc, "a") as file:
    file.write("append line one\n")
    file.write("append line two\n")

print("task complete")

print()


# ----------------------------------------------------------
# Q13: القراءة من ملف نصي
# ----------------------------------------------------------
# اقرأ الملف الذي أنشأته في السؤال السابق باستخدام:
# 1. read() - قراءة كاملة
# 2. readlines() - قراءة كقائمة
# 3. التكرار المباشر على الملف

print("=== Q13 ===")

# 1. قراءة كاملة

with open(loc,"r") as file:
    print('\nusing read : \n' , file.read())

# 2. قراءة كقائمة

print("="*25)
with open(loc,"r") as file:
    print('\nusing readlines : \n')
    lines = file.readlines()
    print(lines)
# 3. التكرار المباشر
    print('\nusing loop : \n')
    for i in range(len(lines)):
        print(lines[i])
    
print()


# ----------------------------------------------------------
# Q14: معالجة بيانات الطلاب من ملف
# ----------------------------------------------------------
# افترض وجود ملف students.txt يحتوي على:
# 20510 85 60 80 Sami
# 20420 60 80 90 Rana
# 20600 95 70 50 Jamil
# اقرأ الملف وعرض بيانات كل طالب مع أعلى درجة

print("=== Q14 ===")
# أولاً ننشئ الملف للاختبار

loc = "CH-3/students.txt"

with open(loc , 'w') as file:
    file.write("20510 85 60 80 Sami\n") 
    file.write("20420 60 80 90 Rana\n") 
    file.write("20600 95 70 50 Jamil\n") 

print('\nStudent data:\n')

with open(loc,'r') as file:
    for line in file:
        items = line.split()
        if len(items) >= 5:
            id = items[0]
            eng = float(items[1])
            math = float(items[2])
            prog = float(items[3])
            name = items[4]
            max_grade = max(eng, math, prog)
            print(f"{id} {name}: Highest grade = {max_grade}")

print()


# ----------------------------------------------------------
# Q15: التحويل بين المحارف والأرقام
# ----------------------------------------------------------
# 1. حول الحرف 'A' إلى كود Unicode
# 2. حول الرقم 66 إلى الحرف المقابل
# 3. اطبع الحروف من 'A' إلى 'Z'



print("=== Q15 ===")
# 1. char to Unicode
char_code = ord('A')

# 2. Unicode to char
char_from_code = chr(66)

# 3. A to Z
print("1. Code of 'A':", char_code)
print("2. Character from 66:", char_from_code)
print("3. Letters from A to Z:")
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end=' ')
print("\n")


# ----------------------------------------------------------
# Q16: برنامج متكامل لتحليل النص
# ----------------------------------------------------------
# اكتب برنامجاً يأخذ نصاً ويقوم بما يلي:
# 1. يعد عدد الكلمات
# 2. يعد عدد الجمل (تفترض أن الجملة تنتهي بـ . أو ! أو ؟)
# 3. يحول النص لأحرف صغيرة
# 4. يبحث عن كلمة محددة يطلبها المستخدم
#sample_text = "Hello world! This is a test. How are you? I am fine."

print("=== Q16 ===")

sample_text = "Hello world! This is a test. How are you? I am fine."

def analyze_text(text):
    # 1. عدد الكلمات
    words = text.split()
    word_count = len(words)
    
    # 2. عدد الجمل
    sentence_count = 0
    for char in text:
        if char in '.!?':
            sentence_count += 1
    
    # 3. تحويل لأحرف صغيرة
    lower_text = text.lower()
    
    # 4. البحث عن كلمة (محاكاة)
    search_word = "the"  # في الواقع نستخدم input()
    search_count = lower_text.count(search_word)
    
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentence_count}")
    print(f"Text in lowercase: {lower_text}")
    print(f"Word '{search_word}' appears {search_count} times")

analyze_text(sample_text)
print()


# ----------------------------------------------------------
# Q17: مقارنة السلاسل
# ----------------------------------------------------------
# قارن بين السلاسل التالية مع وبدون مراعاة حالة الحرف:
# s1 = "Hello", s2 = "hello", s3 = "HELLO"

print("=== Q17 ===")
s1 = "Hello"
s2 = "hello"
s3 = "HELLO"

print("Case sensitive:")
print(f"s1 == s2: {s1 == s2}")
print(f"s1 == s3: {s1 == s3}")

print("Case insensitive (after conversion):")
print(f"s1.lower() == s2.lower(): {s1.lower() == s2.lower()}")
print(f"s1.lower() == s3.lower(): {s1.lower() == s3.lower()}")
print()


# ----------------------------------------------------------
# Q18: استخدام التوابع المسبقة مع السلاسل
# ----------------------------------------------------------
# استخدم التوابع: len(), max(), min(), str() مع السلاسل واشرح النتائج

print("=== Q18 ===")
test_string = "PythonProgramming"

print(f"String: {test_string}")
print(f"len(): {len(test_string)} - String length")
print(f"max(): {max(test_string)} - Highest Unicode value in string")
print(f"min(): {min(test_string)} - Lowest Unicode value in string")

number = 123
converted = str(number)
print(f"str(123): {converted} - Convert number to string")
print(f"Type of str(123): {type(converted)}")
print()


# ----------------------------------------------------------
# Q19: إنشاء سلسلة من قائمة
# ----------------------------------------------------------
# حول القائمة ['a', 'b', 'c', 'd'] إلى السلسلة "a, b, c, d"

print("=== Q19 ===")
my_list = ['a', 'b', 'c', 'd']
result_string = ", ".join(my_list)

print(f"List: {my_list}")
print(f"Result string: {result_string}")
print()


# ----------------------------------------------------------
# Q20: معالجة الملفات المتقدمة
# ----------------------------------------------------------
# اكتب برنامجاً ينسخ محتوى ملف إلى ملف آخر مع إضافة رقم لكل سطر

print("=== Q20 ===")

with open(loc , "r") as file:
    lines = file.readlines()
    
with open("CH-3/studentsCopy.txt" , "w") as file:
    for i in range(len(lines)):
        line = f"{i+1} : {lines[i]}"
        file.write(line)
        
print()


# ==========================================================
# نهاية اختبار الفصل الثالث
# ==========================================================
