import tkinter as tk

import inventory
import api
import ai_assistant

from gui import InventoryGUI


# ============================================================
# LOAD INVENTORY
# ============================================================

inventory.create_files()

products = inventory.load_products()


# ============================================================
# INVENTORY FUNCTIONS
# MAIN CONNECTS GUI TO INVENTORY
# ============================================================

def add_product(
    product_id,
    name,
    quantity,
    price,
    minimum_stock
):

    return inventory.add_product(
        products,
        product_id,
        name,
        quantity,
        price,
        minimum_stock
    )


def update_product(
    product_id,
    quantity,
    price,
    minimum_stock
):

    return inventory.update_product(
        products,
        product_id,
        quantity,
        price,
        minimum_stock
    )


def delete_product(product_id):

    return inventory.delete_product(
        products,
        product_id
    )


def record_sale(
    product_id,
    quantity
):

    return inventory.record_sale(
        products,
        product_id,
        quantity
    )


def search_product(search):

    return inventory.search_product(
        products,
        search
    )


def low_stock():

    return inventory.get_low_stock(
        products
    )


# ============================================================
# API
# ============================================================

def api_search(product_name):

    return api.search_product_api(
        product_name
    )


# ============================================================
# AI
# ============================================================

def ai_analysis():

    return ai_assistant.get_ai_summary(
        products
    )


# ============================================================
# SUMMARY
# ============================================================

def inventory_summary():

    return inventory.get_inventory_summary(
        products
    )


# ============================================================
# START APPLICATION
# ============================================================

def main():

    root = tk.Tk()

    app = InventoryGUI(
        root=root,
        products=products,

        add_function=add_product,

        update_function=update_product,

        delete_function=delete_product,

        sale_function=record_sale,

        search_function=search_product,

        low_stock_function=low_stock,

        api_function=api_search,

        ai_function=ai_analysis,

        summary_function=inventory_summary
    )

    root.mainloop()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
