# ==========================================================
# Comprehensive Test: Chapter 4 - Subprograms and Lambda
# ==========================================================


# ----------------------------------------------------------
# Q1: تعريف التوابع الأساسية
# ----------------------------------------------------------
# اكتب تابعاً اسمه calculate_area يحسب مساحة المستطيل
# ثم استدعِ التابع بطول 5 وعرض 3

print("=== Q1 ===")

def calculate_area(length, width):
    return length * width

result = calculate_area(5, 3)
print(f"Rectangle area: {result}")
print()


# ----------------------------------------------------------
# Q2: تمرير الوسطاء بالقيمة وبالمرجع
# ----------------------------------------------------------
# اكتب برنامجاً يوضح الفرق بين تمرير الوسيط بالقيمة والمرجع

print("=== Q2 ===")

def modify_value(x):
    x = 10
    print(f"Inside function - x = {x}")

def modify_list(lst):
    lst.append(4)
    lst[0] = 99

# Pass by value
num = 5
modify_value(num)
print(f"Outside function - num = {num}")

# Pass by reference
my_list = [1, 2, 3]
modify_list(my_list)
print(f"Outside function - my_list = {my_list}")
print()


# ----------------------------------------------------------
# Q3: التوابع الداخلية (Nested Functions)
# ----------------------------------------------------------
# اكتب تابعاً خارجياً يحتوي على تابع داخلي

print("=== Q3 ===")

def outer_function():
    x = 5
    
    def inner_function():
        y = 10
        print(f"Inside inner function: x = {x}, y = {y}")
    
    inner_function()
    print(f"Inside outer function: x = {x}")

outer_function()
print()


# ----------------------------------------------------------
# Q4: استخدام global و nonlocal
# ----------------------------------------------------------
# اكتب برنامجاً يوضح استخدام global و nonlocal

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
# استخدم lambda لإنشاء توابع للعمليات الحسابية الأساسية

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

print("=== Q6 ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Convert numbers to their squares
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")
print()


# ----------------------------------------------------------
# Q7: استخدام Lambda مع filter
# ----------------------------------------------------------
# استخدم filter و lambda لتصفية الأعداد الزوجية من قائمة

print("=== Q7 ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"All numbers: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print()


# ----------------------------------------------------------
# Q8: استخدام Lambda مع reduce
# ----------------------------------------------------------
# استخدم reduce و lambda لحساب مجموع الأعداد في قائمة

print("=== Q8 ===")
import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate sum
total_sum = functools.reduce(lambda x, y: x + y, numbers)

# Calculate product
total_product = functools.reduce(lambda x, y: x * y, numbers)

print(f"Numbers: {numbers}")
print(f"Total sum: {total_sum}")
print(f"Total product: {total_product}")
print()


# ----------------------------------------------------------
# Q9: تمرير التابع كوسيط
# ----------------------------------------------------------
# اكتب تابعاً يمكنه استقبال تابعات مختلفة كوسيط وتطبيقها على بيانات

print("=== Q9 ===")

def apply_operation(data, operation):
    """Apply operation to each element in data"""
    return [operation(x) for x in data]

numbers = [1, 2, 3, 4, 5]

# Define different operations using lambda
square = lambda x: x ** 2
cube = lambda x: x ** 3
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


# ----------------------------------------------------------
# Q10: نظام إدارة الطلاب (متقدم)
# ----------------------------------------------------------
# استخدم المفاهيم المتقدمة لإنشاء نظام إدارة طلاب

print("=== Q10 ===")

# Student data
students = [
    [12436, "Sami Ahmad", 56.3, 74.6],
    [12440, "Anas Mansour", 34.4, 80.9],
    [13822, "Moustafa Zein", 80, 13],
    [12541, "Ahmad Alos", 39.4, 80.5],
    [16621, "Zouhair Dahrouj", 55.2, 35]
]

def calculate_score(student):
    """Calculate score: 70% exam + 30% practical"""
    xam = student[2]
    pract = student[3]
    return xam * 0.70 + pract * 0.30

def is_successful(student):
    """Determine success"""
    xam = student[2]
    pract = student[3]
    score = calculate_score(student)
    
    return xam >= 40 and pract >= 40 and score >= 60

def process_students(students_list):
    """Process all students and add results"""
    processed_students = []
    
    for student in students_list:
        score = calculate_score(student)
        success = is_successful(student)
        # Add score and success result to student data
        processed_student = student + [round(score, 2), success]
        processed_students.append(processed_student)
    
    return processed_students

def get_successful_students(students_list):
    """Get only successful students"""
    return list(filter(lambda student: student[5], students_list))

def get_failed_students(students_list):
    """Get only failed students"""
    return list(filter(lambda student: not student[5], students_list))

def sort_by_score(students_list):
    """Sort students by score"""
    return sorted(students_list, key=lambda student: student[4], reverse=True)

# Process data
processed_students = process_students(students)

print("All students:")
for student in processed_students:
    status = "Pass" if student[5] else "Fail"
    print(f"{student[1]}: Score = {student[4]}, Status = {status}")

print("\nSuccessful students:")
successful = get_successful_students(processed_students)
for student in successful:
    print(f"{student[1]}: Score = {student[4]}")

print("\nStudents sorted by score:")
sorted_students = sort_by_score(processed_students)
for student in sorted_students:
    status = "Pass" if student[5] else "Fail"
    print(f"{student[1]}: Score = {student[4]}, Status = {status}")
print()


# ----------------------------------------------------------
# Q11: استخدام متقدم لـ map, filter, reduce
# ----------------------------------------------------------
# اكتب برنامجاً يحلل بيانات الطلاب باستخدام التوابع المتقدمة

print("=== Q11 ===")

def analyze_students(students_list):
    """Advanced analysis of student data"""
    
    # Average score using reduce
    total_score = functools.reduce(lambda x, y: x + y[4], students_list, 0)
    average_score = total_score / len(students_list)
    
    # Highest score
    highest_score = max(students_list, key=lambda student: student[4])
    
    # Lowest score
    lowest_score = min(students_list, key=lambda student: student[4])
    
    # Number of successful students
    successful_count = len(list(filter(lambda student: student[5], students_list)))
    
    # Success rate
    success_rate = (successful_count / len(students_list)) * 100
    
    print(f"Student Statistics:")
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {highest_score[4]} - {highest_score[1]}")
    print(f"Lowest score: {lowest_score[4]} - {lowest_score[1]}")
    print(f"Number of successful students: {successful_count}")
    print(f"Success rate: {success_rate:.1f}%")

analyze_students(processed_students)
print()


# ----------------------------------------------------------
# Q12: التوابع العودية (Recursive Functions)
# ----------------------------------------------------------
# اكتب تابعاً عودياً لحساب المضروب

print("=== Q12 ===")

def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test function
for i in range(1, 11):
    print(f"{i}! = {factorial(i)}")
print()


# ----------------------------------------------------------
# Q13: توليد التوابع ديناميكياً
# ----------------------------------------------------------
# اكتب برنامجاً يولد توابع بناءً على معطيات المدخل

print("=== Q13 ===")

def create_power_function(exponent):
    """Create function to raise numbers to a specific power"""
    return lambda x: x ** exponent

# Create different functions
square_func = create_power_function(2)
cube_func = create_power_function(3)
quad_func = create_power_function(4)

# Test generated functions
number = 5
print(f"{number}² = {square_func(number)}")
print(f"{number}³ = {cube_func(number)}")
print(f"{number}⁴ = {quad_func(number)}")
print()


# ----------------------------------------------------------
# Q14: معالجة الأخطاء في التوابع
# ----------------------------------------------------------
# اكتب توابع تتضمن معالجة الأخطاء

print("=== Q14 ===")

def safe_divide(x, y):
    """Safe division with error handling"""
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid data type"

def safe_convert_to_number(text):
    """Safe conversion of text to numbers"""
    try:
        return float(text)
    except ValueError:
        return "Error: Cannot convert text to number"

# Test error handling
print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Error: Cannot divide by zero
print(safe_divide(10, "a"))  # Error: Invalid data type

print(safe_convert_to_number("123.45"))  # 123.45
print(safe_convert_to_number("abc"))     # Error: Cannot convert text to number
print()


# ----------------------------------------------------------
# Q15: التوابع ككائنات من الدرجة الأولى
# ----------------------------------------------------------
# اكتب برنامجاً يوضح أن التوابع كائنات من الدرجة الأولى في بايثون

print("=== Q15 ===")

def greet(name):
    return f"Hello {name}!"

def farewell(name):
    return f"Goodbye {name}!"

def process_name(name, greeting_func):
    """Process name using greeting function"""
    return greeting_func(name)

# Store functions in list
greeting_functions = [greet, farewell]

# Pass functions as parameters
names = ["Ahmed", "Mohammed", "Fatima"]

for name in names:
    for func in greeting_functions:
        print(process_name(name, func))
    print("---")

print()


# ----------------------------------------------------------
# Q16: إغلاق (Closure) في التوابع
# ----------------------------------------------------------
# اكتب برنامجاً يوضح مفهوم الإغلاق في التوابع

print("=== Q16 ===")

def create_counter():
    """Create counter using closure"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

def create_multiplier(factor):
    """Create multiplier using closure"""
    def multiplier(x):
        return x * factor
    return multiplier

# Test counter
counter1 = create_counter()
counter2 = create_counter()

print("Counter 1:")
for i in range(3):
    print(counter1())

print("Counter 2:")
for i in range(2):
    print(counter2())

# Test multiplier
double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double of 5: {double(5)}")
print(f"Triple of 5: {triple(5)}")
print()


# ----------------------------------------------------------
# Q17: توليد السلاسل باستخدام التوابع
# ----------------------------------------------------------
# اكتب برنامجاً يولد سلاسل نصية بناءً على قواعد محددة

print("=== Q17 ===")

def create_greeting_template(language):
    """Create greeting template based on language"""
    templates = {
        'english': lambda name: f"Hello {name}!",
        'arabic': lambda name: f"مرحباً {name}!",
        'french': lambda name: f"Bonjour {name}!",
        'spanish': lambda name: f"¡Hola {name}!"
    }
    
    return templates.get(language.lower(), lambda name: f"Hello {name}!")

# Test greeting generation
names = ["Ahmed", "Maria", "Jean"]

languages = ['english', 'arabic', 'french', 'spanish']

for lang in languages:
    greeting_func = create_greeting_template(lang)
    print(f"{lang.capitalize()}:")
    for name in names:
        print(f"  {greeting_func(name)}")
    print()
print()


# ----------------------------------------------------------
# Q18: معالجة البيانات باستخدام سلسلة من التوابع
# ----------------------------------------------------------
# اكتب برنامجاً يعالج البيانات باستخدام سلسلة من عمليات map و filter

print("=== Q18 ===")

# Initial data
numbers = list(range(1, 21))

print(f"Original data: {numbers}")

# Chain of processing operations
processed_data = list(
    map(lambda x: x ** 2,                    # Square numbers
    filter(lambda x: x % 2 == 0,             # Filter even numbers
    filter(lambda x: x > 5, numbers)))       # Filter numbers greater than 5
)

print(f"Data after processing: {processed_data}")

# Analyze results
if processed_data:
    total = functools.reduce(lambda x, y: x + y, processed_data)
    average = total / len(processed_data)
    maximum = max(processed_data)
    minimum = min(processed_data)
    
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum value: {maximum}")
    print(f"Minimum value: {minimum}")
print()


# ----------------------------------------------------------
# Q19: نظام تصنيف متقدم للطلاب
# ----------------------------------------------------------
# اكتب نظام تصنيف متقدم باستخدام جميع المفاهيم المتعلمة

print("=== Q19 ===")

def create_student_grader(grade_ranges):
    """Create student grader based on score ranges"""
    def grader(score):
        for grade, (min_score, max_score) in grade_ranges.items():
            if min_score <= score <= max_score:
                return grade
        return "Not classified"
    return grader

# Define score ranges
grade_system = {
    "Excellent": (90, 100),
    "Very Good": (80, 89),
    "Good": (70, 79),
    "Acceptable": (60, 69),
    "Fail": (0, 59)
}

# Create grader
student_grader = create_student_grader(grade_system)

# Test system
test_scores = [45, 67, 78, 85, 92, 55, 100, 72, 88, 61]

print("Classification results:")
for score in test_scores:
    grade = student_grader(score)
    print(f"Score {score}: {grade}")
print()


# ----------------------------------------------------------
# Q20: تقرير شامل باستخدام جميع المفاهيم
# ----------------------------------------------------------
# اكتب برنامجاً يولد تقريراً شاملاً باستخدام جميع مفاهيم الفصل

print("=== Q20 ===")

def generate_comprehensive_report(students_data):
    """Generate comprehensive student report"""
    
    # Process data
    processed_students = process_students(students_data)
    
    # General statistics
    total_students = len(processed_students)
    successful_students = get_successful_students(processed_students)
    failed_students = get_failed_students(processed_students)
    
    success_rate = (len(successful_students) / total_students) * 100
    
    # Score analysis
    scores = list(map(lambda student: student[4], processed_students))
    average_score = functools.reduce(lambda x, y: x + y, scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    # Report
    print("=" * 50)
    print("Comprehensive Student Report")
    print("=" * 50)
    print(f"Total students: {total_students}")
    print(f"Successful students: {len(successful_students)}")
    print(f"Failed students: {len(failed_students)}")
    print(f"Success rate: {success_rate:.1f}%")
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {max_score}")
    print(f"Lowest score: {min_score}")
    print("\nOutstanding students (Score ≥ 80):")
    
    top_students = list(filter(lambda student: student[4] >= 80, processed_students))
    for student in top_students:
        print(f"  - {student[1]}: {student[4]}")
    
    print("\nStudents needing improvement (Score < 60):")
    struggling_students = list(filter(lambda student: student[4] < 60, processed_students))
    for student in struggling_students:
        print(f"  - {student[1]}: {student[4]}")
    
    print("=" * 50)

# Generate report
generate_comprehensive_report(students)
print()


# ==========================================================
# End of Chapter 4 Comprehensive Test
# ==========================================================