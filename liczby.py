numbers=[value for value in range(1,10)]


for value in numbers:
    if value == 1:
        print(str(value)+"st")
    elif value == 2:
        print(str(value)+"nd")
    elif value == 3:
        print(str(value)+"rd")
    else:
        print(str(value)+"th")

