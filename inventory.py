
FILE_NAME = "products.csv"
SALES_FILE = "sales.csv"


def create_files():
    try:
        file = open(FILE_NAME, "r")
        file.close()
    except FileNotFoundError:
        file = open(FILE_NAME, "w")
        file.write("ID,Name,Quantity,Price,Minimum Stock\n")
        file.close()

    try:
        file = open(SALES_FILE, "r")
        file.close()
    except FileNotFoundError:
        file = open(SALES_FILE, "w")
        file.write("Product ID,Product Name,Quantity Sold,Total Price\n")
        file.close()


def load_products():
    products = []

    try:
        file = open(FILE_NAME, "r")

        # Skip the header
        file.readline()

        for line in file:
            line = line.strip()

            if line == "":
                continue

            data = line.split(",")

            if len(data) != 5:
                continue

            product = {
                "id": data[0],
                "name": data[1],
                "quantity": int(data[2]),
                "price": float(data[3]),
                "minimum_stock": int(data[4])
            }

            products.append(product)

        file.close()

    except FileNotFoundError:
        create_files()

    return products


def save_products(products):
    file = open(FILE_NAME, "w")

    file.write("ID,Name,Quantity,Price,Minimum Stock\n")

    for product in products:
        file.write(
            product["id"] + "," +
            product["name"] + "," +
            str(product["quantity"]) + "," +
            str(product["price"]) + "," +
            str(product["minimum_stock"]) + "\n"
        )

    file.close()


def add_product(products, product_id, name, quantity, price, minimum_stock):

    for product in products:
        if product["id"] == product_id:
            return False, "Product ID already exists."

    product = {
        "id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "minimum_stock": minimum_stock
    }

    products.append(product)
    save_products(products)

    return True, "Product added successfully."


def update_product(products, product_id, quantity, price, minimum_stock):

    for product in products:

        if product["id"] == product_id:

            product["quantity"] = quantity
            product["price"] = price
            product["minimum_stock"] = minimum_stock

            save_products(products)

            return True, "Product updated successfully."

    return False, "Product not found."


def delete_product(products, product_id):

    for product in products:

        if product["id"] == product_id:

            products.remove(product)
            save_products(products)

            return True, "Product deleted successfully."

    return False, "Product not found."


def search_product(products, search):

    results = []

    for product in products:

        if (
            search.lower() in product["id"].lower()
            or search.lower() in product["name"].lower()
        ):
            results.append(product)

    return results


def get_low_stock(products):

    low_stock = []

    for product in products:

        if product["quantity"] <= product["minimum_stock"]:
            low_stock.append(product)

    return low_stock


def record_sale(products, product_id, quantity_sold):

    if quantity_sold <= 0:
        return False, "Quantity must be greater than zero."

    for product in products:

        if product["id"] == product_id:

            if quantity_sold > product["quantity"]:
                return False, "Not enough stock available."

            product["quantity"] -= quantity_sold

            total_price = quantity_sold * product["price"]

            save_products(products)

            file = open(SALES_FILE, "a")

            file.write(
                product["id"] + "," +
                product["name"] + "," +
                str(quantity_sold) + "," +
                str(total_price) + "\n"
            )

            file.close()

            return True, (
                "Sale recorded successfully. "
                "Remaining stock: "
                + str(product["quantity"])
            )

    return False, "Product not found."


def get_inventory_summary(products):

    total_products = len(products)
    total_quantity = 0
    total_value = 0
    low_stock_count = 0

    for product in products:

        total_quantity += product["quantity"]

        total_value += (
            product["quantity"] *
            product["price"]
        )

        if product["quantity"] <= product["minimum_stock"]:
            low_stock_count += 1

    return {
        "total_products": total_products,
        "total_quantity": total_quantity,
        "total_value": total_value,
        "low_stock": low_stock_count
    }


def get_sales():

    sales = []

    try:
        file = open(SALES_FILE, "r")

        # Skip header
        file.readline()

        for line in file:

            line = line.strip()

            if line == "":
                continue

            data = line.split(",")

            if len(data) != 4:
                continue

            sales.append({
                "id": data[0],
                "name": data[1],
                "quantity": int(data[2]),
                "total": float(data[3])
            })

        file.close()

    except FileNotFoundError:
        create_files()

    return sales
 main
