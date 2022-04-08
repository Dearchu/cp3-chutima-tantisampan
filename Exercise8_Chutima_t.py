username =input("username:")
password =input("password:")
if username == "dear" and password =="chu":
    print("--welcome to Dear Shop--")
    print("fruit")
    print("1. banana x1: 20 THB")
    print("2. Apple  x1: 40 THB")
    print("3. Orange x1: 30 THB")
    userselected1 =int(input("Please select number of fruit:"))
    if userselected1 >3:
        print("Invalid data")
    else:
        fruitnum = int(input("number of fruit:"))
        if userselected1 == 1:
            sum = 20 * fruitnum
            print("Total:",sum)
        elif userselected1 ==2:
            sum = 40 * fruitnum
            print("Total:" , sum)
        elif userselected1 ==3:
            sum = 30 * fruitnum
            print("Total:" , sum)
else:
    print("username or Password is not valid")
