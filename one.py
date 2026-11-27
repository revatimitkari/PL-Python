print("simple calculator")
try:
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. power")
    print("6. modulus")
    choice = input("enter your choice: ")
     if choice == "1":
        print("answer =", num1 + num2)
    elif choice == "2":
        print("answer =", num1 - num2)
    elif choice == "3":
        print("answer =", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            print("answer =", num1 / num2)
    elif choice == "5":
        print("answer =", num1 ** num2)
    elif choice == "6":
        if num2 == 0:
            print("cannot find modulus by zero.")
        else:
            print("answer =", num1 % num2)
    else:
        print("invalid choice.")
except:
    print("please enter numbers only.")
