# ImageN = int(input("how many images do you have : "))
# ImageT = input("what is the Images type png webp : ")
# FileN = input("what is the file name t-shirt chef : ")
# print("\n \n \n \n")
# i = 1
# while i <= ImageN:
#     print(f'- "../../images/product/{FileN}/({i}).{ImageT}"')
#     i += 1

numbers = {1, 2, 3}
x = numbers.pop()   # هنا pop() تحذف عنصراً من المجموعة، وأيضاً تُرجِع هذا العنصر وتخزّنه في x
print(x)            # يطبع العنصر الذي أرجعته pop()
print(numbers)      # يطبع المجموعة بعد حذف هذا العنصر
