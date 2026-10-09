import json
import urllib.request
import urllib.parse


API_URL = "https://dummyjson.com/products/search?q="


def search_product_api(product_name):

    try:

        encoded_name = urllib.parse.quote(product_name)

        url = API_URL + encoded_name

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Smart Inventory System"
            }
        )

        response = urllib.request.urlopen(
            request,
            timeout=10
        )

        data = response.read().decode("utf-8")

        result = json.loads(data)

        if len(result.get("products", [])) == 0:
            return None, "No product found from API."

        product = result["products"][0]

        api_product = {
            "name": product.get("title", "Unknown"),
            "category": product.get("category", "Unknown"),
            "price": product.get("price", 0),
            "brand": product.get("brand", "Not available"),
            "rating": product.get("rating", 0),
            "description": product.get(
                "description",
                "No description available."
            )
        }

        return api_product, "Product information retrieved successfully."

    except Exception as error:

        return None, "API connection failed: " + str(error)
