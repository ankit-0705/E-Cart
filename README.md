# E-Cart
E-Commerce System with User and Administrator Roles
This project is a Python-based e-commerce system that supports both customer and administrator functionalities, allowing users to register, log in, view products, add them to a cart, and make purchases. Administrators can manage products by adding, updating prices, and modifying stock quantities.

Features
User Registration & Login: Users can either register a new account or log in using their email or phone number.
Client Section:
View Profile: Users can view their personal profile information.
Cart Management: Users can add products to their cart, remove items, modify quantities, and view the total price of items in their cart.
Administrator Section:
Product Management: Administrators can add new products to the system, update product prices, and modify quantities available in stock.
Admin Verification: Only authenticated administrators with the correct administrator code can access and manage product details.
Product Catalog: Admins can add products with name, price, and quantity, and manage them accordingly.
Cart and Checkout System: Clients can interact with the products by adding them to their cart, modifying quantities, and checking out with a summary of their total price.
How to Use
Start the Application: When the program starts, users are prompted to either log in or register. If registering, they must provide their name, email, phone number, password, and administrator code (for admins).
Login Process: After registration or during subsequent logins, users can authenticate themselves via email or phone number. The system allows a maximum of 3 login attempts.
Administrator Access: After successful login, administrators are prompted to enter an administrator code. Only those with the correct code can manage product details.
Product Interaction: Administrators can manage the product catalog by adding new items, updating prices, or altering available stock quantities.
Client Actions: Clients can add items to their cart, modify quantities, remove items, and calculate the total price for their order.
Tech Stack
Python (No external libraries required)
