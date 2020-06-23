systemmenu = {"FriedChicken":40,"FriedPork":30,"FriedRice":25,"FriedVegetables":60}
menuList = []
Sum = 0

def ShowBill():
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])

while True:
    menu = input("Please enter your menu: ")
    if menu.lower() == "exit":
        break
    else:
        menuList.append([menu,systemmenu[menu]])

print(ShowBill())
for y in range(len(menuList)):
    Sum += menuList[y][1]
print("The total price is : ",Sum)
