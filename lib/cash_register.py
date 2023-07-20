#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for i in range(0, quantity):
            self.items.append(title)
        self.prices = []
        self.prices.append(price)
        self.quantities = []
        self.quantities.append(quantity)

    def apply_discount(self):
        self.total -= self.total * (self.discount / 100)
        if self.discount != 0:
            print(f"After the discount, the total comes to ${int(self.total)}.")
        elif self.discount == 0:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        for i in range(0, self.quantities[-1]):
            self.total -= self.prices[-1]
        self.prices.pop()
        self.quantities.pop()
