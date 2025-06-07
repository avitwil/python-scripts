def clear_screen(): #cleaning the screen in the terminal for a streamline look
    import os
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Other systems (Linux, macOS)
    else:
        os.system('clear')


def initial_calculator():
    x = input("enter your calculation: ")
    i = 0
    for j in x:  # checking every char in the string for somthing that is not a digit
        if not j.isdigit():
            i = i + 1
            if i == 1:
                math = j
    if i == 1:  # checking that only one char is not a digit
        y = x.rpartition(math)  # converting the string in to a tuple containing three strings and the second value is the non digit
        num1 = y[0]
        num2 = y[2]
        if num1.isdigit() is False or num2.isdigit() is False:
            print("please enter a valid calculation")
            initial_calculator()
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
                    initial_calculator()
            clear_screen()
            print("======= welcome to avi's calculator =======")
            print(str(num1) + " " + str(math) + " " + str(num2) + " = " + str(num3) + '  continue calculating or type "c" to clear or type "e" to exit ')
            continue_calculator(num3)
    else:
        print("please enter a valid calculation")
        initial_calculator()



def continue_calculator(num1):
    user_input = input()
    math = user_input[0]
    num2 = user_input[1:]

    if not(math == "+" or math == "-" or math == "*" or math == "/"):

        if math == "c":
            initial_calculator()

        elif math == "e":
            print("======= Thank you for using avi's calculator =======")
            exit()

        else:
            print("please enter a valid calculation")
            continue_calculator(num1)

    elif num2.isdigit() is False:
        print("please enter a valid calculation")
        continue_calculator(num1)

    else:
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
                continue_calculator(num1)
        clear_screen()
        print("======= welcome to avi's calculator =======")
        print(str(num1) + " " + str(math) + " " + str(num2) + " = " + str(num3) + '  continue calculating or type "c" to clear or type "e" to exit ')
        continue_calculator(num3)





clear_screen()
print("======= welcome to avi's calculator =======")
initial_calculator()
