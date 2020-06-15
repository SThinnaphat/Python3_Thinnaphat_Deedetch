username = input("Enter your username : ")
password = input("Enter your password : ")
if username == "SThinnaphat" and password == "123456":
    print("Access granted!")
    print("--------------------")
    print("Welcome to the shop")
    print("--------------------")
    print("Select your items")
    print("Apple 10 Bahts")
    print("Banana 5 Bahts")
    print("Candy 2 Bahts")
    selected = int(input("Select 1 for Apple, Select2 for Banana, Select 3 for candy, Select4 for all : "))
    if selected == 1:
        apples = int(input("How many apples do you want?: "))
        print("Total price is", 10*apples)
        print("Thank you")
    elif selected == 2:
        banana = int(input("How many bananas do you want?: "))
        print("Total price is", 5 * banana)
        print("Thank you")
    elif selected == 3 :
        candy = int(input("How many candies do you want?: "))
        print("Total price is", 2 * candy)
        print("Thank you")
    else :
        apples = int(input("How many apples do you want?: "))
        banana = int(input("How many bananas do you want?: "))
        candy = int(input("How many candies do you want?: "))
        print("Total price is", (5 * banana)+(10*apples)+(2*candy), "Bahts")
        print("Thank you")
else:
    print("Access denied")


