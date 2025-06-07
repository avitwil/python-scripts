def sort_input(x):
    z1 = ""
    z2 = ""
    for i in x:
        if i.isdigit() is True or i == ".":
            z1 = z1 + i
        elif i == "+" or i == "-" or i == "*" or i == "/":
            z2 = z2 + i
            z1 = z1 + ":"
        else:
            print("invalid input")
            sort_input()
    y = z1.split(":")
    z = 0
    w =[]
    for i in z2:
        w = w + [int(y[z]), z2[z]]
        z = z + 1
    w.append(int(y[-1]))
    return w
def calculate(x):
    while not x.count("/") == 0 or not x.count("*") == 0:
        yd = 0
        ym = 0
        if not x.count("/") == 0:
            yd = x.index("/")
        if not x.count("*") == 0:
            ym = x.index("*")
        if yd > 0 and yd < ym or ym == 0:
            y1 = yd - 1
            y2 = yd + 1
            z = x[y1] / x[y2]
        else:
            y1 = ym - 1
            y2 = ym + 1
            z = x[y1] * x[y2]
        x.pop(y1)
        x.pop(y1)
        x.pop(y1)
        x.insert(y1, z)
    while not x.count("+") == 0 or not x.count("-") == 0:
        yd = 0
        ym = 0
        if not x.count("-") == 0:
            yd = x.index("-")
        if not x.count("+") == 0:
            ym = x.index("+")
        if yd > 0 and yd < ym or ym == 0:
            y1 = yd - 1
            y2 = yd + 1
            z = x[y1] - x[y2]
        else:
            y1 = ym - 1
            y2 = ym + 1
            z = x[y1] + x[y2]
        x.pop(y1)
        x.pop(y1)
        x.pop(y1)
        x.insert(y1, z)





    return x[0]
def check_input(n):

    y = 0
    for i in n:
        y1 = y - 1
        y2 = y + 1
        if i.isdigit() is False:
            if y == 0 or n[y1].isdigit() is False or n[y2].isdigit() is False or not(i == "+" or i == "-" or i == "*" or i == "/"):
                print("invalid input --- exiting")
                exit()
        y = y + 1


l = input("enter your calculation \n")
check_input(l)
x1 = sort_input(l)
x2 = calculate(x1)
print(l + " = " + str(x2))

l = input("enter your calculation \n")
x1 = sort_input(l)
x2 = calculate(x1)
print(l + " = " + str(x2))

