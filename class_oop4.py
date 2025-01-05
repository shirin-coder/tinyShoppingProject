class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_from_cart(self, item_name):
        for product in self.cart:
            if product['item'] == item_name:
                self.cart.remove(product)
                print(f"{item_name} has been removed from your cart.")
                return
        print(f"{item_name} is not in the cart.")

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('Total price:', total)
        if amount < total:
            print(f'Please provide {total - amount} more money.')
        else:
            extra = amount - total
            print(f'Here are your items and extra money {extra}.')

# Example Usage
shirin = Shopping("shirin akter")
shirin.add_to_cart('alu', 50, 6)
shirin.add_to_cart('dim', 12, 24)
shirin.add_to_cart('rice', 50, 5)

print("Cart before removal:", shirin.cart)
shirin.remove_from_cart('dim')  # Removing an item
print("Cart after removal:", shirin.cart)

shirin.checkout(600)
shirin.checkout(1600)












