# ==========================================================
# Comprehensive Test: Chapter 7 - Object Oriented Programming in Python
# ==========================================================


# ----------------------------------------------------------
# Q1: تعريف الصف الأساسي (Basic Class Definition)
# ----------------------------------------------------------
# قم بإنشاء صف اسمه Student يحتوي على:
# 1. الباني (__init__) الذي يقوم بتهيئة:
#    - name (اسم)
#    - age (عمر)
#    - major (تخصص)
# 2. الطريقة display_info() التي تطبع معلومات الطالب

print("=== Q1 ===")

class Student:
    def __init__(self , name , age , major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(f'Welcome back\nname : {self.name} \nage : {self.age}\nmajor : {self.major}')
s1 = Student('bob' , 22 , 'ITE')
s1.display_info()

print()


# ----------------------------------------------------------
# Q2: الطرق الساكنة والطرق العادية (Static vs Instance Methods)
# ----------------------------------------------------------
# قم بتعديل صف Student ليشمل:
# 1. طريقة عادية (instance method) تزيد العمر بمقدار 1
# 2. طريقة ساكنة (static method) تطبع جملة ترحيب عامة

print("=== Q2 ===")

class Student:
    def __init__(self , count):
        self.count = count
        
    def Older(self):
        self.count += 1
        return self.count

    @staticmethod
    def Hello():
        print('hello')

s1 = Student(5)
print(s1.Older())
s1.Hello()

print()


# ----------------------------------------------------------
# Q3: زيادة تحميل العمليات (Operator Overloading)
# ----------------------------------------------------------
# قم بإنشاء صف Vector يمثل متجه ثنائي الأبعاد (x, y) وقم بتحميل:
# 1. عملية الجمع (+) بين متجهين
# 2. عملية التمثيل النصي (__str__)

print("=== Q3 ===")

class Vector():
    def __init__(self , x , y ):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f'Vectors({self.x} , {self.y})'

v1 = Vector(5,3)
v2 = Vector(2,5)
print(v1 + v2)
print(v1)


print()


# ----------------------------------------------------------
# Q4: الوراثة البسيطة (Simple Inheritance)
# ----------------------------------------------------------
# قم بإنشاء صف Person ثم صف Employee الذي يرث من Person
# Person يحتوي على: name, age
# Employee يضيف: employee_id, salary

print("=== Q4 ===")

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
    def display_person_info(self):
        print(f"Person: {self.name}, {self.age} years old")
        
        
class Employee(Person):
    def __init__(self , name , age , employee_id , salary):
        super().__init__(name , age)
        self.employee_id = employee_id
        self.salary = salary
        
    def display_employee_info(self):
        self.display_person_info()
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")

emp = Employee("Mohammed", 30, "E101", 50000)
emp.display_employee_info()


print()


# ----------------------------------------------------------
# Q5: إعادة تعريف الطرق (Method Overriding)
# ----------------------------------------------------------
# قم بإنشاء صف Animal وصف Dog الذي يرث من Animal
# 1. Animal لديه طريقة make_sound() تطبع "Some sound"
# 2. Dog يعيد تعريف make_sound() ليطبع "Woof!"

print("=== Q5 ===")

class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# اختبار الصفوف
animal = Animal()
dog = Dog()

print("Animal sound: ", end="")
animal.make_sound()
print("Dog sound: ", end="")
dog.make_sound()

print()


# ----------------------------------------------------------
# Q6: محددات الوصول (Access Modifiers)
# ----------------------------------------------------------
# قم بإنشاء صف BankAccount مع:
# 1. خاصية عامة: account_number
# 2. خاصية خاصة (بخط سفلي مزدوج): __balance
# 3. طرق للوصول المحمي: deposit(), withdraw(), get_balance()

print("=== Q6 ===")

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance
    
    
print()


# ----------------------------------------------------------
# Q7: الوراثة المتعددة (Multiple Inheritance)
# ----------------------------------------------------------
# قم بإنشاء صفين: Swimmer و Flyer ثم صف Duck الذي يرث منهما معاً

print("=== Q7 ===")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Flyer:
    def fly(self):
        print("I can fly!")

class Duck(Swimmer, Flyer):
    def quack(self):
        print("Quack! Quack!")

# اختبار الصف
duck = Duck()
duck.swim()
duck.fly()
duck.quack()

print()


# ----------------------------------------------------------
# Q8: مثال الصف Complex كما في المقرر
# ----------------------------------------------------------
# قم بإعادة كتابة صف Complex الذي يمثل الأعداد العقدية مع:
# 1. الباني
# 2. طريقة الجمع
# 3. زيادة تحميل عملية الجمع (+)
# 4. التمثيل النصي

print("=== Q8 ===")

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    
    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        return f"({self.real}, {self.imag})"

# اختبار الصف
c1 = Complex(3, 4)
c2 = Complex(1, 2)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c1.add(c2) = {c1.add(c2)}")
print(f"c1 + c2 = {c1 + c2}")

print()


# ----------------------------------------------------------
# Q9: استخدام super() في الوراثة
# ----------------------------------------------------------
# قم بإنشاء هرمية وراثة: Vehicle → Car → ElectricCar
# واستخدم super() لاستدعاء باني الصف الأب

print("=== Q9 ===")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}")

class ElectricCar(Car):
    def __init__(self, brand, model, num_doors, battery_capacity):
        super().__init__(brand, model, num_doors)
        self.battery_capacity = battery_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Battery: {self.battery_capacity} kWh")

# اختبار الصفوف
ev = ElectricCar("Tesla", "Model S", 4, 100)
ev.display_info()

print()


# ----------------------------------------------------------
# Q10: التوابع الجاهزة للصفوف
# ----------------------------------------------------------
# قم بإنشاء صف Book واستخدم التوابع الجاهزة التالية:
# 1. __init__ للباني
# 2. __str__ للتمثيل النصي
# 3. __del__ للباني العكسي
# 4. __eq__ للمقارنة بين كتابين (بناءً على ISBN)

print("=== Q10 ===")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        print(f"Book '{title}' created")
    
    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"
    
    def __del__(self):
        print(f"Book '{self.title}' is being deleted")
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

# اختبار الصف
book1 = Book("Python Programming", "John Doe", "12345")
book2 = Book("OOP in Python", "Jane Smith", "12345")
book3 = Book("Another Book", "Someone", "67890")

print(book1)
print(book2)
print(book3)

print(f"book1 == book2: {book1 == book2}")  # True (نفس ISBN)
print(f"book1 == book3: {book1 == book3}")  # False

# حذف الكتب
del book1
del book2
del book3

print()


# ----------------------------------------------------------
# Q11: تطبيق عملي - نظام إدارة الطلاب باستخدام OOP
# ----------------------------------------------------------
# قم بإنشاء نظام متكامل لإدارة الطلاب باستخدام مفاهيم OOP

print("=== Q11 ===")

class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
    
    def __str__(self):
        return f"{self.course_code}: {self.course_name} ({self.credits} credits)"

class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.courses = []
        self.grades = {}
    
    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}")
    
    def assign_grade(self, course, grade):
        if course in self.courses:
            self.grades[course.course_code] = grade
            print(f"Grade {grade} assigned for {course.course_name}")
        else:
            print(f"Student not enrolled in {course.course_name}")
    
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        
        total_points = 0
        total_credits = 0
        
        for course_code, grade in self.grades.items():
            # تحويل الدرجة إلى نقاط
            grade_points = self._grade_to_points(grade)
            
            # البحث عن المادة للحصول على عدد الساعات
            for course in self.courses:
                if course.course_code == course_code:
                    total_points += grade_points * course.credits
                    total_credits += course.credits
                    break
        
        return total_points / total_credits if total_credits > 0 else 0.0
    
    def _grade_to_points(self, grade):
        # دالة خاصة لتحويل الدرجة إلى نقاط
        grade_map = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        return grade_map.get(grade.upper(), 0.0)
    
    def display_transcript(self):
        print(f"\nTranscript for {self.name} ({self.student_id})")
        print(f"Major: {self.major}")
        print("-" * 40)
        
        for course in self.courses:
            grade = self.grades.get(course.course_code, "No Grade")
            print(f"{course.course_code}: {course.course_name} - Grade: {grade}")
        
        print(f"GPA: {self.calculate_gpa():.2f}")

# إنشاء مواد دراسية
math101 = Course("MATH101", "Calculus I", 3)
cs101 = Course("CS101", "Introduction to Programming", 4)
eng101 = Course("ENG101", "English Composition", 3)

# إنشاء طالب
student1 = Student("S123", "Ahmed", "Computer Science")

# تسجيل الطالب في المواد
student1.enroll_course(math101)
student1.enroll_course(cs101)
student1.enroll_course(eng101)

# إعطاء الدرجات
student1.assign_grade(math101, 'A')
student1.assign_grade(cs101, 'B')
student1.assign_grade(eng101, 'A')

# عرض السجل الأكاديمي
student1.display_transcript()

print()


# ----------------------------------------------------------
# Q12: الكلمات المفتاحية والتوابع الجاهزة في OOP
# ----------------------------------------------------------
# قم بتجربة واستخدام الكلمات المفتاحية والتوابع الجاهزة المتعلقة بالـ OOP

print("=== Q12 ===")

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# اختبار isinstance و issubclass
parent_obj = Parent("Parent")
child_obj = Child("Child", 10)

print(f"isinstance(child_obj, Child): {isinstance(child_obj, Child)}")
print(f"isinstance(child_obj, Parent): {isinstance(child_obj, Parent)}")
print(f"issubclass(Child, Parent): {issubclass(Child, Parent)}")
print(f"issubclass(Parent, Child): {issubclass(Parent, Child)}")

# استخدام التوابع الجاهزة
print(f"\nType of child_obj: {type(child_obj)}")
print(f"ID of child_obj: {id(child_obj)}")

# استخدام hasattr و getattr
print(f"\nchild_obj has attribute 'name': {hasattr(child_obj, 'name')}")
print(f"child_obj has attribute 'salary': {hasattr(child_obj, 'salary')}")
print(f"Value of 'name' attribute: {getattr(child_obj, 'name', 'Not Found')}")
print(f"Value of 'salary' attribute: {getattr(child_obj, 'salary', 'Not Found')}")

# إضافة خاصية جديدة باستخدام setattr
setattr(child_obj, 'grade', 'Fifth')
print(f"\nAfter setattr - child_obj.grade: {child_obj.grade}")

# ==========================================================
# End of Chapter 7 Comprehensive Test
# ==========================================================
