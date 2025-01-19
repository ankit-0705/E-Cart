class App:
    login_counter=0
    def __init__(self,name=None,email=None,phone_number=None,password=None,administrator_code=None):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.__password=password
        self.__administrator_code=administrator_code
        print("App has been started!!!")
        self.authorization_option()

    def admin_code_getter(self):
        return self.__administrator_code

    def authorization_option(self):
        user_choice = input("Want to login or register: ")
        if user_choice == "login":
            self.login()
        elif user_choice == "register":
            self.register()
        else:
            print("Enter a valid choice.")
            self.authorization_option()

    def login(self):
        if App.login_counter<3:
            login_choice = input("Want to login through email or phone number: ")
            if login_choice.lower() == "email":
                user_email = input("Enter your email: ")
                user_password = input("Enter your password: ")
                if self.email == user_email and self.__password == user_password:
                    print("Congratulation on successful login.")
                    ProfessionOption(self.name,self.email,self.phone_number,self.admin_code_getter())
                    App.login_counter=0
                    return
                else:
                    print("Try again with correct credentials.")
                    App.login_counter += 1
                    self.login()
            elif login_choice.lower() == "phone number":
                user_pn = int(input("Enter your phone number: "))
                user_password = input("Enter your password")
                if self.phone_number == user_pn and self.__password == user_password:
                    print("Congratulation on successful login.")
                    ProfessionOption(self.name,self.email,self.phone_number,self.admin_code_getter())
                    return
                else:
                    print("Try again with correct credentials.")
                    App.login_counter += 1
                    self.login()
            else:
                print("Enter a valid choice.")
                self.login()
        else:
            print("Are you sure, you have a account?")
            redirect_choice=input("Wanna register?(Yes/No)")
            if redirect_choice.lower() == "yes":
                self.register()
                App.login_counter=0
            else:
                print("It's your last chance.")
                App.login_counter=1
                self.login()

    def register(self):
        self.name=input("Enter your name: ")
        self.email=input("Enter your email: ")
        self.__password=input("Enter your password: ")
        self.phone_number=int(input("Enter you phone number: "))
        self.__administrator_code=int(input("Enter your administrator code: "))
        print("Congratulation registration complete successfully.")
        self.login()
        App.login_counter=0

class ProfessionOption(App):
    def __init__(self,name,email,phone_number,security_code):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.security_code=security_code
        user_choice = input("Are you a client or administrator?: ")
        if user_choice.lower() == "client":
            Client(self.name, self.email, self.phone_number)
        elif user_choice == "administrator":
            administrator_code = int((input("Enter your administrator code: ")))
            if administrator_code == self.security_code:
                Administrator(self.name,self.email,self.phone_number,self.security_code)
            else:
                print("Invalid Administrator code.")
                ProfessionOption(self.name,self.email,self.phone_number,self.security_code)
        else:
            print("Invalid choice.")
            ProfessionOption(self.name,self.email,self.phone_number,self.security_code)

class Administrator(ProfessionOption):
    def __init__(self,name,email,phone_number,security_code):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.security_code=security_code
        print("Welcome to the Administrator section!")
        Product(self.name,self.email,self.phone_number,self.security_code)

class Product(Administrator):
    products={} #{name:[price(Rs),quantity(Kg)]}(Blueprint of dictionary containing info about products)
    def __init__(self,name,email,phone_number,security_code,pname=None,price=None,quantity=None):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.security_code=security_code
        self.pname=pname
        self.price=price
        self.quantity=quantity
        print("Welcome to the Product section.")
        self.storing_products()

    def storing_products(self):
        info_list=[]
        self.pname=input("Enter the name of the product: ")
        self.price=int(input("Enter its price(Rs): "))
        self.quantity=int(input("Enter its quantity(Kg): "))
        info_list.append(self.price)
        info_list.append(self.quantity)
        Product.products[self.pname]=info_list
        user_choice=input("Want to add more products?(Yes/No): ").lower()
        if user_choice == "yes":
            self.storing_products()
        elif user_choice == "no":
            print(Product.products)
            self.administrator_action()
        else:
            print("Enter a valid choice.")
            self.storing_products()

    def administrator_action(self):
        print("1.Update Price\n2.Update Quantity\n3.Go to Client Section\n4.Exit")
        administrator_choice = int(input("Enter your choice(1/2/3): "))
        if administrator_choice == 1:
            self.updating_price()
        elif administrator_choice == 2:
            self.updating_quantity()
        elif administrator_choice==3:
            ProfessionOption(self.name,self.email,self.phone_number,self.security_code)
        elif administrator_choice == 4:
            exit()
        else:
            print("Enter a valid choice.")
            self.administrator_action()

    def updating_price(self):
        product_name=input("Whose price you want to update: ")
        if product_name in Product.products:
            new_price=int(input("Enter the new price: "))
            if new_price>=0:
                Product.products[product_name][0]=new_price
                print(f"New price({new_price}) has been set for {product_name}")
                self.administrator_action()
            else:
                print("Enter a valid price.")
                self.updating_price()
        else:
            u=input("Are you sure about this product(Yes/No)?Bcz it is not in the stock.")
            if u.lower()=='yes':
                self.updating_price()
            elif u.lower()=='no':
                self.administrator_action()
            else:
                print("Enter a valid choice.")
                self.updating_price()

    def updating_quantity(self):
        product_name = input("Whose quantity you want to update: ")
        if product_name in Product.products:
            new_quantity = int(input("Enter the new quantity: "))
            if new_quantity >= 0:
                Product.products[product_name][1] = new_quantity
                print(f"New quantity({new_quantity}) has been set for {product_name}")
                self.administrator_action()
            else:
                print("Enter a valid quantity.")
                self.updating_quantity()
        else:
            u = input("Are you sure about this product(Yes/No)?Bcz it is not in the stock.")
            if u.lower() == 'yes':
                self.updating_quantity()
            elif u.lower() == 'no':
                self.administrator_action()
            else:
                print("Enter a valid choice.")
                self.updating_quantity()


class Client(ProfessionOption):
    def __init__(self, name, email, phone_number):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        print("Welcome to the Client section!")
        self.client_action()

    def client_action(self):
        print("1.Go to Profile\n2.Go to Cart\n3.Exit")
        client_choice = int(input("Enter your choice: "))
        if client_choice == 1:
            Customer(self.name, self.email, self.phone_number)
        elif client_choice == 2:
            CartOrders(Product.products)
        elif client_choice == 3:
            exit()
        else:
            print("Enter a valid choice.")
            self.client_action()


class Customer(Client):
    def __init__(self,name,email,phone_number):
        print("User profile info is given below: ")
        print("Name: ",name)
        print("Email: ",email)
        print("Phone Number: ",phone_number)

class CartOrders(Product):
    def __init__(self,products=None):
        self.products=products
        self.cart={}
        print("Welcome to Cart section.")
        self.cart_options()

    def cart_options(self):
        print("1.Add Product\n2.Remove Product\n3.Total Price\n4.Exit")
        options=int(input("Enter your choice(): "))
        if options==1:
            self.add_product()
        elif options==2:
            self.remove_product()
        elif options==3:
            self.total_price()
        elif options==4:
            exit()
        else:
            self.cart_options()

    def add_product(self):
        info_lst=[]
        product_name=input("Which product you want to add in your cart? ")
        if product_name in self.products:
            product_quantity=int(input("Enter the quantity of product: "))
            if product_quantity<=self.products[product_name][1]:
                info_lst.append(self.products[product_name][0])
                info_lst.append(product_quantity)
                self.cart[product_name]=info_lst
                print(f"{product_quantity} unit of {product_name} is successfully added to the cart.")
                user_choice = input("Want to add more product in your cart(Yes/No): ").lower()
                if user_choice == 'yes':
                    self.add_product()
                elif user_choice == 'no':
                    print("Your current cart.")
                    print(self.cart)
                    self.cart_options()
                else:
                    print("Enter a valid choice.")
                    self.cart_options()
            else:
                print("Sorry for inconvenience,but this much amount is not available.")
                print(f"You can only order {self.products[product_name][1]} units.")
        else:
            print("Sorry for inconvenience,but it is out of stock now.")
            self.cart_options()

    def remove_product(self):
        product_name = input("Which product you want to remove from your cart? ")
        if product_name in self.cart:
            print(f"{product_name} has been successfully removed from your cart.")
            self.cart.pop(product_name)
            user_choice = input("Want to remove more product from your cart(Yes/No): ").lower()
            if user_choice == 'yes':
                self.remove_product()
            elif user_choice == 'no':
                print("Your current cart.")
                print(self.cart)
                self.cart_options()
            else:
                print("Enter a valid choice.")
                self.cart_options()
        else:
            print("Already not present inside your cart.")
            self.cart_options()

    def modify_quantity(self):
        product_name = input("Whose quantity you want to alter? ")
        if product_name in self.cart:
            new_quantity=int(input("Enter new quantity: "))
            self.cart[product_name][1]=new_quantity
            print(f"{product_name} quantity has been changed successfully.")
            user_choice = input("Want to add more product in your cart(Yes/No): ").lower()
            if user_choice == 'yes':
                self.modify_quantity()
            elif user_choice == 'no':
                print("Your current cart.")
                print(self.cart)
                self.cart_options()
            else:
                print("Enter a valid choice.")
                self.cart_options()
        else:
            print("This item is not present in your cart.")
            self.cart_options()

    def total_price(self):
        total_amount=sum({price*units for price,units in self.cart.values()})
        print("Items in your cart are:")
        print(self.cart)
        print("Their total is:",total_amount)
        self.cart_options()

App()