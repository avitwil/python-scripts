def calculator():
    x = input("enter your calculation: ")
    i = 0
    for j in x:
        if not j.isdigit():
            i = i + 1
            if i == 1:
               math = j
    if i == 1:
        y = x.rpartition(math)
        num1 = y[0]
        num2 = y[2]
        if  num1.isdigit() is False or num2.isdigit() is False:
            print("please enter a valid calculation")
            calculator()
        else:
            num1 = int(num1)
            num2 = int(num2)
            match math:
                case "+":
                    num3 = num1 + num2
                case "-":
                    num3 = num1 - num2
                case "*":
                    num3 = num1 * num2
                case "/":
                    num3 = num1 / num2
                case _:
                    print("please enter a valid calculation")
                    calculator()
            print(str(num1) + " " + str(math) + " " + str(num2) + " = " + str(num3))
    else:
        print("please enter a valid calculation")
        calculator()

def clear_screen():
    import os
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Other systems (Linux, macOS)
    else:
        os.system('clear')

clear_screen()
print("======= welcome to avi's calculator =======")
calculator()
while input('type "y" if you want to try again: ') =="y":
    clear_screen()
    print("======= welcome to avi's calculator =======")
    calculator()
print("======= Thank you for using avi's calculator =======")



