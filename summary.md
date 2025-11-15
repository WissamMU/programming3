---
# مقرر برمجة 3 بايثون  
## الفصل الأول: التعليمات والأنماط الأساسية  
---

### **المفاهيم الأساسية**
- **التعليمات الأساسية**: `if`, `if-else`, `while`, `for`  
- **الأنماط الأساسية**: `int`, `float`, `bool`, `string`  

---

## **1. التعليمات الأساسية**

### **مثال عملي: حساب القاسم المشترك الأعظم (GCD) باستخدام خوارزمية إقليدس**


#### **Python**
```python
# Read a, b
Sa = input("a="); a = int(Sa)
Sb = input("b="); b = int(Sb)

# Compute GCD of a and b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
g = a
print("GCD = " + str(g))
```

---

## **تعليمات القراءة**

### **1.1 تعليمة القراءة `input()`**
- تقرأ دخلاً كسلسلة نصية.  
- لتحويل النوع: استخدم `int()`, `float()`, `bool()`.

```python
Sa = input("input a :"); a = int(Sa)
Sb = input("input b :"); b = int(Sb)
a = int(input("input a :"))
```

> **ملاحظة**: لا يوجد تعريف لنمط المتغير في Python، بل يُحدد ضمنيًا عبر الإسناد.

---

## **تعليمات الكتابة**

### **2.1 تعليمة الكتابة `print()`**
- تطبع قيم المعاملات (أعداد، سلاسل نصية، إلخ).  
- تفصل المعاملات بفاصلة `,`.  
- لدمج سلسلة نصية مع قيم أخرى: استخدم `str()`.

```python
a=5; b=7; c=8; g=1
print("a , b, c", a, b, c)
print("GCD =" + str(g))
```

---

## **تعليمة الإسناد**

### **3.1 الإسناد**
```python
a = b = c = d = 8   # إسناد متعدد
```

> - يُحدد نمط المتغير ضمنيًا (`implicitly`).  
> - يمكن أن يتغير النمط مع كل إسناد جديد.

### **الإسناد المزود بعملية**
```python
a += b    # معادل لـ: a = a + b
b *= 3    # معادل لـ: b = b * 3
```

---

## **العمليات الحسابية والتعابير الرياضية**

| العملية | الوصف |
|--------|-------|
| `+`, `-`, `*`, `/` | جمع، طرح، ضرب، قسمة |
| `//` | قسمة صحيحة (النتيجة عدد صحيح) |
| `%` | الباقي |
| `**` | الأس (رفع للقوة) |
| `()` | الأقواس لتحديد الأولوية |

### **أولويات العمليات**
1. `()`  
2. `**`  
3. `*`, `/`, `%`  
4. `+`, `-`

> **ملاحظات**:  
> - إذا كان أحد العددين `float` → النتيجة `float`.  
> - القسمة `/` دائمًا تُعيد `float`، استخدم `//` للقسمة الصحيحة.

---

## **التعليمة الشرطية `if`**

### **4.1 الأشكال الثلاثة**

#### **1. `if`**
```python
if expression:
    instructionBlock
```

#### **2. `if-else`**
```python
if expression:
    instructionBlock1
else:
    instructionBlock2
```

#### **3. `if-elif`**
```python
if expression1:
    instructionBlock1
elif expression2:
    instructionBlock2
```

> - يُحدد الكتل بالمحاذاة (**alignment**).  
> - بعد كل `if`, `elif`, `else`, `while` → يجب إزاحة الأوامر.

---

### **تعليمة الإسناد الشرطية (C-Like)**

#### **C#**
```csharp
if (expression) Value1 else Value2
```

#### **Python**
```python
A = Value1 if expression else Value2
```

---

## **التعليقات (Comments)**

### **تعليق سطر واحد**
```python
# This is a comment
```

### **تعليق متعدد الأسطر**
```python
"""
Python is an interpreted, high-level and general-purpose
programming language. Created by Guido van Rossum and first
released in 1991
"""
```

> - لا تُنفذ، تُستخدم للتوضيح.  
> - لا يمكن وضع `#` داخل سلسلة نصية كتعليق.

---

## **جدول التعليمات في بايثون**

| الرقم | التعليمة | الوصف |
|------|----------|-------|
| 1 | `input()` | قراءة الدخل |
| 2 | `print()` | كتابة النتيجة |
| 3 | `=` | إسناد قيمة |
| 4 | `if`, `elif`, `else` | تعليمة شرطية |
| 5 | `while` | تعليمة تكرارية |

> - كتل التعليمات تُحدد بالإزاحة (indentation).  
> - لا أقواس، لا فواصل منقوطة.

---

## **الكلمات المحجوزة في بايثون (من الصفحة 36-37)**

### **الكلمات المحجوزة المستعملة**
- `if`, `else`, `elif`, `while`, `for`, `in`, `and`, `or`, `not`, `True`, `False`, `input`, `print`, `int`, `float`, `bool`, `str`

### **الكلمات المحجوزة الكاملة**
(سيتم إدراجها لاحقًا من الصفحة 37)

---

## **التوابع مسبقة التعريف المستعملة**

| الدالة | الوصف |
|-------|-------|
| `int(x)` | تحويل إلى عدد صحيح |
| `float(x)` | تحويل إلى عدد حقيقي |
| `bool(x)` | تحويل إلى قيمة منطقية |
| `str(x)` | تحويل إلى سلسلة نصية |
| `input(prompt)` | قراءة من المستخدم |
| `print(*args)` | طباعة النتائج |

---

## **تنويهات هامة**
- **الإزاحة (Indentation)**: تُحدد الكتل، خطأ في الإزاحة = خطأ نحوي.  
- **التعليقات**: لا تؤثر على التنفيذ.  
- **الإسناد المتعدد**: `a = b = c = 5`  
- **التحويل التلقائي**: يحدث عند الجمع بين `int` و `float`.  
- **عملية القسمة**:  
  - `/` → دائمًا `float`  
  - `//` → قسمة صحيحة

---
# مقرر برمجة 3 بايثون  
## الفصل الأول: التعليمات والأنماط الأساسية  
---

### **المفاهيم الأساسية**
- **التعليمات الأساسية**: `if`, `if-else`, `while`, `for`  
- **الأنماط الأساسية**: `int`, `float`, `bool`, `string`  

---

## **1. التعليمات الأساسية**

### **مثال عملي: حساب القاسم المشترك الأعظم (GCD) باستخدام خوارزمية إقليدس**

#### **Python**
```python
# Read a, b
Sa = input("a="); a = int(Sa)
Sb = input("b="); b = int(Sb)

# Compute GCD of a and b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
g = a
print("GCD = " + str(g))
```

---

## **2. تعليمات القراءة والكتابة**

### **2.1 تعليمة القراءة `input()`**
- تقرأ دخلاً كسلسلة نصية.  
- لتحويل النوع: استخدم `int()`, `float()`, `bool()`.

```python
# قراءة عدد صحيح
Sa = input("input integer: "); a = int(Sa)

# قراءة عدد عشري
Sb = input("input float: "); b = float(Sb)

# قراءة قيمة منطقية
Sc = input("input boolean: "); c = bool(Sc)
```

> **ملاحظة**: لا يوجد تعريف لنمط المتغير في Python، بل يُحدد ضمنيًا عبر الإسناد.

### **2.2 تعليمة الكتابة `print()`**
- تطبع قيم المعاملات (أعداد، سلاسل نصية، إلخ).  
- تفصل المعاملات بفاصلة `,`.  
- لدمج سلسلة نصية مع قيم أخرى: استخدم `str()`.

```python
a = 5; b = 7; c = 8; g = 1
print("a, b, c:", a, b, c)
print("GCD = " + str(g))
```

---

## **3. تعليمة الإسناد**

### **3.1 الإسناد الأساسي**
```python
a = b = c = d = 8   # إسناد متعدد
```

> - يُحدد نمط المتغير ضمنيًا (`implicitly`).  
> - يمكن أن يتغير النمط مع كل إسناد جديد.

### **3.2 الإسناد المزود بعملية**
```python
a += b    # معادل لـ: a = a + b
b *= 3    # معادل لـ: b = b * 3
a -= 5    # معادل لـ: a = a - 5
```

---

## **4. العمليات الحسابية والتعابير الرياضية**

| العملية | الوصف |
|--------|-------|
| `+`, `-`, `*`, `/` | جمع، طرح، ضرب، قسمة |
| `//` | قسمة صحيحة (النتيجة عدد صحيح) |
| `%` | الباقي |
| `**` | الأس (رفع للقوة) |
| `()` | الأقواس لتحديد الأولوية |

### **أولويات العمليات**
1. `()`  
2. `**`  
3. `*`, `/`, `%`, `//`  
4. `+`, `-`

> **ملاحظات**:  
> - إذا كان أحد العددين `float` → النتيجة `float`.  
> - القسمة `/` دائمًا تُعيد `float`، استخدم `//` للقسمة الصحيحة.

---

## **5. التعليمة الشرطية `if`**

### **5.1 الأشكال الثلاثة**

#### **الشكل 1: `if` فقط**
```python
if expression:
    instructionBlock
```

#### **الشكل 2: `if-else`**
```python
if expression:
    instructionBlock1
else:
    instructionBlock2
```

#### **الشكل 3: `if-elif`**
```python
if expression1:
    instructionBlock1
elif expression2:
    instructionBlock2
else:
    instructionBlock3
```

### **5.2 الصيغة المختصرة (Conditional Expression)**
```python
# الصيغة المختصرة للإسناد الشرطي
absx = x if (x >= 0) else -x

# مقابلتها في C#:
# absx = (x >= 0) ? x : -x;
```

> **ملاحظات هامة**:  
> - يُحدد الكتل بالمحاذاة (**alignment**).  
> - بعد كل `if`, `elif`, `else`, `while` → يجب إزاحة الأوامر.  
> - لا توجد نهاية صريحة للتعليمة (لا وجود لـ `;` في النهاية).

---

## **6. التعليمة التكرارية `while`**

### **6.1 الشكل الأساسي**
```python
while expression:
    instructionBlock
```

### **مثال: إيجاد أكبر عدد في سلسلة**
```python
Sa = input("a= "); a = int(Sa)
max = a
while (a != 999):
    if (a > max):
        max = a
    a = int(input("a= "))

if (max != 999):
    print("max =", max)
```

---

## **7. التعليمة التكرارية `for`**

### **7.1 استخدام `range()`**
```python
# حساب مجموع الأعداد من 1 إلى M
M = int(input("Input M: "))
s = 0
for i in range(1, M+1):
    s = s + i
print("1+2+...+" + str(M) + " = " + str(s))

# حساب مضروب M (M!)
s = 1
for i in range(1, M+1):
    s = s * i
print(str(M) + "! = " + str(s))
```

> **ملاحظة**: `range(1, M+1)` يبدأ من 1 وينتهي عند M (شامل).

---

## **8. كسر وتخطي التكرار**

### **8.1 `break` - كسر التكرار**
```python
i = 0; n = 13
while (i <= n):
    if ((i % 4 == 0) and (i > 4)):
        break
    print("i =", i)
    i = i + 1
```

### **8.2 `continue` - تخطي التكرار الحالي**
```python
for i in range(0, 14):
    if ((i % 4 == 0) and (i > 4)):
        continue
    print("i =", i)
```

> **ملاحظة**: لا توجد تعليمة `do-while` في Python.

---

## **9. الأنماط الأساسية**

### **9.1 الأنماط البسيطة**
```python
# assign integer
i = 34
# assign float
f = 105.7
# assign complex
c = 5+4j
# assign Boolean
b = True
# assign string
s = "This is a string"
```

### **9.2 مرونة الأنماط في Python**
```python
a = 34
print("a=", a, type(a))        # <class 'int'>

a = 105.7
print("a=", a, type(a))        # <class 'float'>

a = True
print("a=", a, type(a))        # <class 'bool'>

a = "This is a string"
print("a=", a, type(a))        # <class 'str'>
```

### **9.3 الأنماط العددية**
- `int` - الأعداد الصحيحة
- `float` - الأعداد العشرية  
- `complex` - الأعداد العقدية

### **9.4 النمط المنطقي `bool`**
- القيم: `True`, `False`
- العمليات: `and`, `or`, `not`

#### **جداول الحقيقة**
| A | B | A and B | A or B | not A |
|---|----|---------|--------|-------|
| F | F | F | F | T |
| F | T | F | T | T |
| T | F | F | T | F |
| T | T | T | T | F |

---

## **10. العمليات على البتات (Bitwise Operations)**

### **10.1 التحويل بين أنظمة العد**
```python
a = 35
print(bin(a))   # 0b100011
print(oct(a))   # 0o43
print(hex(a))   # 0x23
```

### **10.2 العمليات الأساسية**
```python
a = 65    # 01000001
b = 35    # 00100011

print(a & b)   # 1   (00000001)
print(a | b)   # 99  (01100011)
print(a ^ b)   # 98  (01100010)
```

#### **جداول العمليات على البتات**
| A | B | A & B | A \| B | A ^ B |
|---|---|-------|--------|-------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

---

## **11. ميزات خاصة في Python**

### **11.1 استخدام `eval()`**
#### حساب قيمة اي تعبير يدخل 
```python
f1 = input("Function 1: f1(x) = ")  # x**2
f2 = input("Function 2: f2(x) = ")  # pow(x,3)

x0 = 0; dx = 0.25
for i in range(0, 10):
    x = x0 + i * dx
    y1 = eval(f1)   # يحسب قيمة التعبير
    y2 = eval(f2)
    print("%4.2f %6.2f %6.2f" % (x, y1, y2))
```

---

## **12. التمارين العملية**

### **التمرين 1: جدول الضرب**
```python
print("input k in [2..10] = ")
k = int(input())
i = 1
while (i <= 10):
    print(k, "x", i, "=", k * i)
    i = i + 1
```

### **التمرين 2: حل معادلة من الدرجة الثانية**
```python
import math
a = float(input("Input a = "))
b = float(input("Input b = "))
c = float(input("Input c = "))

delta = b * b - 4 * a * c
if delta < 0:
    print("No Real Solution")
elif delta == 0:
    x = -b / (2 * a)
    print("One Solution: x =", x)
else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("Two Solutions: x1 =", x1, "x2 =", x2)
```

### **التمرين 3: الأعداد الكاملة (Perfect Numbers)**
```python
n = int(input("Number of perfect numbers you wish find: "))
nbr = 2
compt = 0

while compt != n:
    sumdiv = 1
    k = 2
    while k <= nbr/2:
        if nbr % k == 0:
            sumdiv += k
        k += 1
    if sumdiv == nbr:
        print(nbr, "is a Perfect number")
        compt += 1
    nbr += 1
```

---

## **13. الكلمات المحجوزة في Python**

### **13.1 الكلمات المستخدمة في الفصل**
- `and`, `break`, `continue`, `elif`, `else`
- `False`, `for`, `if`, `import`, `in`
- `not`, `or`, `while`, `True`

True False None الكلمات الوحيدة  باول حرف كبير

### **13.2 الكلمات المحجوزة الكاملة (33 كلمة)**
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

## **14. التوابع مسبقة التعريف**

### **14.1 أهم التوابع المستخدمة**

| التابع | الوصف |
|--------|-------|
| `int()`, `float()`, `bool()`, `str()` | تحويل بين الأنماط |
| `input()`, `print()` | الإدخال والإخراج |
| `abs()`, `pow()`, `round()`, `sum()` | عمليات حسابية |
| `bin()`, `oct()`, `hex()` | تحويل بين أنظمة العد |
| `eval()` | تنفيذ تعبير |
| `type()`, `len()` | معلومات عن الكائنات |
| `range()` | توليد سلسلة أرقام |

### **14.2 أمثلة استخدام**
```python
# التحويل بين الأنظمة العددية
a = 35
print(bin(a))   # 0b100011
print(oct(a))   # 0o43
print(hex(a))   # 0x23

# التوابع الحسابية
print(abs(-5))      # 5
print(pow(2, 3))    # 8
print(round(3.14159, 2))  # 3.14
print(sum([1, 2, 3, 4]))  # 10
```

---

## ** النقاط الهامة**

- ✅ **المحاذاة** تحدد كتل التعليمات (بدلاً من الأقواس)
- ✅ **لا توجد نهاية صريحة** للتعليمة (لا وجود لـ `;`)
- ✅ **المرونة في الأنماط** - يتغير نمط المتغير مع كل إسناد
- ✅ **لا توجد** `switch-case` أو `do-while`
- ✅ **المحاذاة الإلزامية** - أساسية لصحة النص البرمجي
- ✅ **`eval()`** - أداة قوية لتنفيذ التعابير الديناميكية

---
