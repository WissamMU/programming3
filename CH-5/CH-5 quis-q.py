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

def safe_division():
    try:
        num1 = int(input("أدخل العدد الأول: "))
        num2 = int(input("أدخل العدد الثاني: "))
        result = num1 / num2
        print(f"نتيجة القسمة: {result}")
    except ZeroDivisionError:
        print("خطأ: لا يمكن القسمة على الصفر!")
    except ValueError:
        print("خطأ: أدخل أرقاماً صحيحة فقط!")

# اختبار الدالة
safe_division()
print()


# ----------------------------------------------------------
# Q2: معالجة أنواع متعددة من الاستثناءات
# ----------------------------------------------------------
# اكتب كود يحول مدخل المستخدم إلى عدد صحيح
# وعالج كلاً من ValueError و TypeError

print("=== Q2 ===")

def convert_to_int():
    try:
        user_input = input("أدخل عدداً صحيحاً: ")
        number = int(user_input)
        print(f"العدد المحول: {number}")
    except ValueError:
        print("خطأ: لا يمكن تحويل المدخل إلى عدد صحيح")
    except TypeError:
        print("خطأ: نوع البيانات غير مناسب")

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
        file = open(filename, 'r')
        content = file.read()
        print("محتويات الملف:")
        print(content)
    except FileNotFoundError:
        print(f"خطأ: الملف {filename} غير موجود")
    finally:
        if file:
            file.close()
            print("تم إغلاق الملف")

read_file_safely("example.txt")
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
        print(f"حدث خطأ في الفهرس: {e}")
        print(f"نوع الخطأ: {type(e).__name__}")

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
        index = int(input("أدخل فهرس العنصر (0-4): "))
        print(f"القيمة عند الفهرس {index}: {numbers[index]}")
    except IndexError:
        print("خطأ: الفهرس خارج نطاق القائمة")
    except ValueError:
        print("خطأ: أدخل رقماً صحيحاً فقط")

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
        a = int(input("أدخل العدد الأول: "))
        b = int(input("أدخل العدد الثاني: "))
        result = a ** b  # عملية الأس
        print(f"النتيجة: {a} ^ {b} = {result}")
    except ValueError:
        print("خطأ: أدخل أرقاماً صحيحة فقط")
    except ZeroDivisionError:
        print("خطأ: لا يمكن القسمة على الصفر")
    except OverflowError:
        print("خطأ: النتيجة كبيرة جداً")
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")

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
            user_input = input("أدخل عدداً عشرياً: ")
            number = float(user_input)
            return number
        except ValueError:
            print("خطأ: أدخل عدداً عشرياً صحيحاً. حاول مرة أخرى")

# اختبار الدالة
result = get_safe_float()
print(f"القيمة المدخلة: {result}")
print()


# ----------------------------------------------------------
# Q8: معالجة استثناءات القواميس
# ----------------------------------------------------------
# اكتب كود يطلب مفتاحاً من المستخدم ويعرض قيمته من قاموس
# وعالج حالة المفتاح غير الموجود

print("=== Q8 ===")

def access_dictionary():
    student_grades = {
        "أحمد": 85,
        "فاطمة": 92,
        "محمد": 78,
        "سارة": 95
    }
    
    try:
        key = input("أدخل اسم الطالب: ")
        grade = student_grades[key]
        print(f"درجة {key}: {grade}")
    except KeyError:
        print("خطأ: الاسم غير موجود في السجلات")
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")

access_dictionary()
print()


# ----------------------------------------------------------
# Q9: استخدام else مع try-except
# ----------------------------------------------------------
# اكتب كود يستخدم كتلة else لتنفيذ تعليمات عند نجاح try

print("=== Q9 ===")

def try_except_else():
    try:
        num = int(input("أدخل عدداً صحيحاً: "))
    except ValueError:
        print("خطأ: أدخل عدداً صحيحاً فقط")
    else:
        print(f"تم إدخال العدد بنجاح: {num}")
        print(f"مربع العدد: {num ** 2}")

try_except_else()
print()


# ----------------------------------------------------------
# Q10: إنشاء برنامج آمن للبحث في قائمة
# ----------------------------------------------------------
# اكتب برنامجاً يبحث عن عنصر في قائمة باستخدام try-except
# بدلاً من التحقق الشرطي العادي

print("=== Q10 ===")

def safe_list_search():
    fruits = ["تفاح", "موز", "برتقال", "فراولة"]
    
    try:
        index = int(input("أدخل فهرس العنصر: "))
        print(f"العنصر عند الفهرس {index}: {fruits[index]}")
    except IndexError:
        print("خطأ: الفهرس خارج نطاق القائمة")
    except ValueError:
        print("خطأ: أدخل رقماً صحيحاً فقط")

safe_list_search()
print()


# ----------------------------------------------------------
# Q11: معالجة استثناءات التحويل بين الأنواع
# ----------------------------------------------------------
# اكتب كود يحول قائمة من السلاسل إلى أعداد ويعالج الأخطاء

print("=== Q11 ===")

def convert_strings_to_numbers():
    string_list = ["10", "20", "ثلاثون", "40", "50.5"]
    numbers = []
    
    for item in string_list:
        try:
            number = float(item)
            numbers.append(number)
        except ValueError:
            print(f"لا يمكن تحويل '{item}' إلى عدد")
    
    print(f"الأعداد المحولة: {numbers}")

convert_strings_to_numbers()
print()


# ----------------------------------------------------------
# Q12: برنامج متكامل لإدارة الأخطاء
# ----------------------------------------------------------
# اكتب برنامجاً يحسب متوسط درجات الطلاب مع معالجة جميع الأخطاء المحتملة

print("=== Q12 ===")

def calculate_average_grades():
    try:
        num_students = int(input("أدخل عدد الطلاب: "))
        if num_students <= 0:
            raise ValueError("عدد الطلاب يجب أن يكون موجباً")
        
        total = 0
        for i in range(num_students):
            try:
                grade = float(input(f"أدخل درجة الطالب {i+1}: "))
                if grade < 0 or grade > 100:
                    raise ValueError("الدرجة يجب أن تكون بين 0 و 100")
                total += grade
            except ValueError as e:
                print(f"خطأ في إدخال الدرجة: {e}")
                return
        
        average = total / num_students
        print(f"متوسط الدرجات: {average:.2f}")
        
    except ValueError as e:
        print(f"خطأ في الإدخال: {e}")
    except ZeroDivisionError:
        print("خطأ: لا يمكن حساب المتوسط لعدد طلاب صفري")
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")

calculate_average_grades()
print()


# ----------------------------------------------------------
# Q13: استخدام التعليمة raise
# ----------------------------------------------------------
# اكتب دالة تتحقق من عمر المستخدم وتطلق استثناء إذا كان العمر غير منطقي

print("=== Q13 ===")

def validate_age(age):
    if age < 0:
        raise ValueError("العمر لا يمكن أن يكون سالباً")
    elif age > 150:
        raise ValueError("العمر غير منطقي")
    else:
        print(f"العمر {age} مقبول")

try:
    validate_age(25)
    validate_age(-5)  # سيتسبب في استثناء
except ValueError as e:
    print(f"خطأ في التحقق: {e}")
print()


# ----------------------------------------------------------
# Q14: إنشاء معالج استثناءات مخصص
# ----------------------------------------------------------
# اكتب دالة تعالج الاستثناءات بناءً على نوعها وتقدم رسائل مساعدة

print("=== Q14 ===")

def custom_exception_handler(operation_func):
    try:
        return operation_func()
    except ZeroDivisionError:
        return "خطأ: حاولت القسمة على الصفر - تأكد من أن المقام ليس صفراً"
    except ValueError:
        return "خطأ: قيمة غير صالحة - تأكد من إدخال أرقام فقط"
    except IndexError:
        return "خطأ: فهرس خارج النطاق - تحقق من حجم القائمة"
    except Exception as e:
        return f"خطأ غير متوقع: {e}"

# اختبار المعالج المخصص
def test_operation():
    numbers = [1, 2, 3]
    return numbers[5]  # سيتسبب في IndexError

result = custom_exception_handler(test_operation)
print(result)
print()


# ----------------------------------------------------------
# Q15: سجل الأخطاء في ملف
# ----------------------------------------------------------
# اكتب برنامجاً يسجل جميع الأخطاء في ملف log بدلاً من عرضها للمستخدم

print("=== Q15 ===")

def log_errors_to_file():
    try:
        # عملية قد تسبب أخطاء
        num = int("غير رقم")
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8") as log_file:
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] خطأ: {e}\n")
        print("تم تسجيل الخطأ في الملف")

log_errors_to_file()
print("تم الانتهاء من تسجيل الأخطاء")
print()


# ==========================================================
# نهاية اختبار الفصل الخامس
# ==========================================================