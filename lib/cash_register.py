#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        
    def add_item(self, title, price, quantity=1):
        self.price = price
        for self.i in range(quantity):
            self.items.append(title)

        self.total += self.price * quantity
        return self.items

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total - (self.price * self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.items:
            return

        last_item_price = self.price
        last_item_quantity = self.items.count(self.items[-1])

        for self.i in range(last_item_quantity):
            self.items.pop()

        self.total -= last_item_price * last_item_quantity