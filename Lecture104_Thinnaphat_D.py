class Customer:
    name = ""
    lastname = ""
    age = 0 #default value

    def addCart(self):
        print("Added to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Thinnaphat"
customer1.lastname = "Deedetch"
customer1.addCart()
customer2 = Customer()
customer2.name = "Pataratorn"
customer2.lastname = "T"
customer2.addCart()
customer3 = Customer()
customer3.name = "Kochaporn"
customer3.lastname = "K"
customer3.addCart()
customer4 = Customer()
customer4.name = "Baramee"
customer4.lastname = "K"
customer4.addCart()

