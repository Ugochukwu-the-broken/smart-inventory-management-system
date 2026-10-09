import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class InventoryGUI:

    def __init__(
        self,
        root,
        products,
        add_function,
        update_function,
        delete_function,
        sale_function,
        search_function,
        low_stock_function,
        api_function,
        ai_function,
        summary_function
    ):

        self.root = root
        self.products = products

        self.add_function = add_function
        self.update_function = update_function
        self.delete_function = delete_function
        self.sale_function = sale_function
        self.search_function = search_function
        self.low_stock_function = low_stock_function
        self.api_function = api_function
        self.ai_function = ai_function
        self.summary_function = summary_function

        self.root.title("Smart Inventory Management System")
        self.root.geometry("1000x650")

        self.create_dashboard()

    # =========================================================
    # MAIN DASHBOARD
    # =========================================================

    def create_dashboard(self):

        title = tk.Label(
            self.root,
            text="SMART INVENTORY MANAGEMENT SYSTEM",
            font=("Arial", 20, "bold")
        )

        title.pack(pady=20)

        subtitle = tk.Label(
            self.root,
            text="Select an operation",
            font=("Arial", 12)
        )

        subtitle.pack(pady=5)

        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=20)

        buttons = [
            ("Add Product", self.show_add_section),
            ("Update Product", self.show_update_section),
            ("Delete Product", self.show_delete_section),
            ("Record Sale", self.show_sale_section),
            ("Search Product", self.show_search_section),
            ("Low Stock", self.show_low_stock_section),
            ("API Search", self.show_api_section),
            ("AI Analysis", self.show_ai_section),
            ("Inventory Summary", self.show_summary_section)
        ]

        row = 0
        column = 0

        for text, command in buttons:

            button = tk.Button(
                button_frame,
                text=text,
                width=20,
                height=2,
                command=command
            )

            button.grid(
                row=row,
                column=column,
                padx=10,
                pady=10
            )

            column += 1

            if column == 3:
                column = 0
                row += 1

        # Area where the selected section will appear
        self.section_frame = tk.Frame(
            self.root,
            bd=2,
            relief=tk.GROOVE
        )

        self.section_frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=10
        )

        self.show_home_section()

    # =========================================================
    # CLEAR CURRENT SECTION
    # =========================================================

    def clear_section(self):

        for widget in self.section_frame.winfo_children():
            widget.destroy()

    # =========================================================
    # HOME
    # =========================================================

    def show_home_section(self):

        self.clear_section()

        label = tk.Label(
            self.section_frame,
            text="Welcome to Smart Inventory Management System",
            font=("Arial", 16, "bold")
        )

        label.pack(pady=40)

        instruction = tk.Label(
            self.section_frame,
            text="Choose an operation from the buttons above.",
            font=("Arial", 12)
        )

        instruction.pack()

    # =========================================================
    # ADD PRODUCT
    # =========================================================

    def show_add_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="ADD PRODUCT",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=15)

        form = tk.Frame(self.section_frame)

        form.pack(pady=10)

        tk.Label(
            form,
            text="Product ID:"
        ).grid(row=0, column=0, padx=10, pady=8)

        self.add_id = tk.Entry(form, width=30)

        self.add_id.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(
            form,
            text="Product Name:"
        ).grid(row=1, column=0, padx=10, pady=8)

        self.add_name = tk.Entry(form, width=30)

        self.add_name.grid(row=1, column=1, padx=10, pady=8)

        tk.Label(
            form,
            text="Quantity:"
        ).grid(row=2, column=0, padx=10, pady=8)

        self.add_quantity = tk.Entry(form, width=30)

        self.add_quantity.grid(row=2, column=1, padx=10, pady=8)

        tk.Label(
            form,
            text="Price:"
        ).grid(row=3, column=0, padx=10, pady=8)

        self.add_price = tk.Entry(form, width=30)

        self.add_price.grid(row=3, column=1, padx=10, pady=8)

        tk.Label(
            form,
            text="Minimum Stock:"
        ).grid(row=4, column=0, padx=10, pady=8)

        self.add_minimum = tk.Entry(form, width=30)

        self.add_minimum.grid(row=4, column=1, padx=10, pady=8)

        tk.Button(
            self.section_frame,
            text="Add Product",
            width=20,
            command=self.add_product
        ).pack(pady=15)

    def add_product(self):

        product_id = self.add_id.get().strip()
        name = self.add_name.get().strip()

        if product_id == "" or name == "":
            messagebox.showerror(
                "Error",
                "Product ID and name are required."
            )
            return

        try:
            quantity = int(self.add_quantity.get())
            price = float(self.add_price.get())
            minimum_stock = int(self.add_minimum.get())

        except ValueError:
            messagebox.showerror(
                "Error",
                "Quantity and minimum stock must be whole numbers, and price must be a number."
            )
            return

        result, message = self.add_function(
            product_id,
            name,
            quantity,
            price,
            minimum_stock
        )

        if result:

            messagebox.showinfo(
                "Success",
                message
            )

            self.clear_section()

            self.show_home_section()

        else:

            messagebox.showerror(
                "Error",
                message
            )

    # =========================================================
    # UPDATE PRODUCT
    # =========================================================

    def show_update_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="UPDATE PRODUCT",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=15)

        form = tk.Frame(self.section_frame)

        form.pack(pady=10)

        tk.Label(
            form,
            text="Product ID:"
        ).grid(row=0, column=0, padx=10, pady=8)

        self.update_id = tk.Entry(form, width=30)

        self.update_id.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        tk.Label(
            form,
            text="New Quantity:"
        ).grid(row=1, column=0, padx=10, pady=8)

        self.update_quantity = tk.Entry(
            form,
            width=30
        )

        self.update_quantity.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        tk.Label(
            form,
            text="New Price:"
        ).grid(row=2, column=0, padx=10, pady=8)

        self.update_price = tk.Entry(
            form,
            width=30
        )

        self.update_price.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        tk.Label(
            form,
            text="New Minimum Stock:"
        ).grid(row=3, column=0, padx=10, pady=8)

        self.update_minimum = tk.Entry(
            form,
            width=30
        )

        self.update_minimum.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        tk.Button(
            self.section_frame,
            text="Update Product",
            width=20,
            command=self.update_product
        ).pack(pady=15)

    def update_product(self):

        product_id = self.update_id.get().strip()

        if product_id == "":
            messagebox.showerror(
                "Error",
                "Enter the Product ID."
            )
            return

        try:

            quantity = int(
                self.update_quantity.get()
            )

            price = float(
                self.update_price.get()
            )

            minimum_stock = int(
                self.update_minimum.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter valid numbers for quantity, price and minimum stock."
            )

            return

        result, message = self.update_function(
            product_id,
            quantity,
            price,
            minimum_stock
        )

        if result:

            messagebox.showinfo(
                "Success",
                message
            )

            self.show_home_section()

        else:

            messagebox.showerror(
                "Error",
                message
            )

    # =========================================================
    # DELETE PRODUCT
    # =========================================================

    def show_delete_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="DELETE PRODUCT",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=20)

        tk.Label(
            self.section_frame,
            text="Enter Product ID:"
        ).pack(pady=5)

        self.delete_id = tk.Entry(
            self.section_frame,
            width=30
        )

        self.delete_id.pack(pady=10)

        tk.Button(
            self.section_frame,
            text="Delete Product",
            width=20,
            command=self.delete_product
        ).pack(pady=15)

    def delete_product(self):

        product_id = self.delete_id.get().strip()

        if product_id == "":

            messagebox.showerror(
                "Error",
                "Enter the Product ID."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this product?"
        )

        if not answer:
            return

        result, message = self.delete_function(
            product_id
        )

        if result:

            messagebox.showinfo(
                "Success",
                message
            )

            self.show_home_section()

        else:

            messagebox.showerror(
                "Error",
                message
            )

    # =========================================================
    # RECORD SALE
    # =========================================================

    def show_sale_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="RECORD SALE",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=20)

        form = tk.Frame(self.section_frame)

        form.pack(pady=10)

        tk.Label(
            form,
            text="Product ID:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.sale_id = tk.Entry(
            form,
            width=30
        )

        self.sale_id.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            form,
            text="Quantity Sold:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.sale_quantity = tk.Entry(
            form,
            width=30
        )

        self.sale_quantity.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        tk.Button(
            self.section_frame,
            text="Record Sale",
            width=20,
            command=self.record_sale
        ).pack(pady=15)

    def record_sale(self):

        product_id = self.sale_id.get().strip()

        if product_id == "":
            messagebox.showerror(
                "Error",
                "Enter the Product ID."
            )
            return

        try:

            quantity = int(
                self.sale_quantity.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid quantity."
            )

            return

        result, message = self.sale_function(
            product_id,
            quantity
        )

        if result:

            messagebox.showinfo(
                "Sale",
                message
            )

            self.show_home_section()

        else:

            messagebox.showerror(
                "Sale Error",
                message
            )

    # =========================================================
    # SEARCH PRODUCT
    # =========================================================

    def show_search_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="SEARCH PRODUCT",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=15)

        search_frame = tk.Frame(
            self.section_frame
        )

        search_frame.pack(pady=10)

        tk.Label(
            search_frame,
            text="Product ID or Name:"
        ).pack(side=tk.LEFT, padx=5)

        self.search_entry = tk.Entry(
            search_frame,
            width=30
        )

        self.search_entry.pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            search_frame,
            text="Search",
            command=self.search_product
        ).pack(side=tk.LEFT, padx=5)

        self.create_table()

    def search_product(self):

        search = self.search_entry.get().strip()

        if search == "":
            messagebox.showerror(
                "Error",
                "Enter a product ID or name."
            )
            return

        results = self.search_function(
            search
        )

        self.display_products(results)

        if len(results) == 0:

            messagebox.showinfo(
                "Search",
                "No product found."
            )

    # =========================================================
    # LOW STOCK
    # =========================================================

    def show_low_stock_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="LOW STOCK PRODUCTS",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=15)

        results = self.low_stock_function()

        if len(results) == 0:

            tk.Label(
                self.section_frame,
                text="No products are currently low in stock.",
                font=("Arial", 12)
            ).pack(pady=30)

            return

        self.create_table()

        self.display_products(results)

    # =========================================================
    # API SEARCH
    # =========================================================

    def show_api_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="PRODUCT API SEARCH",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=15)

        tk.Label(
            self.section_frame,
            text="Enter product name:"
        ).pack(pady=5)

        self.api_entry = tk.Entry(
            self.section_frame,
            width=40
        )

        self.api_entry.pack(pady=10)

        tk.Button(
            self.section_frame,
            text="Search API",
            width=20,
            command=self.api_search
        ).pack(pady=10)

    def api_search(self):

        product_name = self.api_entry.get().strip()

        if product_name == "":

            messagebox.showerror(
                "API",
                "Enter a product name."
            )

            return

        product, message = self.api_function(
            product_name
        )

        if product is None:

            messagebox.showerror(
                "API",
                message
            )

            return

        text = (
            "Product: "
            + str(product["name"])
            + "\n\n"
            "Category: "
            + str(product["category"])
            + "\n\n"
            "Price: "
            + str(product["price"])
            + "\n\n"
            "Brand: "
            + str(product["brand"])
            + "\n\n"
            "Rating: "
            + str(product["rating"])
            + "\n\n"
            "Description:\n"
            + str(product["description"])
        )

        messagebox.showinfo(
            "API Product Information",
            text
        )

    # =========================================================
    # AI ANALYSIS
    # =========================================================

    def show_ai_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="AI INVENTORY ANALYSIS",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=20)

        message = self.ai_function()

        result = tk.Label(
            self.section_frame,
            text=message,
            font=("Arial", 12),
            wraplength=700,
            justify=tk.LEFT
        )

        result.pack(pady=30)

    # =========================================================
    # SUMMARY
    # =========================================================

    def show_summary_section(self):

        self.clear_section()

        title = tk.Label(
            self.section_frame,
            text="INVENTORY SUMMARY",
            font=("Arial", 16, "bold")
        )

        title.pack(pady=20)

        summary = self.summary_function()

        text = (
            "Total Products: "
            + str(summary["total_products"])
            + "\n\n"
            "Total Quantity: "
            + str(summary["total_quantity"])
            + "\n\n"
            "Total Inventory Value: "
            + str(summary["total_value"])
            + "\n\n"
            "Low Stock Products: "
            + str(summary["low_stock"])
        )

        label = tk.Label(
            self.section_frame,
            text=text,
            font=("Arial", 13),
            justify=tk.LEFT
        )

        label.pack(pady=30)

    # =========================================================
    # TABLE
    # =========================================================

    def create_table(self):

        table_frame = tk.Frame(
            self.section_frame
        )

        table_frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=10
        )

        columns = (
            "ID",
            "Name",
            "Quantity",
            "Price",
            "Minimum Stock"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.table.heading(
                column,
                text=column
            )

            self.table.column(
                column,
                width=130
            )

        self.table.pack(
            fill=tk.BOTH,
            expand=True
        )

    def display_products(self, products):

        for item in self.table.get_children():
            self.table.delete(item)

        for product in products:

            self.table.insert(
                "",
                tk.END,
                values=(
                    product["id"],
                    product["name"],
                    product["quantity"],
                    product["price"],
                    product["minimum_stock"]
                )
            )
