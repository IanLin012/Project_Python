def initial():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    func = int(input("Enter choice(1/2/3/4): "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if(func == 1):
        print(a, "+", b, "=", add(a, b))
    elif(func == 2):
        print(a, "-", b, "=", sub(a, b))
    elif(func == 3):
        print(a, "*", b, "=", mul(a, b))
    elif(func == 4):
        print(a, "/", b, "=", div(a, b))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == "__main__":
    initial()
