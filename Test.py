def getBMI(h: str, w: str)-> float: # type hint
    h = float(h)/100
    bmi = round(w/(h*h), 2)
    return bmi

group = {'john': ('John', 172, 68),
        'nick': ('Nick', 180, 58),
        'mary': ('Mary', 160, 90),}

for p_id, p_value in group.items():
    n, h, w = p_value[0], p_value[1], p_value[2]
    print(f"The weight, height and BMI of {n} is {h}, {w} and {getBMI(h, w)}")