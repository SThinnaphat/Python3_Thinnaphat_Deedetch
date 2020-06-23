systemmenu = {"friedchicken":40,"friedpork":30,"friedrice":25,"friedvegetables":60}
menuList = []
Sum = 0

def ShowBill():
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])

while True:
    menu= input("Please enter your menu: ").lower()
    if menu.lower() == "exit":
        break
    else:
        menuList.append([menu,systemmenu[menu]])

print(ShowBill())
for y in range(len(menuList)):
    Sum += menuList[y][1]
print("The total price is : ",Sum)
