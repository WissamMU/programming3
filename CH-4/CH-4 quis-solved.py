# ==========================================================
# Comprehensive Test: Chapter 4 - Subprograms and Lambda
# ==========================================================


# ----------------------------------------------------------
# Q1: تعريف التوابع الأساسية
# ----------------------------------------------------------
# اكتب تابعاً اسمه calculate_area يحسب مساحة المستطيل
# المدخلات: length (الطول), width (العرض)
# المخرجات: مساحة المستطيل (الطول × العرض)
# ثم استدعِ التابع بطول 5 وعرض 3 واطبع النتيجة

print("=== Q1 ===")


def calculate_area(length, width):
    return length * width


result = calculate_area(5, 3)
print(f"Rectangle area: {result}")
print()


# ----------------------------------------------------------
# Q2: تمرير الوسطاء بالقيمة وبالمرجع
# ----------------------------------------------------------
# اكتب برنامجاً يوضح الفرق بين تمرير متغير عادي (بالقيمة)
# وتمرير قائمة (بالمرجع) إلى التوابع

print("=== Q2 ===")


def modify_value(x):
    """توضح تمرير الوسيط بالقيمة - التغيير لا يؤثر على المتغير الأصلي"""
    x = 10
    print(f"Inside function - x = {x}")


def modify_list(lst):
    """توضح تمرير الوسيط بالمرجع - التغيير يؤثر على القائمة الأصلية"""
    lst.append(4)
    lst[0] = 99
    print(f"Inside function - my_list = {my_list}")


# اختبار تمرير المتغير العادي (بالقيمة)
num = 5
print(f"Before function call - num = {num}")
modify_value(num)
print(f"After function call - num = {num}")

# اختبار تمرير القائمة (بالمرجع)
my_list = [1, 2, 3]
print(f"Before function call - my_list = {my_list}")
modify_list(my_list)
print(f"After function call - my_list = {my_list}")
print()


# ----------------------------------------------------------
# Q3: التوابع الداخلية (Nested Functions)
# ----------------------------------------------------------
# اكتب تابعاً خارجياً اسمه outer_function يحتوي على تابع داخلي
# اسمه inner_function بحيث:
# - التابع الخارجي يعلن متغير x = 5
# - التابع الداخلي يعلن متغير x = 10
# - اطبع قيمة x من داخل التابع الداخلي ثم من التابع الخارجي

print("=== Q3 ===")


def outer_function():
    x = 5
    print(f"original value x = {x}")

    def inner_function():
        x = 10
        print(f"Inside inner function: x = {x}")

    inner_function()
    print(f"Inside outer function: x = {x}")


outer_function()
print()


# ----------------------------------------------------------
# Q4: استخدام global و nonlocal
# ----------------------------------------------------------
# اكتب برنامجاً يوضح الفرق بين global و nonlocal:
# - عرف متغير عالمي x = 1
# - اكتب تابع test_global يستخدم global لتعديل المتغير العالمي
# - اكتب تابع outer يحتوي على تابع inner يستخدم nonlocal

print("=== Q4 ===")

x = 1  # Global variable


def test_global():
    global x
    x = 10
    print(f"Inside test_global: x = {x}")


def outer():
    x = 5

    def inner():
        nonlocal x
        x = 15
        print(f"Inside inner: x = {x}")

    print(f"Before inner: x = {x}")
    inner()
    print(f"After inner: x = {x}")


print(f"Before test_global: x = {x}")
test_global()
print(f"After test_global: x = {x}")

outer()
print(f"Finally: x = {x}")
print()


# ----------------------------------------------------------
# Q5: التابع Lambda الأساسي
# ----------------------------------------------------------
# استخدم lambda لإنشاء توابع للعمليات الحسابية الأساسية:
# - جمع عددين
# - طرح عددين
# - ضرب عددين
# - قسمة عددين (مع معالجة القسمة على صفر)

print("=== Q5 ===")

# Define functions using lambda
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero"

# Test functions
a, b = 10, 3
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} × {b} = {multiply(a, b)}")
print(f"{a} ÷ {b} = {divide(a, b)}")
print()


# ----------------------------------------------------------
# Q6: استخدام Lambda مع map
# ----------------------------------------------------------
# استخدم map و lambda لتحويل قائمة الأعداد إلى مربعاتها
# القائمة: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# النتيجة المطلوبة: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("=== Q6 ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Convert numbers to their squares using map and lambda
squared_numbers = list(map(lambda x: x**2, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")
print()


# ----------------------------------------------------------
# Q7: استخدام Lambda مع filter
# ----------------------------------------------------------
# استخدم filter و lambda لتصفية:
# - الأعداد الزوجية من القائمة
# - الأعداد الفردية من القائمة
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("=== Q7 ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Filter even numbers (الأعداد الزوجية)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Filter odd numbers (الأعداد الفردية)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"All numbers: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print()


# ----------------------------------------------------------
# Q8: استخدام Lambda مع reduce
# ----------------------------------------------------------
# استخدم reduce و lambda لحساب مجموع الأعداد في قائمة
# القائمة: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# استخدم المكتبة: import functools
# functools.reduce
print("=== Q8 ===")
import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate sum using reduce and lambda
total_sum = functools.reduce(lambda x, y: x + y, numbers)

print(f"Numbers: {numbers}")
print(f"Total sum: {total_sum}")
print()


# ----------------------------------------------------------
# Q9: تمرير التابع كوسيط
# ----------------------------------------------------------
# اكتب تابعاً اسمه apply_operation يمكنه استقبال تابعات مختلفة كوسيط
# وتطبيقها على كل عنصر في قائمة البيانات
# القائمة: [1, 2, 3, 4, 5]
# العمليات المطلوبة:
# - square: رفع العدد للأس 2
# - cube: رفع العدد للأس 3
# - double: ضرب العدد في 2

print("=== Q9 ===")


def apply_operation(data, operation):
    """Apply operation to each element in data"""
    return [operation(x) for x in data]


numbers = [1, 2, 3, 4, 5]

# Define different operations using lambda
square = lambda x: x**2
cube = lambda x: x**3
double = lambda x: x * 2

# Apply different operations
squared = apply_operation(numbers, square)
cubed = apply_operation(numbers, cube)
doubled = apply_operation(numbers, double)

print(f"Numbers: {numbers}")
print(f"Squared: {squared}")
print(f"Cubed: {cubed}")
print(f"Doubled: {doubled}")
print()



# ==========================================================
# End of Chapter 4 Comprehensive Test
# ==========================================================
