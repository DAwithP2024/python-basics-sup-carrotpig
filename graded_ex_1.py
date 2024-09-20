# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    for idx, product in enumerate(sorted_products, 1):
        print(f"{idx}. {product[0]} - ${product[1]}")
    return sorted_products

def display_products(products_list):
    for idx, product in enumerate(products_list, 1):
        print(f"{idx}. {product[0]} - ${product[1]}")

def display_categories():
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))
    print(f"Added {quantity} of {product} to cart.")

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        total_cost = sum(int(item[1]) * int(item[0][1]) for item in cart)
        for item in cart:
            print(f"{item[1]} of {item[0]}")
        print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Items purchased:")
    for item in cart:
        print(f"{item[1]} of {item[0]}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    names = name.split()
    if len(names) == 2 and all(part.isalpha() for part in names):
        return True
    return False

def validate_email(email):
    if "@" in email:
        return True
    return False

def main():
    name = input("Enter your name: ")
    while not validate_name(name):
        name = input("Please enter a valid name (both first name and last name, alphabets only): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        email = input("Please enter a valid email address: ")

    print("Welcome to the Online Shopping Store!")
    print("Categories available:")
    display_categories()

    cart = []
    while True:
        choice = input("Enter the category number you would like to explore or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            category_index = int(choice) - 1
            selected_category = list(products.keys())[category_index]
            print(f"Products available in {selected_category}:")
            display_products(products[selected_category])
            
            while True:
                option = input("Select an option: 1. Select a product to buy, 2. Sort the products, 3. Go back to category selection, 4. Finish shopping: ")
                
                if option == '1':
                    product_choice = int(input("Enter the product number you want to buy: "))
                    quantity = int(input("Enter the quantity: "))
                    selected_product = products[selected_category][product_choice - 1]
                    add_to_cart(cart, selected_product, quantity) 
                
                elif option == '2':
                    sort_order = int(input("Enter 1 for ascending order or 2 for descending order: "))
                    display_sorted_products(products[selected_category], sort_order)
                
                elif option == '3':
                    break
                
                elif option == '4':
                    print("Your cart:")
                    display_cart(cart)
                    total_cost = sum(int(item[1]) * int(item[0][1]) for item in cart)  
                    if cart:
                        address = input("Enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    break
                
                else:
                    print("Invalid option. Please try again.")
        
        except (ValueError, IndexError):
            print("Invalid category number. Please try again.")


if __name__ == "__main__":
    main()
