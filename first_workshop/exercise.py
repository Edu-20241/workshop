class Device:
    """
    Represents an electronic device available in the store.

    Attributes:
        name (str): The name of the device (e.g., "iPhone 13").
        category (str): The category to which the device belongs (e.g., "Phones").
        price (float): The price of the device in USD.
        brand (str): The brand of the device (e.g., "Apple").
        warranty (int): The warranty period of the device in years.
    """

    def __init__(self, name, category, price, brand, warranty):
        self.name = name
        self.category = category
        self.price = price
        self.brand = brand
        self.warranty = warranty


class ShoppingCart:
    """
    Represents a shopping cart that stores devices selected by the user.

    Attributes:
        items (list): A list that holds the devices added to the cart.
    """

    def __init__(self):
        self.items = []

    def add_item(self, device):
        """
        Adds a device to the shopping cart.

        Args:
            device (Device): The device to add to the cart.
        """
        self.items.append(device)

    def show_cart(self):
        """
        Displays the contents of the shopping cart. If the cart is empty, it notifies the user.
        """
        if not self.items:
            print("Your cart is empty.")
        else:
            for device in self.items:
                print(
                    f"{device.name} - ${device.price} (Warranty: {device.warranty} years)")

    def checkout(self):
        """
        Proceeds with the checkout process by prompting the user for their personal details.
        Offers the user an option to purchase extended warranty.
        Displays a confirmation message with the total cost and delivery details if the cart is not empty.
        """
        if not self.items:
            print("Your cart is empty. Add items to proceed.")
            return

        total_price = 0
        print("\n--- Checkout ---")
        self.show_cart()

        extended_warranty_total = 0
        for device in self.items:
            extend_warranty = input(
                f"Would you like to extend the warranty for {device.name} (current warranty: {device.warranty} years)? (yes/no): ").lower()
            if extend_warranty == "yes":
                extra_years = int(
                    input("How many additional years would you like to add? "))

                cost_per_year = 0.05 * device.price
                warranty_cost = cost_per_year * extra_years
                extended_warranty_total += warranty_cost
                device.warranty += extra_years
                print(
                    f"Warranty for {device.name} extended by {extra_years} years. Extra cost: ${warranty_cost:.2f}")

        for device in self.items:
            total_price += device.price

        total_price += extended_warranty_total

        last_name = input("Enter your last name: ")
        address = input("Enter your address: ")
        student_code = input("Enter your student code: ")

        print(
            f"\nTotal price (including warranty extensions): ${total_price:.2f}")
        print(
            f"Order confirmed for {last_name}. It will be delivered to {address}.")


class Store:
    """
    Represents the store that holds a catalog of devices and interacts with users through the CLI.

    Attributes:
        categories (dict): A dictionary with categories as keys and lists of devices as values.
        cart (ShoppingCart): The shopping cart instance to handle user selections.
    """

    def __init__(self):
        self.categories = {"Phones": [], "Laptops": [], "Tablets": []}
        self.cart = ShoppingCart()

    def add_device(self, device):
        """
        Adds a device to the store under its respective category.

        Args:
            device (Device): The device to add to the store.
        """
        if device.category in self.categories:
            self.categories[device.category].append(device)
        else:
            print(f"Category {device.category} not available.")

    def show_categories(self):
        """
        Displays the available categories in the store.
        """
        print("Available categories:")
        for category in self.categories:
            print(category)

    def show_devices_by_category(self, category):
        """
        Displays the devices available in a selected category.

        Args:
            category (str): The category chosen by the user (e.g., "Phones").
        """
        if category in self.categories:
            if not self.categories[category]:
                print(f"No devices available in {category}.")
            else:
                print(f"Devices in {category}:")
                for device in self.categories[category]:
                    print(
                        f"{device.name} - ${device.price} ({device.brand}), Warranty: {device.warranty} years")
        else:
            print(f"Category {category} not found.")

    def filter_devices_by_brand(self, category, brand):
        """
        Filters and displays devices in a category by brand.

        Args:
            category (str): The category to filter devices from.
            brand (str): The brand of devices to filter by (e.g., "Apple").
        """
        if category in self.categories:
            filtered_devices = [
                device for device in self.categories[category] if device.brand == brand]
            if not filtered_devices:
                print(f"No devices found for brand {brand} in {category}.")
            else:
                print(f"Devices in {category} by {brand}:")
                for device in filtered_devices:
                    print(
                        f"{device.name} - ${device.price} (Warranty: {device.warranty} years)")
        else:
            print(f"Category {category} not found.")

    def filter_devices_by_price(self, category, min_price, max_price):
        """
        Filters and displays devices in a category by a given price range.

        Args:
            category (str): The category to filter devices from.
            min_price (float): The minimum price for the filter.
            max_price (float): The maximum price for the filter.
        """
        if category in self.categories:
            filtered_devices = [
                device for device in self.categories[category] if min_price <= device.price <= max_price]
            if not filtered_devices:
                print(
                    f"No devices found in the price range ${min_price} - ${max_price}.")
            else:
                print(
                    f"Devices in {category} within price range ${min_price} - ${max_price}:")
                for device in filtered_devices:
                    print(
                        f"{device.name} - ${device.price} ({device.brand}), Warranty: {device.warranty} years")
        else:
            print(f"Category {category} not found.")

    def show_warranty_ranges(self):
        """
        Displays the warranty ranges for different brands in the store.
        """
        print("\nWarranty Ranges by Brand:")
        warranty_ranges = {
            "Apple": "2-3 years",
            "Samsung": "1-2 years",
            "Huawei": "1-2 years",
            "Xiaomi": "1 year",
            "Oppo": "1 year",
            "Honor": "1 year",
            "Dell": "2-3 years",
            "HP": "2 years",
            "Asus": "2 years",
            "Lenovo": "2-3 years"
        }
        for brand, warranty in warranty_ranges.items():
            print(f"{brand}: {warranty}")

    def ask_students(self):
        """
        Simulates asking 15 students about their device preferences. The responses are stored in a list.

        Returns:
            list: A list of tuples containing student preferences for device types and features.
        """
        student_wants = []
        for i in range(1, 16):
            print(f"\nSurvey for Student {i}")
            device_type = input(
                "What kind of electronic device would you like to see in the catalog? ")
            device_preference = input(
                "Any specific features or brands you're looking for? ")
            student_wants.append((device_type, device_preference))
        return student_wants

    def create_user_stories(self, student_wants):
        """
        Generates user stories based on the preferences provided by students.

        Args:
            student_wants (list): A list of tuples containing student preferences.
        """
        print("\nUser Stories Based on Survey Results:")
        for i, (device_type, preference) in enumerate(student_wants, 1):
            print(
                f"Story {i}: As a student, I want to see {device_type} with {preference}, so I can make informed decisions.")


def main():
    """
    Main function that simulates a command-line interaction with the user.
    It allows the user to view categories, filter devices by brand or price, add devices to the cart, and checkout.
    """
    store = Store()

    store.add_device(Device("iPhone 13", "Phones", 999, "Apple", 2))
    store.add_device(Device("Galaxy S21", "Phones", 799, "Samsung", 1))
    store.add_device(Device("Huawei P50", "Phones", 649, "Huawei", 1))
    store.add_device(Device("Xiaomi Mi 11", "Phones", 749, "Xiaomi", 1))
    store.add_device(Device("Oppo Find X3", "Phones", 899, "Oppo", 1))
    store.add_device(Device("Honor 50", "Phones", 499, "Honor", 1))

    store.add_device(Device("MacBook Pro", "Laptops", 1999, "Apple", 3))
    store.add_device(Device("Dell XPS 13", "Laptops", 1499, "Dell", 2))
    store.add_device(Device("HP Spectre x360", "Laptops", 1399, "HP", 2))
    store.add_device(Device("Asus ZenBook", "Laptops", 1299, "Asus", 2))
    store.add_device(Device("Lenovo ThinkPad X1",
                     "Laptops", 1799, "Lenovo", 3))

    store.add_device(Device("iPad", "Tablets", 499, "Apple", 2))
    store.add_device(Device("Samsung Galaxy Tab S7",
                     "Tablets", 649, "Samsung", 1))
    store.add_device(Device("Huawei MatePad Pro", "Tablets", 549, "Huawei", 1))
    store.add_device(Device("Xiaomi Pad 5", "Tablets", 499, "Xiaomi", 1))

    student_wants = store.ask_students()

    store.create_user_stories(student_wants)

    store.show_categories()
    category = input("Select a category to view devices: ")
    store.show_devices_by_category(category)

    filter_by_brand = input(
        "Do you want to filter by brand? (yes/no): ").lower()
    if filter_by_brand == "yes":
        brand = input("Enter the brand to filter by: ")
        store.filter_devices_by_brand(category, brand)
    else:
        filter_by_price = input(
            "Do you want to filter by price range? (yes/no): ").lower()
        if filter_by_price == "yes":
            min_price = int(input("Enter the minimum price: "))
            max_price = int(input("Enter the maximum price: "))
            store.filter_devices_by_price(category, min_price, max_price)

    store.show_warranty_ranges()

    device_name = input("Select a device to add to the cart: ")
    for device in store.categories.get(category, []):
        if device.name == device_name:
            store.cart.add_item(device)
            break

    store.cart.checkout()


if __name__ == "__main__":
    main()
