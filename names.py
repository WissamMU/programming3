ImageN = int(input("how many images do you have : "))
ImageT = input("what is the Images type png webp : ")
FileN = input("what is the file name t-shirt chef : ")
print("\n \n \n \n")
i = 1
while i <= ImageN:
    print(f'- "../../images/product/{FileN}/({i}).{ImageT}"')
    i += 1
