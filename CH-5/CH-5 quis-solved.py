# ==========================================================
# اختبار الفصل الخامس: معالجة الاستثناءات في بايثون
# ==========================================================
# قُم بكتابة الكود المطلوب في الأماكن المخصصة تحت كل سؤال
# لا تُعدّل على التعليقات أو هيكل الملف
# ==========================================================


# ----------------------------------------------------------
# Q1: البنية الأساسية لمعالجة الاستثناءات
# ----------------------------------------------------------
# اكتب كود يحاول قسمة عددين يدخلهما المستخدم
# واستخدم try-except للتعامل مع القسمة على الصفر

print("=== Q1 ===")


def div():
    while True:  # keep looping until valid input
        try:
            print("Divide by zero try-except")
            n1 = int(input("enter first number : "))
            n2 = int(input("enter second number : "))
            result = n1 / n2
            print(f"{n1} / {n2} = {result}")
            break  # exit loop when everything works
        except ZeroDivisionError:
            print("Error: you can't divide by Zero! Try again.\n")
        except ValueError:
            print("Error: enter numbers only! Try again.\n")


div()
print()

# ----------------------------------------------------------
# Q2: معالجة أنواع متعددة من الاستثناءات
# ----------------------------------------------------------
# اكتب دالة تطلب من المستخدم إدخال رقم، وتحاول تحويل هذا الإدخال إلى عدد صحيح باستخدام الدالة int().
# يجب عليك معالجة الاستثناءات التالية:
# ValueError إذا كان الإدخال غير صالح للتحويل إلى عدد صحيح.
# TypeError إذا تم تمرير نوع غير مناسب للتحويل.

print("=== Q2 ===")

def convert_to_int():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        print(f"Converted number: {number}")
    except ValueError:
        print("Error: Cannot convert input to integer")
    except TypeError:
        print("Error: Data type is not appropriate")


convert_to_int()
print()


# ----------------------------------------------------------
# Q3: استخدام كتلة finally
# ----------------------------------------------------------
# اكتب كود يفتح ملفاً للقراءة مع استخدام finally
# للتأكد من إغلاق الملف بغض النظر عن النتيجة

print("=== Q3 ===")


def read_file_safely(filename):
    file = None
    try:
        file = open(filename , 'r')
        content = file.read()
        print('file contents : ' , content)
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    finally:
        if file:
            file.close()
            print("File closed successfully")

        

read_file_safely("example.txt")
read_file_safely("testing.py")
print()


# ----------------------------------------------------------
# Q4: التقاط استثناء محدد بمعلومياته
# ----------------------------------------------------------
# اكتب كود يلتقط استثناء IndexError ويعرض رسالة الخطأ الكاملة

print("=== Q4 ===")


def handle_index_error():
    my_list = [1, 2, 3]
    try:
        print(my_list[5])
    except IndexError as e:
        print(f"Index error occurred: {e}")
        print(f'Erorr type: {type(e)}')


handle_index_error()
print()


# ----------------------------------------------------------
# Q5: معالجة استثناءات القوائم
# ----------------------------------------------------------
# للسلسلة: numbers = [10, 20, 30, 40, 50]
# اكتب كود يطلب من المستخدم إدخال index ويعرض القيمة
# وعالج حالة الفهرس خارج النطاق

print("=== Q5 ===")


def access_list_element():
    numbers = [10, 20, 30, 40, 50]
    try:
        index = int(input("Enter element index (0-4): "))
        print(f"Value at index {index}: {numbers[index]}")
    except IndexError:
        print("Error: Index out of list range")
    except ValueError:
        print("Error: Please enter an integer only")   


access_list_element()
print()


# ----------------------------------------------------------
# Q6: استخدام multiple except blocks
# ----------------------------------------------------------
# اكتب كود يحول مدخلين إلى أعداد ويعمل عليهما عملية حسابية
# وعالج كل نوع خطأ في كتلة except منفصلة

print("=== Q6 ===")


def multiple_exceptions():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a**b  # Power operation
        print(f"Result: {a} ^ {b} = {result}")
    except ValueError:
        print("Error: Please enter integers only")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except OverflowError:
        print("Error: Result is too large")
    except Exception as e:
        print(f"Unexpected error: {e}")


multiple_exceptions()
print()


# ----------------------------------------------------------
# Q7: إنشاء دالة آمنة للإدخال
# ----------------------------------------------------------
# اكتب دالة get_safe_input() تطلب من المستخدم إدخال عدد عشري
# وتكرر الطلب حتى يدخل المستخدم قيمة صحيحة

print("=== Q7 ===")


def get_safe_float():
    while True:
        try:
            user_input = input("Enter a float number: ")
            number = float(user_input)
            return number
        except ValueError:
            print("Error: Please enter a valid float number. Try again")


result = get_safe_float()
print(f"Entered value: {result}")
print()


# ----------------------------------------------------------
# Q8: معالجة استثناءات القواميس
# ----------------------------------------------------------
# اكتب كود يطلب مفتاحاً من المستخدم ويعرض قيمته من قاموس
# وعالج حالة المفتاح غير الموجود

print("=== Q8 ===")


def access_dictionary():
    student_grades = {"أحمد": 85, "فاطمة": 92, "محمد": 78, "سارة": 95}

    try:
        key = input("Enter student name: ")
        grade = student_grades[key]
        print(f"Grade of {key}: {grade}")
    except KeyError:
        print("Error: Name not found in records")
    except Exception as e:
        print(f"Unexpected error: {e}")


access_dictionary()
print()


# ----------------------------------------------------------
# Q9: استخدام else مع try-except
# ----------------------------------------------------------
# اكتب كود يستخدم كتلة else لتنفيذ تعليمات عند نجاح try

print("=== Q9 ===")


def access_dictionary():
    student_grades = {"أحمد": 85, "فاطمة": 92, "محمد": 78, "سارة": 95}

    try:
        key = input("Enter student name: ")
        grade = student_grades[key]
        print(f"Grade of {key}: {grade}")
    except KeyError:
        print("Error: Name not found in records")
    except Exception as e:
        print(f"Unexpected error: {e}")


access_dictionary()
print()


# ----------------------------------------------------------
# Q10: إنشاء برنامج آمن للبحث في قائمة
# ----------------------------------------------------------
# اكتب برنامجاً يبحث عن عنصر في قائمة باستخدام try-except
# بدلاً من التحقق الشرطي العادي

print("=== Q10 ===")


def safe_list_search():
    fruits = ["apple", "banana", "orange"]

    try:
        index = int(input("Enter element index: "))
        print(f"Element at index {index}: {fruits[index]}")
    except IndexError:
        print("Error: Index out of list range")
    except ValueError:
        print("Error: Please enter an integer only")


safe_list_search()
print()

# ----------------------------------------------------------
# Q12: برنامج متكامل لإدارة الأخطاء
# ----------------------------------------------------------
# اكتب برنامجاً يحسب متوسط درجات الطلاب مع معالجة جميع الأخطاء المحتملة

print("=== Q11 ===")


def calculate_average_grades():
    try:
        num_students = int(input("Enter number of students: "))
        if num_students <= 0:
            raise ValueError("Number of students must be positive")

        total = 0
        for i in range(num_students):
            try:
                grade = float(input(f"Enter grade for student {i+1}: "))
                if grade < 0 or grade > 100:
                    raise ValueError("Grade must be between 0 and 100")
                total += grade
            except ValueError as e:
                print(f"Error in grade input: {e}")
                return

        average = total / num_students
        print(f"Average grades: {average:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except ZeroDivisionError:
        print("Error: Cannot calculate average for zero students")
    except Exception as e:
        print(f"Unexpected error: {e}")


calculate_average_grades()
print()


# ----------------------------------------------------------
# Q13: استخدام التعليمة raise
# ----------------------------------------------------------
# اكتب دالة تتحقق من عمر المستخدم وتطلق استثناء إذا كان العمر غير منطقي

print("=== Q12 ===")


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 110:
        raise ValueError("Age is not logical")
    else:
        print(f"Age {age} is acceptable")


try:
    validate_age(25)
    validate_age(-5)  # This will cause an exception
except ValueError as e:
    print(f"Validation error: {e}")
print()




# ==========================================================
# نهاية اختبار الفصل الخامس
# ==========================================================
