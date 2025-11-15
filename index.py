# x_values = []
# y_values = []

# # Open and read the CSV file
# myfile = open(r"C:\Users\wesaa\OneDrive\Desktop\data.csv", "r")
# lines = myfile.readlines()  # Read all lines

# # Skip the header row and parse the data
# for line in lines[1:]:  # Skip the header row ("X,Y\n")
#     x, y = line.strip().split(",")  # Split each line by comma
#     x_values.append(float(x))  # Convert X to float and append
#     y_values.append(float(y))  # Convert Y to float and append

# myfile.close()

# # Print the first 10 items in a nicely formatted list
# print("\nFirst 10 X and Y Values:")
# print("-" * 30)
# print(f"{'Index':<6} {'X Value':<12} {'Y Value':<12}")
# print("-" * 30)
# for i in range(min(51, len(x_values))):  # Ensure we don't exceed list length
#     print(f"{i:<6} {x_values[i]:<12.6f} {y_values[i]:<12.6f}")



f1 = input("Function 1: f1(x) = ")  # x**2
f2 = input("Function 2: f2(x) = ")  # pow(x,3)

x0 = 0
dx = 0.25
for i in range(0, 10):
    x = x0 + i * dx
    y1 = eval(f1)  # يحسب قيمة التعبير
    y2 = eval(f2)
    print("%4.2f %6.2f %6.2f" % (x, y1, y2))
