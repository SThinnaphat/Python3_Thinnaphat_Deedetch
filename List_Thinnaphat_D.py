menuList = []
Sum = 0

def ShowBill():
    print("----My Food----")
    for i in range(len(menuList)):
        print(menuList[i])

while True:
    menu = input("Please enter your menu: ")
    if menu.lower() == "exit":
        break
    else:
        menuprice = int(input("Enter the price"))
        menuList.append([menu,menuprice])

print(ShowBill())
for y in range(len(menuList)):
    Sum += menuList[y][1]
print("The total price is : ",Sum)
