def analyze_inventory(products):

    recommendations = []

    if len(products) == 0:
        return ["There are no products to analyze."]

    for product in products:

        quantity = product["quantity"]
        minimum = product["minimum_stock"]

        if quantity == 0:

            recommendations.append(
                product["name"] +
                ": OUT OF STOCK. Restock immediately."
            )

        elif quantity <= minimum:

            recommendations.append(
                product["name"] +
                ": LOW STOCK. Consider restocking soon."
            )

        elif quantity >= minimum * 5:

            recommendations.append(
                product["name"] +
                ": Stock level is high. Monitor demand before ordering more."
            )

        else:

            recommendations.append(
                product["name"] +
                ": Stock level looks normal."
            )

    return recommendations


def predict_restock(products):

    restock_list = []

    for product in products:

        quantity = product["quantity"]
        minimum = product["minimum_stock"]

        if quantity <= minimum:

            suggested_quantity = (
                minimum * 2
            ) - quantity

            if suggested_quantity < 1:
                suggested_quantity = 1

            restock_list.append({
                "id": product["id"],
                "name": product["name"],
                "current_stock": quantity,
                "suggested_restock": suggested_quantity
            })

    return restock_list


def get_ai_summary(products):

    if len(products) == 0:
        return "There is no inventory data to analyze."

    total = len(products)
    low = 0
    out_of_stock = 0

    for product in products:

        if product["quantity"] == 0:
            out_of_stock += 1

        elif product["quantity"] <= product["minimum_stock"]:
            low += 1

    if out_of_stock > 0:

        return (
            "AI Recommendation: "
            + str(out_of_stock)
            + " product(s) are out of stock. "
            "Restocking should be prioritized."
        )

    if low > 0:

        return (
            "AI Recommendation: "
            + str(low)
            + " product(s) are low in stock. "
            "Consider restocking these products."
        )

    return (
        "AI Recommendation: "
        + str(total)
        + " products were analyzed. "
        "Current stock levels look healthy."
    )
