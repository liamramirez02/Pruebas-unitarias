class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_product(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self, tax=0.0, discount=0.0):
        subtotal = sum(item["product"]["price"] * item["quantity"] for item in self.items)
        total_with_tax = subtotal * (1 + tax)
        total_with_discount = total_with_tax * (1 - discount)
        return round(total_with_discount, 2)
