def check_num(num):

    while not num.isdigit():
        print(num + "  is not a number")
        num = input("enter a number: ")

    num = int(num)
    return num

def check_math(math):

    while not (math == "+" or math == "-" or math == "*" or math == "/"):
        print("enter only + or - or / or * ")
        math = input("enter math operation  ONLY ( + - / * ): ")

    return math

def clear_screen():
    import os
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Other systems (Linux, macOS)
    else:
        os.system('clear')

yn = "y"
clear_screen()

while yn == "y":
    print("========= Python calculator by Avi Twil ==========")
    user_input = input("enter you caculation:  ")
    split_input = user_input.split(" ")

    while not len(split_input) == 3:
        user_input = input("enter you caculation:  ")
        split_input = user_input.split(" ")

    num1 = split_input[0]
    num2 = split_input[2]
    math = split_input[1]
    num1 = check_num(num1)
    math = check_math(math)
    num2 = check_num(num2)

    match math:
        case "+":
            num3 = num1 + num2
        case "-":
            num3 = num1 - num2
        case "*":
            num3 = num1 * num2
        case "/":
            num3 = num1 / num2

    print(str(num1) +" " + str(math) + " " + str(num2) + " = " + str(num3))
    yn = input("try again ? (y/n): ")
    clear_screen()

