Weather = input("Please enter weather(sunny, rainy): ")
Temperature = int(input("Please enter temperature(0-40°C): "))

if Weather=="sunny":
    if Temperature>=25:
        print("Steak")
    else:
        print("Oden")
elif Weather=="rainy":
    if Temperature<=25:
        print("McDonald's")
    else:
        print("Hotpot")