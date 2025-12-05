# ImageN = int(input("how many images do you have : "))
# ImageT = input("what is the Images type png webp : ")
# FileN = input("what is the file name t-shirt chef : ")
# print("\n \n \n \n")
# i = 1
# while i <= ImageN:
#     print(f'- "../../images/product/{FileN}/({i}).{ImageT}"')
#     i += 1

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