menuList = []
priceList = []
Sum = 0

def ShowBill():
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
    print("The total price is : ",Sum)


while True:
    menu = input("Please enter your menu: ")
    if menu.lower() == "exit":
        break
    else:
        menuprice = int(input("Enter the price"))
        Sum += menuprice
        menuList.append(menu)
        priceList.append(menuprice)


print(ShowBill())