def login():
    username = input("Enter your username ")
    password = input("Enter your password ")
    if username == "SThinnaphat" and password == "123456":
        print("Access Granted")
        print(showMenu())
    else:
        print("Access Denied")
        print(login())
def showMenu():
    print("Welcome to the shop")
    print("Select 1 for VAT calculation")
    print("Select 2 for price calculation")
    print(Select())
def Select():
    select = int(input("Enter your selection "))
    if select == 1:
        print(VATCalculation())
    elif select == 2 :
        print(PriceCalculation())
def VATCalculation():
    price = float(input("Enter the total price "))
    result = price+(price*0.07)
    return result
def PriceCalculation():
    firstItem = float(input("Enter the first price "))
    SecondItem = float(input("Enter the second price "))
    calculate = firstItem + SecondItem
    return calculate

print(login())
