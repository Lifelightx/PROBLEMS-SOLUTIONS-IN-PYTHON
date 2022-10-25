while True:
    num1 = int(input("Enter a number: "))
    opr = input("Enter a operator: ")
    num2 = int(input("Enter a number: "))
    
    if num1 == 56 and num2 == 9 and opr == "+":
        print("77")
    elif num1 == 45 and num2 == 3 and opr == "*":
        print("555")
    elif num1 == 56 and num2 == 6 and opr == "/":
        print("4")
    elif opr == "+":
        print(num1+num2)
    elif opr == "-":
        print(num1-num2)
    elif opr == "*":
        print(num1*num2)
    elif opr == "/":
        print(num1/num2)
    elif opr == "**":
        print(num1**num2)
    else:
        print("Enter a valid operator.")

