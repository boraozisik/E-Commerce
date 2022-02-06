import time


class User():
    is_online = False
    ordered_products = []
    favorite_products = []

    def __init__(self, name, surname, date_of_birth, username, password, email, home_address, work_address, credit_card):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.username = username
        self.password = password
        self.email = email
        self.home_address = home_address
        self.work_address = work_address
        self.credit_card = credit_card

    def login(self):
        if self.is_online:
            print("You have already logged in!!!")
        else :
            username = input("Enter your username:")
            password = input("Enter your password")
            print("Information is checking...")
            time.sleep(3)

            if username == self.username and password == self.password:
                self.is_online = True
                print("Login successful...")
            else:
                print("Wrong username or password!!!")

    def logout(self):
        if not self.is_online:
            print("You have already logged out!!!")
        else:
            self.is_online = False
            print("Logged out!!")

    def order_product(self, product, number_of_products):
        if self.is_online == False:
            print("You must login first!")

        else:

            while True:
                card_number = input("Enter your credit card's number:")
                security_code = input("Enter your credit card's security code:")
                print("Your card information is checking...")
                time.sleep(3)
                if card_number != self.credit_card.card_number:
                    print("Wrong card number!")

                elif security_code != self.credit_card.security_code:
                    print("Wrong security code")


                else:
                    print("Your card information is true, going to the ordering step...")
                    time.sleep(3)
                    if self.credit_card.balance < (product.price * number_of_products) or self.credit_card.balance <= 0:
                        print("Insufficient balance!!!")
                        break
                    elif product.product_stock <= 0 or product.product_stock < number_of_products:
                        print("We have not enough of this product")
                        print("Stocks for this product ==> {} ".format(product.product_stock))
                    else:
                        self.ordered_products.append(product)
                        product.product_stock -= number_of_products
                        print("Your order has been received...")
                        print("*******************************")

                        answer = input("Do you want to add this product to your favorites? (yes/no)")
                        if answer == "yes":
                            print("Added to favorites")
                            self.add_to_favorite_products(product)
                            break
                        else:
                            break

    def see_ordered_products(self):
        if self.is_online == False:
            print("You must login first!")
        else:
            print("User's Ordered Products")
            print(" ")
            for i in self.ordered_products:
                print(i.name)

    def cancel_order(self, product):
        if self.is_online == False:
            print("You must login first!")
        else:
            self.ordered_products.remove(product)

    def add_to_favorite_products(self, product):
        if self.is_online == False:
            print("You must login first!")
        else:
            self.favorite_products.append(product)

    def see_favorite_products(self):
        if self.is_online == False:
            print("You must login first!")
        else:
            print("User's Favorite Products")
            print(" ")
            for i in self.favorite_products:
                print(i.name)

    def return_product(self, product):
        if self.is_online == False:
            print("You must login first!")
        else:
            self.ordered_products.remove(product)
            self.favorite_products.remove(product)
            self.credit_card.balance += product.price


class Product():

    def __init__(self, name, price, category, product_stock, description):
        self.name = name
        self.price = price
        self.category = category
        self.product_stock = product_stock
        self.description = description


class CreditCard():

    def __init__(self, card_number, security_code, balance):
        self.card_number = card_number
        self.security_code = security_code
        self.balance = balance


product_1 = Product("Suç ve Ceza", 40, "Book", 348, "An amazing book")
product_2 = Product("Iphone12", 14000, "Electronic", 175, "Useful cellphone")
product_3 = Product("Nescafe 2-1", 15, "Drink", 235, "No sugar happy life")
product_4 = Product("Pull and Bear Sweatshirt", 390, "Clothes", 420, "You will look fascinating")


credit_card_1 = CreditCard("1579129", "287", 360000)

user1 = User("Bora", "Özışık", "07.11.2000", "bora09", "12345", "bora@gg.com", "Aydın", "İzmir", credit_card_1)

user1.login()
user1.order_product(product_1,50)
user1.order_product(product_2,2)
user1.order_product(product_3,50)
user1.order_product(product_4,3)
user1.see_ordered_products()
print("***************")
user1.see_favorite_products()











