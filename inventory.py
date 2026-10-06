import csv


class Inventory:
    def __init__(self, filename="products.csv"):
        self.filename = filename
        self.products = []
        self.load_products()

    def load_products(self):
        """Load products from the CSV file."""
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                self.products = list(reader)
        except FileNotFoundError:
            self.products = []

    def get_all_products(self):
        """Return all products."""
        return self.products

    def add_product(self, product):
        """Add a new product to the inventory."""

        if not product.get("PRODUCT_ID"):
            raise ValueError("Product ID is required.")

        if not product.get("PRODUCT_NAME"):
            raise ValueError("Product name is required.")

        if not product.get("PRODUCT_QUANTITY"):
            raise ValueError("Product quantity is required.")

        if not product.get("PRODUCT_PRICE"):
            raise ValueError("Product price is required.")

        if not product.get("MinStock"):
            raise ValueError("Minimum stock is required.")

        try:
            quantity = int(product["PRODUCT_QUANTITY"])
            price = float(product["PRODUCT_PRICE"])
            min_stock = int(product["MinStock"])
        except ValueError:
            raise ValueError("Quantity and minimum stock must be numbers, and price must be a number.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        if price < 0:
            raise ValueError("Product price cannot be negative.")

        if min_stock < 0:
            raise ValueError("Minimum stock cannot be negative.")

        # Prevent duplicate product IDs
        if self.search_product(product["PRODUCT_ID"]):
            raise ValueError("Product ID already exists.")

        self.products.append(product)
        self.save_products()

    def save_products(self):
        """Save inventory back to the CSV file."""
        if not self.products:
            return

        fieldnames = self.products[0].keys()

        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.products)

    def search_product(self, product_id):
        """Find a product by its ID."""
        for product in self.products:
            if product["PRODUCT_ID"] == str(product_id):
                return product
        return None

    def update_quantity(self, product_id, new_quantity):
        """Update the quantity of a product."""
        try:
            new_quantity = int(new_quantity)
        except ValueError:
            raise ValueError("Quantity must be a number.")

        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        product = self.search_product(product_id)

        if product:
            product["PRODUCT_QUANTITY"] = str(new_quantity)
            self.save_products()
            return True

        return False

    def remove_product(self, product_id):
        """Remove a product from the inventory."""
        product = self.search_product(product_id)

        if product:
            self.products.remove(product)
            self.save_products()
            return True

        return False

    def get_low_stock(self):
        """Return products whose quantity is at or below MinStock."""
        low_stock = []

        for product in self.products:
            try:
                quantity = int(product["PRODUCT_QUANTITY"])
                minimum = int(product["MinStock"])
            except (ValueError, KeyError):
                continue

            if quantity <= minimum:
                low_stock.append(product)

        return low_stock