nameInput = input("Please Eneter your Username:")
passInput = input("Please Eneter your Password:")
if nameInput == "Nile" and passInput == "123#":
    print ("Welcome to our store!!!")
    print('-------------------------')
    print('Please Selected our menu')
    print('1.Roasted chicken : 150$')
    print('2.Fried Pork      : 50$')
    print('3. Pizza          : 350$')
    print('-------------------------')
    userOrder = int(input('>>>:'))

    if userOrder == 1:
        price = 150
        print("Please Enter Amount:")
        amountItem = int(input(">>>:"))
    elif userOrder == 2:
        price = 50
        print("Please Enter Amount:")
        amountItem = int(input(">>>:"))
    elif userOrder == 3:
        price = 350
        print("Please Enter Amount:")
        amountItem = int(input(">>>:"))

    print('-------------------------')
    print ("Here's your Total Price:")
    print (amountItem * price , "$")
    print ("Thanks for using our store!")
    print('-------------------------')