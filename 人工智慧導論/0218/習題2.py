x = int(input("Please enter x: "))
y = int(input("Please enter y: "))

for i in range(1, x+1):
    for j in range(1, y+1):
        print(i, "*", j, "=", i*j, end = ", ")
    print()