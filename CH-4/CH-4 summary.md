# مقرر برمجة 3 بايثون
## الفصل الرابع: البرامج الجزئية Subprograms والتابع "لامبادا" Lambda
---

### **المفاهيم الأساسية**
- **البرامج الجزئية**: التوابع والدوال في بايثون
- **تمرير الوسطاء**: بالقيمة وبالمرجع
- **مجال رؤية المتحولات**: local, global, nonlocal
- **التابع lambda**: التوابع المجهولة الاسم
- **توابع الجداول الخاصة**: filter, map, reduce

### **ملخص**
يغطي هذا الفصل كيفية تصميم البرامج الجزئية، وتمرير الوسطاء، والتحكم بمجال رؤية المتحولات، والمفهوم الجديد: التابع lambda المفيد مع تطبيق التوابع الخاصة بالجداول filter, map, reduce.

---

## **1. البرامج الجزئية Subprograms**

### **1.1 أهمية البرامج الجزئية**
البرامج الجزئية تمثل الانتقال من البرمجة الصغيرة إلى البرمجة الكبيرة، حيث يتم تقسيم البرنامج إلى أجزاء صغيرة يسهل إدارتها.

**فوائد استخدام البرامج الجزئية:**
1. **تقليل التعقيد**: تقسيم المشكلة إلى أجزاء أبسط
2. **إعادة الاستخدام**: تجنب تكرار نفس التعليمات
3. **الصيانة السهلة**: تعديل جزء دون التأثير على الآخرين

### **1.2 تعريف التوابع في بايثون**
```python
def function_name(parameters):
    """docstring"""
    # function body
    return value
```

### **1.3 مثال: تابع حساب المضروب**
```python
def fact(n):
    """Calculate factorial of n"""
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

# استخدام التابع
N = int(input("Input N: "))
M = int(input("Input M: "))
result = fact(N) // (fact(M) * fact(N - M))
print(f"C({N},{M}) = {result}")
```

### **1.4 مثال: تابع فرز الجداول**
```python
def bubbleSort(a):
    """Sort any list using bubble sort"""
    n = len(a)
    if n == 0:
        return []
    
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# اختبار التابع مع أنواع مختلفة
integerList = [23, 45, 1, 56, 3, 6]
bubbleSort(integerList)
print(integerList)  # [1, 3, 6, 23, 45, 56]

floatList = [0.9, 9.5, 67.8, 45, 23.1]
bubbleSort(floatList)
print(floatList)  # [0.9, 9.5, 23.1, 45, 67.8]

stringList = ["Zouhair", "Rama", "Mera", "Ahmad", "Kamel"]
bubbleSort(stringList)
print(stringList)  # ['Ahmad', 'Kamel', 'Mera', 'Rama', 'Zouhair']
```

---

## **2. تمرير الوسطاء Parameter Passing**

### **2.1 تمرير الوسيط بالقيمة (للمتغيرات البسيطة)**
```python
x = 5

def change(x):
    x = 9
    print(f"Inside function: x = {x}")

change(x)  # Inside function: x = 9
print(f"Outside function: x = {x}")  # Outside function: x = 5
```

### **2.2 تمرير الوسيط بالمرجع (للقوائم والمتغيرات المركبة)**
```python
def modify_list(lst):
    lst.append(4)
    lst[0] = 99

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [99, 2, 3, 4]
```

### **2.3 تمرير تابع كوسيط**
```python
def Map(f, iList):
    """Apply function f to each element in iList"""
    resultList = []
    for element in iList:
        resultList.append(f(element))
    return resultList

def cubeX(x):
    return x ** 3

iList = [0, 1, 2, 3, 4, 5]
rList = Map(cubeX, iList)
print(rList)  # [0, 1, 8, 27, 64, 125]
```

---

## **3. التوابع الداخلية Nested Functions**

### **3.1 تعريف التوابع الداخلية**
```python
def outer_function():
    x = 5
    
    def inner_function():
        x = 9
        print(f"Inside inner function: x = {x}")
    
    inner_function()
    print(f"Inside outer function: x = {x}")

outer_function()
# Output:
# Inside inner function: x = 9
# Inside outer function: x = 5
```

---

## **4. مجال رؤية المتحولات Variable Scope**

### **4.1 المتحولات المحلية والعالمية**
```python
x = 5  # Global variable

def subProg1():
    global x  # Use global keyword to modify global variable
    x = 9
    print(f"subProg1 x = {x}")

def subProg2():
    global x
    x = 10
    print(f"subProg2 x = {x}")

print(f"Main prog x = {x}")  # Main prog x = 5
subProg1()  # subProg1 x = 9
subProg2()  # subProg2 x = 10
print(f"Main prog x = {x}")  # Main prog x = 10
```

### **4.2 استخدام nonlocal للتوابع الداخلية**
```python
def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x  # Modify variable from outer function
        x = 15
        print(f"inner function: x = {x}")
    
    print(f"outer function: x = {x}")  # outer function: x = 10
    inner_function()  # inner function: x = 15
    print(f"outer function: x = {x}")  # outer function: x = 15

outer_function()
```

---

## **5. التابع Lambda**

### **5.1 تعريف التوابع المجهولة الاسم**
```python
# تابع تقليدي
def cubeX(x):
    return x ** 3

# تابع lambda مكافئ
cubeX_lambda = lambda x: x ** 3

print(cubeX(3))  # 27
print(cubeX_lambda(3))  # 27
```

### **5.2 استخدام lambda مع التوابع**
```python
def Map(f, iList):
    resultList = []
    for element in iList:
        resultList.append(f(element))
    return resultList

iList = [0, 1, 2, 3, 4, 5]
# استخدام lambda مباشرة
rList = Map(lambda x: x ** 3, iList)
print(rList)  # [0, 1, 8, 27, 64, 125]
```

---

## **6. توابع الجداول الخاصة**

### **6.1 تابع الفلترة filter()**
```python
# تصفية الأعداد الأصغر من 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered = list(filter(lambda x: x < 4, numbers))
print(filtered)  # [1, 2, 3]
```

### **6.2 تابع التقابل map()**
```python
# حساب مربعات الأعداد
numbers = [1, 2, 4, 8]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 16, 64]
```

### **6.3 تابع التقليص reduce()**
```python
import functools

# جمع مربعات الأعداد
result = functools.reduce(lambda x, y: x + y ** 2, [1, 2, 3, 4])
print(result)  # 30
# الخطوات:
# 1 + 2² = 5
# 5 + 3² = 14  
# 14 + 4² = 30
```

---

## **7. قوة التوابع في بايثون**

### **7.1 المرونة في التعامل مع الأنماط**
```python
# نفس التابع يعمل مع أنواع مختلفة
def process_data(data):
    return len(data)

print(process_data("Hello"))  # 5 (string)
print(process_data([1, 2, 3]))  # 3 (list)
print(process_data((1, 2, 3, 4)))  # 4 (tuple)
```

### **7.2 التوابع كمتغيرات**
```python
def square(x):
    return x * x

def cube(x):
    return x * x * x

# تخزين التوابع في قائمة
operations = [square, cube]

for func in operations:
    print(func(3))  # 9, 27
```

---

## **8. تمارين عملية**

### **8.1 بيانات الطلاب**
```python
Students = [
    [12436, "Sami Ahmad", 56.3, 74.6],
    [12440, "Anas Mansour", 34.4, 80.9],
    [13822, "Moustafa Zein", 80, 13],
    [12440, "Ahmad Khaled", 50.4, 50.5]
]
```

### **8.2 التابع: حساب المحصلة**
```python
def Score(student):
    """Calculate student score: 70% exam + 30% practical"""
    xam = student[2]
    pract = student[3]
    return xam * 0.7 + pract * 0.3
```

### **8.3 التابع: تحديد النجاح**
```python
def isSuccess(student):
    """Check if student passed"""
    xam = student[2]
    pract = student[3]
    score = Score(student)
    
    return xam >= 40 and pract >= 40 and score >= 60
```

### **8.4 التابع: النتائج النهائية**
```python
def FinalResults(Students):
    """Calculate final results for all students"""
    for student in Students:
        score = Score(student)
        success = isSuccess(student)
        student.extend([score, success])
    return Students
```

### **8.5 استخدام filter مع lambda**
```python
def Success(Students):
    """Get list of successful students using filter"""
    return list(filter(lambda student: student[5], Students))

def FailBut(Students):
    """Get students who failed but passed practical"""
    return list(filter(lambda student: not student[5] and student[3] >= 40, Students))
```

---

## **9. الكلمات المحجوزة المستخدمة**

### **الكلمات الجديدة في هذا الفصل:**
- `def` - لتعريف التوابع
- `return` - لإرجاع القيم
- `global` - للوصول للمتغيرات العالمية
- `nonlocal` - للوصول للمتغيرات في الدوال الخارجية
- `lambda` - لتعريف التوابع المجهولة

### **الكلمات المحجوزة الكاملة (33 كلمة):**
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

---

## **10. التوابع المسبقة التعريف المستخدمة**

### **10.1 التوابع الأساسية للفصل**

| التابع | الوصف | الفصل |
|--------|-------|-------|
| `filter()` | تصفية عناصر التكرار بناء على شرط | Ch04 |
| `map()` | تطبيق دالة على كل عنصر في التكرار | Ch04 |
| `len()` | إرجاع طول الكائن | Ch01, Ch02, Ch03, Ch04 |
| `list()` | تحويل إلى قائمة | Ch01, Ch02, Ch03, Ch04 |

### **10.2 أمثلة استخدام متقدمة**
```python
# سلسلة من العمليات على البيانات
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# تصفية الأعداد الزوجية ثم تربيعها
result = list(map(lambda x: x ** 2, 
                 filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16, 36, 64, 100]
```

---

## **🎯 النقاط الهامة في الفصل الرابع**

- ✅ **البرامج الجزئية** - تقسيم البرنامج إلى أجزاء قابلة للإدارة
- ✅ **تمرير الوسطاء** - بالقيمة للمتغيرات البسيطة، وبالمرجع للقوائم
- ✅ **مجال الرؤية** - local, global, nonlocal للتحكم بالمتغيرات
- ✅ **التوابع الداخلية** - إمكانية تعريف دوال داخل دوال
- ✅ **التابع lambda** - دوال مجهولة الاسم للاستخدامات البسيطة
- ✅ **filter, map, reduce** - توابع قوية لمعالجة البيانات
- ✅ **المرونة** - نفس التابع يمكن أن يعمل مع أنواع مختلفة من البيانات
- ✅ **إعادة الاستخدام** - كتابة الكود مرة واحدة واستخدامه多次
- ✅ **الصيانة** - سهولة تعديل وتطوير الأجزاء المنفصلة

**الخلاصة**: هذا الفصل يمثل نقلة نوعية في البرمجة، حيث يتعلم الطالب كيفية تنظيم الكود بشكل احترافي باستخدام التوابع والدوال، مع الاستفادة من الميزات المتقدمة في بايثون مثل lambda و filter و map و reduce لكتابة كود أكثر كفاءة وقابلية للقراءة.