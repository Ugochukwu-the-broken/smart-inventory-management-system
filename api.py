
"""api.py - External product lookup for the Smart Inventory Management System.

Searches the DummyJSON API by product name and returns the first match
(category, price, brand, rating, description).

    pip install requests
"""
import requests

API_URL = "https://dummyjson.com/products/search"
TIMEOUT = 10  # seconds


def search_product_api(product_name):
    """Look up a product by name.

    Returns a dict:
      {"success": True,  "product": {...}}   product found
      {"success": False, "message": "..."}   empty input, not found, or error
    """
    product_name = (product_name or "").strip()
    if not product_name:
        return {"success": False, "message": "Please enter a product name."}

    try:
        response = requests.get(API_URL, params={"q": product_name}, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Connection failed. Check your internet connection."}
    except requests.exceptions.Timeout:
        return {"success": False, "message": "The request timed out. Please try again."}
    except (requests.exceptions.RequestException, ValueError):
        return {"success": False, "message": "Could not retrieve product information."}

    products = data.get("products", [])
    if not products:
        return {"success": False, "message": f"No product found for '{product_name}'."}

    item = products[0]  # first matching product
    return {
        "success": True,
        "product": {
            "name": item.get("title", "N/A"),
            "category": item.get("category", "N/A"),
            "price": item.get("price", "N/A"),
            "brand": item.get("brand", "N/A"),
            "rating": item.get("rating", "N/A"),
            "description": item.get("description", "N/A"),
        },
    }


def format_product(product):
    """Turn a product dict into text for display in the GUI."""
    return (
        f"Name: {product['name']}\n"
        f"Category: {product['category']}\n"
        f"Price: ${product['price']}\n"
        f"Brand: {product['brand']}\n"
        f"Rating: {product['rating']}\n"
        f"Description: {product['description']}"
    )


if __name__ == "__main__":
    result = search_product_api(input("Product name: "))
    print(format_product(result["product"]) if result["success"] else result["message"])
 main
