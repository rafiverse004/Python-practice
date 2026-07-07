# The raise statement creates an exception manually.

def calculate_discount(price):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price * 0.9


try:
    discounted_price = calculate_discount(500)
    print(f"Discounted price: {discounted_price}")

    discounted_price = calculate_discount(-100)
    print(discounted_price)

except ValueError as error:
    print(error)