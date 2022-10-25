#YOU HAVE A GIVEN NUMBER AND TAKE A INPUT FROM USER AND GUESS IT YOU HAVE ONLY 9 CHANCES.


n = 18


case = 9
for i in range(case):
    num = int(input("Enter a number: "))

    

    if num ==n:
        print("Wow. 🤗 you guess the right number.")
        break
    elif num>15 and num<22:
        print("you are too close to the number🧐 ")
    elif num>25:
        print("you entered a greater number🧐")
    if n < num:
        print("Enter a smaller number🧐")
    elif n>num:
        print("Enter a larger number🧐")
else:
    print("Game Over 😖...........")
