# ملخص مفصل وشامل للفصل السابع: البرمجة غرضية التوجه (OOP) في بايثون

## 📚 **التمهيد والنظرة العامة**

### **ماهية البرمجة غرضية التوجه (OOP)**
البرمجة غرضية التوجه هي **نموذج برمجي** يعتمد على مفهوم **"الكائنات" (Objects)** التي تجمع بين **البيانات (Data)** و **السلوكيات (Behaviors)** في كيان واحد. هذا النموذج يتناقض مع البرمجة الإجرائية التقليدية حيث تكون البيانات والوظائف منفصلة.

### **لماذا OOP مهمة؟**
- **إعادة الاستخدام (Reusability)**: يمكن استخدام الكود في مشاريع متعددة
- **التنظيم (Organization)**: تنظيم الكود في وحدات منطقية
- **الصيانة (Maintenance)**: سهولة إيجاد وتصحيح الأخطاء
- **التجريد (Abstraction)**: إخفاء التفاصيل المعقدة عن المستخدم
- **المرونة (Flexibility)**: سهولة التعديل والتوسيع

## 🏗️ **الهيكل الأساسي للصفوف في بايثون**

### **1. تعريف الصف (Class Definition)**
```python
class ClassName:
    """توثيق الصف (اختياري)"""
    
    # متغيرات الصف (Class Variables)
    class_variable = "قيمة مشتركة"
    
    # المنشئ (Constructor)
    def __init__(self, parameter1, parameter2):
        """تهيئة الكائن"""
        self.instance_variable1 = parameter1  # متغير مثيل
        self.instance_variable2 = parameter2
    
    # الطرق (Methods)
    def instance_method(self):
        """طريقة المثيل"""
        return f"القيمة: {self.instance_variable1}"
    
    @staticmethod
    def static_method():
        """طريقة ثابتة"""
        return "أنا طريقة ثابتة"
    
    @classmethod
    def class_method(cls):
        """طريقة الصف"""
        return f"متغير الصف: {cls.class_variable}"
```

### **2. شرح المكونات الأساسية**

#### **أ. المنشئ (Constructor) - `__init__`**
- **الوظيفة**: تهيئة الكائن عند إنشائه
- **التنفيذ**: يُستدعى تلقائياً عند إنشاء كائن جديد
- **المعاملات**: أول معامل دائمًا هو `self`
- **الاستخدام**: لتعيين القيم الأولية لمتغيرات المثيل

```python
class Student:
    def __init__(self, name, student_id, gpa=0.0):
        """
        تهيئة كائن الطالب
        
        Args:
            name (str): اسم الطالب
            student_id (int): رقم الطالب الجامعي
            gpa (float): المعدل التراكمي (اختياري، افتراضي 0.0)
        """
        self.name = name
        self.id = student_id
        self.gpa = gpa
        self.courses = []  # قائمة فارغة للمقررات
```

#### **ب. الكلمة المفتاحية `self`**
- **المعنى**: تشير إلى **الكائن الحالي**
- **الضرورة**: مطلوبة في جميع طرق المثيل
- **الاستخدام**: للوصول إلى متغيرات وطرق الكائن

```python
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        """إيداع مبلغ في الحساب"""
        if amount > 0:
            self.balance += amount
            print(f"تم إيداع {amount}. الرصيد الحالي: {self.balance}")
        return self.balance  # إرجاع self.balance للكائن الحالي
```

## 🔄 **أنواع الطرق (Methods) في الصفوف**

### **1. طرق المثيل (Instance Methods)**
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """حساب مساحة المستطيل"""
        return self.length * self.width
    
    def perimeter(self):
        """حساب محيط المستطيل"""
        return 2 * (self.length + self.width)
    
    def is_square(self):
        """التحقق إذا كان المستطيل مربعًا"""
        return self.length == self.width
```

### **2. الطرق الثابتة (Static Methods)**
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        """جمع رقمين"""
        return a + b
    
    @staticmethod
    def factorial(n):
        """حساب مضروب عدد"""
        if n < 0:
            return None
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    @staticmethod
    def is_prime(n):
        """التحقق إذا كان عدد أولي"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
```

### **3. طرق الصف (Class Methods)**
```python
class Car:
    total_cars = 0  # متغير صف
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1
    
    @classmethod
    def get_total_cars(cls):
        """الحصول على عدد السيارات المصنوعة"""
        return cls.total_cars
    
    @classmethod
    def from_string(cls, car_string):
        """إنشاء كائن سيارة من سلسلة نصية"""
        brand, model = car_string.split('-')
        return cls(brand, model)
```

## 🎭 **محددات الوصول (Access Modifiers)**

### **المستويات الثلاثة للوصول**
```python
class Employee:
    def __init__(self, name, salary, department):
        self.name = name            # public - عام
        self._department = department  # protected - محمي
        self.__salary = salary      # private - خاص
    
    def get_salary(self):
        """getter للراتب الخاص"""
        return self.__salary
    
    def set_salary(self, new_salary):
        """setter للراتب الخاص"""
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("الراتب يجب أن يكون موجبًا")
    
    def _internal_method(self):
        """طريقة محمية للاستخدام الداخلي"""
        return f"القسم: {self._department}"
    
    def __private_calculation(self):
        """طريقة خاصة للحسابات الداخلية"""
        return self.__salary * 1.1  # زيادة 10%

# الاستخدام
emp = Employee("أحمد", 5000, "التطوير")
print(emp.name)          # ✅ متاح: أحمد
print(emp._department)   # ⚠️ متاح لكنه غير مستحسن
# print(emp.__salary)    # ❌ خطأ: غير متاح مباشرة
print(emp.get_salary())  # ✅ الطريقة الصحيحة: 5000
```

### **التفاصيل التقنية للخصوصية**
```python
class Secret:
    def __init__(self):
        self.public = "أنا عام"
        self._protected = "أنا محمي"
        self.__private = "أنا خاص"
        self.__very_private__ = "خاص جداً"
    
    def reveal_secrets(self):
        """كشف الأسرار من داخل الصف"""
        print(f"العام: {self.public}")
        print(f"المحمي: {self._protected}")
        print(f"الخاص: {self.__private}")

# حقيقة الخصوصية في بايثون
secret = Secret()
print(secret._Secret__private)  # ✅ الوصول بطريقة غير مباشرة
# بايثون تقوم بتسمية خاصة: _ClassName__variable
```

## 🔗 **الوراثة (Inheritance)**

### **1. الوراثة البسيطة**
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        return f"{self.name} يأكل"
    
    def sleep(self):
        return f"{self.name} ينام"
    
    def make_sound(self):
        return "صوت الحيوان"

class Dog(Animal):  # Dog يرث من Animal
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # استدعاء منشئ الأب
        self.breed = breed
    
    def make_sound(self):  # إعادة تعريف (override)
        return "هاو هاو!"
    
    def fetch(self):  # طريقة جديدة خاصة بالكلب
        return f"{self.name} يجلب العصا"

class Cat(Animal):  # Cat يرث من Animal
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):  # إعادة تعريف (override)
        return "مواء!"
    
    def climb(self):  # طريقة جديدة خاصة بالقط
        return f"{self.name} يتسلق الشجرة"
```

### **2. الوراثة المتعددة (Multiple Inheritance)**
```python
class Flyable:
    def __init__(self, max_altitude):
        self.max_altitude = max_altitude
    
    def fly(self):
        return "يطير في السماء"
    
    def land(self):
        return "يهبط على الأرض"

class Swimmable:
    def __init__(self, max_depth):
        self.max_depth = max_depth
    
    def swim(self):
        return "يسبح في الماء"
    
    def dive(self):
        return "يغوص تحت الماء"

class Duck(Flyable, Swimmable):  # يرث من صفين
    def __init__(self, name, max_altitude, max_depth):
        Flyable.__init__(self, max_altitude)
        Swimmable.__init__(self, max_depth)
        self.name = name
    
    def quack(self):
        return "كواك كواك!"

# إنشاء وإستخدام
donald = Duck("دونالد", 100, 10)
print(donald.fly())    # من Flyable
print(donald.swim())   # من Swimmable
print(donald.quack())  # من Duck نفسها
```

### **3. الوراثة متعددة المستويات**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"أنا {self.name}, عمري {self.age} سنة"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
        return f"تم تسجيل {self.name} في مقرر {course}"

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic
        self.publications = []
    
    def publish_paper(self, paper_title):
        self.publications.append(paper_title)
        return f"نشر {self.name} ورقة بحثية: {paper_title}"
```

## ✨ **التوابع الجاهزة (Magic/Dunder Methods)**

### **1. التوابع الحسابية**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # العمليات الأساسية
    def __add__(self, other):
        """الجمع: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """الطرح: v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """الضرب: v * scalar"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("يجب أن يكون المضروب رقمًا")
    
    def __truediv__(self, scalar):
        """القسمة: v / scalar"""
        if scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        raise ZeroDivisionError("القسمة على صفر غير مسموحة")
    
    # العمليات العكسية
    def __radd__(self, other):
        """الجمع العكسي: scalar + v"""
        return self.__add__(other)
    
    def __rmul__(self, scalar):
        """الضرب العكسي: scalar * v"""
        return self.__mul__(scalar)
```

### **2. التوابع المقارنة**
```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def simplify(self):
        """تبسيط الكسر"""
        from math import gcd
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
    
    def __eq__(self, other):
        """المساواة: f1 == f2"""
        return (self.numerator == other.numerator and 
                self.denominator == other.denominator)
    
    def __lt__(self, other):
        """أقل من: f1 < f2"""
        return (self.numerator * other.denominator < 
                other.numerator * self.denominator)
    
    def __le__(self, other):
        """أقل من أو يساوي: f1 <= f2"""
        return (self.numerator * other.denominator <= 
                other.numerator * self.denominator)
    
    def __gt__(self, other):
        """أكبر من: f1 > f2"""
        return not self.__le__(other)
    
    def __ge__(self, other):
        """أكبر من أو يساوي: f1 >= f2"""
        return not self.__lt__(other)
```

### **3. التوابع النصية والتمثيلية**
```python
class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    
    def __str__(self):
        """تمثيل نصي للمستخدم"""
        return f'"{self.title}" من تأليف {self.author} ({self.year})'
    
    def __repr__(self):
        """تمثيل رسمي للمبرمجين"""
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.pages})"
    
    def __len__(self):
        """طول الكتاب (عدد الصفحات)"""
        return self.pages
    
    def __contains__(self, word):
        """التحقق إذا كانت الكلمة في العنوان"""
        return word.lower() in self.title.lower()
```

### **4. التوابع الخاصة بالمجموعات**
```python
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, quantity=1):
        """إضافة عنصر إلى السلة"""
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
    
    def remove_item(self, item, quantity=1):
        """إزالة عنصر من السلة"""
        if item in self.items:
            if self.items[item] <= quantity:
                del self.items[item]
            else:
                self.items[item] -= quantity
    
    def __len__(self):
        """عدد العناصر المختلفة في السلة"""
        return len(self.items)
    
    def __contains__(self, item):
        """التحقق إذا كان العنصر في السلة"""
        return item in self.items
    
    def __iter__(self):
        """التكرار على عناصر السلة"""
        return iter(self.items.items())
    
    def __getitem__(self, item):
        """الحصول على كمية عنصر"""
        return self.items.get(item, 0)
    
    def __setitem__(self, item, quantity):
        """تعيين كمية لعنصر"""
        if quantity <= 0:
            if item in self.items:
                del self.items[item]
        else:
            self.items[item] = quantity
```

## 🎯 **المثال الشامل من الكتاب: Time Class**

### **التنفيذ الكامل**
```python
class Time:
    """
    فئة الوقت لتمثيل وتعامل مع الوقت في صيغ مختلفة
    """
    
    def __init__(self, hour=0, minute=0, second=0):
        """
        تهيئة كائن الوقت
        
        Args:
            hour (int): الساعة (0-23)
            minute (int): الدقيقة (0-59)
            second (int): الثانية (0-59)
        """
        self.set_time(hour, minute, second)
    
    def set_time(self, hour=0, minute=0, second=0):
        """
        تعيين وقت جديد مع التحقق من الصحة
        
        Args:
            hour (int): الساعة (0-23)
            minute (int): الدقيقة (0-59)
            second (int): الثانية (0-59)
        """
        # التحقق من صحة المدخلات وتعيين القيم الافتراضية
        self.hour = hour if 0 <= hour < 24 else 0
        self.minute = minute if 0 <= minute < 60 else 0
        self.second = second if 0 <= second < 60 else 0
    
    def to_universal_string(self):
        """
        تحويل الوقت إلى صيغة عالمية (24 ساعة)
        
        Returns:
            str: الوقت بصيغة HH:MM:SS
        """
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    def to_standard_string(self):
        """
        تحويل الوقت إلى صيغة قياسية (12 ساعة مع AM/PM)
        
        Returns:
            str: الوقت بصيغة HH:MM:SS AM/PM
        """
        # تحديد AM أو PM
        period = "AM" if self.hour < 12 else "PM"
        
        # تحويل الساعة إلى صيغة 12 ساعة
        if self.hour == 0 or self.hour == 12:
            display_hour = 12
        else:
            display_hour = self.hour % 12
        
        return f"{display_hour:02d}:{self.minute:02d}:{self.second:02d} {period}"
    
    def add_seconds(self, seconds):
        """
        إضافة ثواني إلى الوقت
        
        Args:
            seconds (int): عدد الثواني للإضافة
            
        Returns:
            Time: الوقت الجديد بعد الإضافة
        """
        # تحويل الوقت الحالي إلى ثواني
        total_seconds = (self.hour * 3600 + 
                        self.minute * 60 + 
                        self.second + 
                        seconds)
        
        # حساب الوقت الجديد
        new_hour = (total_seconds // 3600) % 24
        new_minute = (total_seconds % 3600) // 60
        new_second = total_seconds % 60
        
        return Time(new_hour, new_minute, new_second)
    
    def __str__(self):
        """تمثيل نصي للوقت"""
        return self.to_standard_string()
    
    def __repr__(self):
        """تمثيل رسمي للوقت"""
        return f"Time({self.hour}, {self.minute}, {self.second})"
    
    def __add__(self, other):
        """جمع وقتين"""
        if isinstance(other, Time):
            total_seconds = (self.hour * 3600 + self.minute * 60 + self.second +
                            other.hour * 3600 + other.minute * 60 + other.second)
            hour = (total_seconds // 3600) % 24
            minute = (total_seconds % 3600) // 60
            second = total_seconds % 60
            return Time(hour, minute, second)
        elif isinstance(other, int):  # إضافة ثواني
            return self.add_seconds(other)
        else:
            raise TypeError("يمكن جمع Time فقط مع Time أو عدد صحيح")
```

### **الاختبار والتجربة**
```python
# إنشاء كائنات وقت
time1 = Time()  # 00:00:00
time2 = Time(14, 30, 45)  # 02:30:45 PM
time3 = Time(25, 70, 80)  # وقت غير صالح -> 00:00:00

# استخدام التوابع
print(f"الوقت 1: {time1.to_universal_string()}")  # 00:00:00
print(f"الوقت 2: {time2.to_standard_string()}")   # 02:30:45 PM

# تغيير الوقت
time1.set_time(8, 15, 20)
print(f"الوقت 1 بعد التغيير: {time1}")  # 08:15:20 AM

# إضافة ثواني
new_time = time2.add_seconds(3661)  # إضافة ساعة ودقيقة وثانية
print(f"الوقت 2 بعد إضافة 3661 ثانية: {new_time}")

# استخدام مشغل الجمع
time_sum = time1 + time2
print(f"مجموع الوقت 1 والوقت 2: {time_sum}")
```

## 🔄 **الوراثة المتقدمة: مثال Point → Circle → Cylinder**

### **التنفيذ التفصيلي**
```python
import math

class Point:
    """
    فئة النقطة تمثل نقطة في المستوى ثنائي الأبعاد
    """
    
    def __init__(self, x=0, y=0):
        """
        تهيئة النقطة بإحداثياتها
        
        Args:
            x (float): الإحداثي الأفقي
            y (float): الإحداثي الرأسي
        """
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        """حساب المسافة من النقطة إلى الأصل"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def distance_to(self, other_point):
        """حساب المسافة بين نقطتين"""
        return math.sqrt((self.x - other_point.x) ** 2 + 
                        (self.y - other_point.y) ** 2)
    
    def __str__(self):
        """تمثيل نصي للنقطة"""
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        """تمثيل رسمي للنقطة"""
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        """المساواة بين نقطتين"""
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        """جمع إحداثيات نقطتين"""
        return Point(self.x + other.x, self.y + other.y)


class Circle(Point):
    """
    فئة الدائرة ترث من النقطة وتضيف نصف القطر
    """
    
    def __init__(self, x=0, y=0, radius=1):
        """
        تهيئة الدائرة بمركز ونصف قطر
        
        Args:
            x (float): إحداثي x للمركز
            y (float): إحداثي y للمركز
            radius (float): نصف القطر (يجب أن يكون موجبًا)
        """
        super().__init__(x, y)  # استدعاء منشئ النقطة
        self.radius = abs(radius)  # تأكد أن نصف القطر موجب
    
    def area(self):
        """حساب مساحة الدائرة"""
        return math.pi * (self.radius ** 2)
    
    def circumference(self):
        """حساب محيط الدائرة"""
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """حساب قطر الدائرة"""
        return 2 * self.radius
    
    def contains_point(self, point):
        """التحقق إذا كانت النقطة داخل الدائرة"""
        distance = self.distance_to(point)
        return distance <= self.radius
    
    def __str__(self):
        """تمثيل نصي للدائرة"""
        return f"الدائرة مركزها {super().__str__()} ونصف قطرها {self.radius:.2f}"
    
    def __repr__(self):
        """تمثيل رسمي للدائرة"""
        return f"Circle({self.x}, {self.y}, {self.radius})"
    
    def __eq__(self, other):
        """المساواة بين دائرتين (نفس المركز ونصف القطر)"""
        return (super().__eq__(other) and 
                abs(self.radius - other.radius) < 0.0001)


class Cylinder(Circle):
    """
    فئة الأسطوانة ترث من الدائرة وتضيف الارتفاع
    """
    
    def __init__(self, x=0, y=0, radius=1, height=1):
        """
        تهيئة الأسطوانة بقاعدة دائرية وارتفاع
        
        Args:
            x (float): إحداثي x لمركز القاعدة
            y (float): إحداثي y لمركز القاعدة
            radius (float): نصف قطر القاعدة
            height (float): ارتفاع الأسطوانة
        """
        super().__init__(x, y, radius)  # استدعاء منشئ الدائرة
        self.height = abs(height)  # تأكد أن الارتفاع موجب
    
    def volume(self):
        """حساب حجم الأسطوانة"""
        return self.area() * self.height
    
    def lateral_surface_area(self):
        """حساب المساحة الجانبية للأسطوانة"""
        return self.circumference() * self.height
    
    def total_surface_area(self):
        """حساب المساحة الكلية للأسطوانة"""
        return (2 * self.area()) + self.lateral_surface_area()
    
    def __str__(self):
        """تمثيل نصي للأسطوانة"""
        return (f"الأسطوانة مركز قاعدتها {super().__str__()} "
                f"وارتفاعها {self.height:.2f}")
    
    def __repr__(self):
        """تمثيل رسمي للأسطوانة"""
        return f"Cylinder({self.x}, {self.y}, {self.radius}, {self.height})"
```

### **الاختبار العملي**
```python
# اختبار النقطة
p1 = Point(3, 4)
p2 = Point(6, 8)
print(f"النقطة 1: {p1}")  # (3, 4)
print(f"المسافة إلى الأصل: {p1.distance_to_origin():.2f}")  # 5.00
print(f"المسافة بين النقطتين: {p1.distance_to(p2):.2f}")  # 5.00

# اختبار الدائرة
circle = Circle(0, 0, 5)
print(f"\nالدائرة: {circle}")
print(f"مساحة الدائرة: {circle.area():.2f}")  # 78.54
print(f"محيط الدائرة: {circle.circumference():.2f}")  # 31.42
print(f"هل النقطة (3, 4) داخل الدائرة؟ {circle.contains_point(p1)}")  # True

# اختبار الأسطوانة
cylinder = Cylinder(0, 0, 5, 10)
print(f"\nالأسطوانة: {cylinder}")
print(f"حجم الأسطوانة: {cylinder.volume():.2f}")  # 785.40
print(f"المساحة الجانبية: {cylinder.lateral_surface_area():.2f}")  # 314.16
print(f"المساحة الكلية: {cylinder.total_surface_area():.2f}")  # 471.24

# التحقق من الوراثة
print(f"\nهل Circle ابن لـ Point؟ {issubclass(Circle, Point)}")  # True
print(f"هل Cylinder ابن لـ Circle؟ {issubclass(Cylinder, Circle)}")  # True
print(f"هل Cylinder ابن لـ Point؟ {issubclass(Cylinder, Point)}")  # True
```

## 🛠 **الدوال المهمة للميتا-برمجة والفحص**

### **1. الفحص الديناميكي للكائنات**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"مرحباً، أنا {self.name}"

# إنشاء كائن
person = Person("سارة", 25)

# فحص الخصائص والطرق
print(type(person))  # <class '__main__.Person'>
print(isinstance(person, Person))  # True
print(hasattr(person, 'name'))  # True
print(hasattr(person, 'greet'))  # True
print(hasattr(person, 'address'))  # False

# الحصول على القيم
print(getattr(person, 'name'))  # سارة
print(getattr(person, 'age', 'غير معروف'))  # 25
print(getattr(person, 'address', 'غير معروف'))  # غير معروف

# تعيين قيم جديدة
setattr(person, 'age', 26)
setattr(person, 'city', 'الرياض')
print(f"العمر الجديد: {person.age}")  # 26
print(f"المدينة: {person.city}")  # الرياض

# حذف خصائص
delattr(person, 'city')
# print(person.city)  # ❌ خطأ: الخاصية محذوفة
```

### **2. خصائص البرمجة (Properties)**
```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self._owner = owner
        self._balance = initial_balance
        self._transaction_history = []
    
    @property
    def balance(self):
        """الحصول على الرصيد (getter)"""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """تعيين الرصيد (setter)"""
        if amount < 0:
            raise ValueError("الرصيد لا يمكن أن يكون سالبًا")
        old_balance = self._balance
        self._balance = amount
        self._transaction_history.append(f"تعديل رصيد: {old_balance} → {amount}")
    
    @property
    def owner(self):
        """الحصول على اسم المالك (getter فقط)"""
        return self._owner
    
    def deposit(self, amount):
        """إيداع مبلغ"""
        if amount > 0:
            self.balance += amount  # يستخدم الـ setter
            self._transaction_history.append(f"إيداع: +{amount}")
        else:
            raise ValueError("المبلغ يجب أن يكون موجبًا")
    
    def withdraw(self, amount):
        """سحب مبلغ"""
        if 0 < amount <= self.balance:
            self.balance -= amount  # يستخدم الـ setter
            self._transaction_history.append(f"سحب: -{amount}")
        else:
            raise ValueError("المبلغ غير صالح أو غير متوفر")
    
    @property
    def transaction_count(self):
        """عدد المعاملات (خاصية محسوبة)"""
        return len(self._transaction_history)
    
    @property
    def last_transaction(self):
        """آخر معاملة"""
        if self._transaction_history:
            return self._transaction_history[-1]
        return "لا توجد معاملات"
```

## 📝 **الممارسات الجيدة في OOP مع بايثون**

### **1. التوثيق الجيد (Documentation)**
```python
class Employee:
    """
    فئة تمثل موظف في الشركة
    
    Attributes:
        name (str): اسم الموظف
        employee_id (int): رقم تعريف الموظف
        department (str): القسم الذي يعمل فيه
        salary (float): الراتب الشهري
        years_of_service (int): سنوات الخدمة
    """
    
    def __init__(self, name, employee_id, department, salary=3000):
        """
        تهيئة كائن الموظف
        
        Args:
            name (str): اسم الموظف
            employee_id (int): رقم تعريف الموظف
            department (str): القسم
            salary (float, optional): الراتب الشهري. Defaults to 3000.
        
        Raises:
            ValueError: إذا كان الراتب سالبًا
        """
        if salary < 0:
            raise ValueError("الراتب لا يمكن أن يكون سالبًا")
        
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.years_of_service = 0
    
    def promote(self, salary_increase_percentage=10):
        """
        ترقية الموظف وزيادة راتبه
        
        Args:
            salary_increase_percentage (float, optional): 
                نسبة زيادة الراتب. Defaults to 10.
        
        Returns:
            float: الراتب الجديد
        """
        increase = self.salary * (salary_increase_percentage / 100)
        self.salary += increase
        self.years_of_service += 1
        return self.salary
    
    def annual_bonus(self):
        """
        حساب المكافأة السنوية
        
        Returns:
            float: المكافأة السنوية
        """
        base_bonus = self.salary * 0.5  # نصف الراتب كأساس
        service_bonus = self.years_of_service * 500
        return base_bonus + service_bonus
```

### **2. التقسيم المنطقي للصفوف**
```python
# نظام إدارة المكتبة
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class LibraryItem(ABC):
    """فئة مجردة تمثل عنصرًا في المكتبة"""
    
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_available = True
        self.due_date = None
    
    @abstractmethod
    def get_loan_period(self):
        """الحصول على مدة الاستعارة"""
        pass
    
    def borrow(self, borrower):
        """استعارة العنصر"""
        if self.is_available:
            self.is_available = False
            self.due_date = datetime.now() + timedelta(days=self.get_loan_period())
            return f"تم استعارة '{self.title}' حتى {self.due_date.strftime('%Y-%m-%d')}"
        return f"العنصر '{self.title}' غير متاح حاليًا"
    
    def return_item(self):
        """إرجاع العنصر"""
        self.is_available = True
        self.due_date = None
        return f"تم إرجاع '{self.title}'"
    
    def __str__(self):
        status = "متاح" if self.is_available else "مستعار"
        return f"{self.title} ({self.item_id}) - {status}"


class Book(LibraryItem):
    """فئة الكتاب ترث من LibraryItem"""
    
    def __init__(self, title, item_id, author, isbn, pages):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn
        self.pages = pages
    
    def get_loan_period(self):
        return 14  # 14 يوم للكتب
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - {self.author} ({self.pages} صفحة)"


class Magazine(LibraryItem):
    """فئة المجلة ترث من LibraryItem"""
    
    def __init__(self, title, item_id, issue_number, publication_date):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date
    
    def get_loan_period(self):
        return 7  # 7 أيام للمجلات
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - العدد {self.issue_number} ({self.publication_date})"


class DVD(LibraryItem):
    """فئة DVD ترث من LibraryItem"""
    
    def __init__(self, title, item_id, director, duration, rating):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration  # بالدقائق
        self.rating = rating
    
    def get_loan_period(self):
        return 3  # 3 أيام للأقراص DVD
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - إخراج: {self.director} ({self.duration} دقيقة)"
```

## 🏆 **الخلاصة النهائية للفصل السابع**

### **1. المفاهيم الأساسية التي تم استيعابها**
- **الصفوف (Classes)**: كائنات برمجية تجمع البيانات والسلوكيات
- **الكائنات (Objects)**: نماذج عملية تنشأ من الصفوف
- **الوراثة (Inheritance)**: آلية لاستعادة واستخدام كود الصفوف الموجودة
- **التغليف (Encapsulation)**: إخفاء تفاصيل التنفيذ الداخلية
- **تعدد الأشكال (Polymorphism)**: قدرة الكائنات على الاستجابة بطرق مختلفة

### **2. المهارات المكتسبة**
- ✓ تصميم وتنفيذ الصفوف المعقدة
- ✓ استخدام الوراثة لإنشاء تسلسلات هرمية
- ✓ زيادة تحميل المشغلين باستخدام التوابع الجاهزة
- ✓ تطبيق مبادئ OOP في مشاريع حقيقية
- ✓ إدارة حالات الكائنات بفعالية

### **3. الاختلافات المهمة في بايثون**
- **المرونة**: لا توجد محددات وصول صارمة
- **الوراثة المتعددة**: مدعومة بشكل كامل
- **التوابع الجاهزة**: نظام قوي لزيادة تحميل المشغلين
- **البرمجة الديناميكية**: إمكانية تعديل الصفوف أثناء التنفيذ

### **4. أفضل الممارسات**
- استخدام أسماء واضحة ووصفية
- توثيق الكود بشكل شامل
- تقسيم المسؤوليات بين الصفوف
- استخدام الوراثة عند وجود علاقة "is-a" حقيقية
- اختبار الصفوف بشكل منفصل

يُمكنّن هذا الفصل المبرمجين من بناء أنظمة برمجية معقدة وقابلة للصيانة، مع التركيز على المبادئ الأساسية للبرمجة غرضية التوجه وتطبيقها الفعلي في بيئة بايثون.