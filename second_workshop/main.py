"""
5/10/2024 - Advanced Programming Workshop #2

This program is an electronic store that displays products for purchase and allows
user registration and login, it is an update to improve the service.

Author: [Your Name]
"""

from abc import ABC, abstractmethod


class StoreUser:
    """
    Class representing a user of the store.

    Attributes:
        username (str): The username for authentication.
        password (str): The user's password.
        name (str): The full name of the user.
        role (str): The role of the user, either 'admin' or 'user'.
    """

    def __init__(self, username, password, name, role="user"):
        self.username = username
        self.password = password
        self.name = name
        self.role = role

    def is_admin(self):
        """Returns True if the user is an admin, otherwise False."""
        return self.role == "admin"


class Admin(StoreUser):
    """Class representing an admin user."""

    def __init__(self, username, password, name):
        super().__init__(username, password, name, role="admin")


class Customer(StoreUser):
    """Class representing a regular customer."""

    def __init__(self, username, password, name):
        super().__init__(username, password, name, role="user")


class AbstractStore(ABC):
    """Abstract class defining the interface for a store."""
    @abstractmethod
    def display_main_menu(self):
        pass


class Store(AbstractStore):
    """
    Concrete class that implements the store functionality.

    Attributes:
        categories (dict): Available product categories.
        products (dict): Products organized by category.
        cart (list): The shopping cart for storing selected products.
        users (list): List of registered users.
        sales (list): List of completed sales transactions.
    """

    def __init__(self):
        self.categories = {1: "Phones", 2: "Laptops",
                           3: "Tablets", 4: "Accessories"}
        self.products = {
            "Phones": {1: {"name": "iPhone 15", "price": 1200, "brand": "Apple"}},
            "Laptops": {1: {"name": "MacBook Air", "price": 1500, "brand": "Apple"}},
        }
        self.cart = []
        self.users = []
        self.sales = []

    def register_user(self, username, password, name, role):
        """Registers a new user in the store."""
        if role == "admin":
            self.users.append(Admin(username, password, name))
        else:
            self.users.append(Customer(username, password, name))
        print("User registered successfully.")

    def login_user(self, username, password):
        """Authenticates and logs in a user."""
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Welcome, {user.name}!")
                return user
        print("Invalid credentials.")
        return None

    def display_main_menu(self):
        """Displays the main menu options."""
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Checkout")
        print("4. View cart")
        print("5. Search by brand")
        print("6. Search by price range")
        print("7. Exit")

    def add_product_to_cart(self, category, product_id):
        """Adds a product to the shopping cart."""
        if category in self.products and product_id in self.products[category]:
            self.cart.append(self.products[category][product_id])
            print(
                f"{self.products[category][product_id]['name']} added to cart.")
        else:
            print("Invalid product selection.")

    def view_cart(self):
        """Displays the products currently in the shopping cart."""
        if not self.cart:
            print("Cart is empty.")
        else:
            for item in self.cart:
                print(f"{item['name']} - ${item['price']}")

    def checkout(self):
        """Processes the final sale transaction."""
        if not self.cart:
            print("Cart is empty. Cannot proceed to checkout.")
            return
        total = sum(item["price"] for item in self.cart)
        print(f"Total: ${total}")
        self.sales.append({"total": total, "items": self.cart})
        self.cart.clear()
        print("Checkout complete.")

    def search_by_brand(self, brand):
        """Searches for products by brand name."""
        found_products = [item for category in self.products.values(
        ) for item in category.values() if item["brand"].lower() == brand.lower()]
        if found_products:
            for item in found_products:
                print(f"{item['name']} - ${item['price']}")
        else:
            print("No products found for this brand.")

    def search_by_price(self, min_price, max_price):
        """Searches for products within a specified price range."""
        found_products = [item for category in self.products.values(
        ) for item in category.values() if min_price <= item["price"] <= max_price]
        if found_products:
            for item in found_products:
                print(f"{item['name']} - ${item['price']}")
        else:
            print("No products found in this price range.")


# Main Application
store = Store()
print("Welcome to the Electronic Store!")
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter full name: ")
        role = input("Enter role (admin/user): ")
        store.register_user(username, password, name, role)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = store.login_user(username, password)
    elif choice == "3":
        print("Exiting store. Goodbye!")
        break
    else:
        print("Invalid selection. Try again.")
