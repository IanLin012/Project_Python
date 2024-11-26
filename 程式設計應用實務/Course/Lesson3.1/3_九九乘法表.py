for i in range(1, 10):
    for j in range(1, 10):
        if(j == 9):
            print(str(i) + " x " + str(j) + " = " + str(i*j) + ",")
        else:
            print(str(i) + " x " + str(j) + " = " + str(i*j) + ",", end=' ')