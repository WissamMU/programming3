# ImageN = int(input("how many images do you have : "))
# ImageT = input("what is the Images type png webp : ")
# FileN = input("what is the file name t-shirt chef : ")
# print("\n \n \n \n")
# i = 1
# while i <= ImageN:
#     print(f'- "../../images/product/{FileN}/({i}).{ImageT}"')
#     i += 1

S = "what is world wide web : www"
sf = "w"
print("String: " + S)
print("Looking for: " + sf)
print()

ib = iw = nw = 0
while ib < len(S):
    try:
        iw = S.index(sf, ib)
        print("{0} found at index {1}".format(sf, iw))
        nw += 1
        ib = iw + 1
    except ValueError:
        break

print("word ({0}) found {1} times".format(sf, nw))