import datetime # untuk membaca waktu
import os # untuk command clear screen
import time #untuk command sleep

def clear_screen(): # untuk membersihkan terminal
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class User: # untuk tempat menyimpan password dan emoney
    def __init__(self, username, pin, role, name, gender, age, emoney=0):
        self.username = username
        self.pin = pin
        self.role = role
        self.name = name
        self.gender = gender
        self.age = age
        self.emoney = emoney
    def top_up(self, amount):
        self.emoney += amount
        print(f"Berhasil! Saldo anda sekarang: Rp. {self.emoney}")
    
    def __str__(self):
        return f"User(username={self.username}, role={self.role}, emoney={self.emoney})"

class Product: # untuk menyimpan parameter product
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
    
    def __str__(self):
        return f"Product(id={self.id}, title={self.title}, price={self.price})"

class Cart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, product_id, products):
        product = next((prod for prod in products if prod.id == product_id), None)
        if product:
            for item in self.items:
                if item[0].id == product.id:
                    item[1] += 1
                    self.total += product.price
                    return
            self.items.append([product, 1])
            self.total += product.price
    
    def calculate_final_price(self):
        discount = self.calculate_discount()
        return self.total - discount
    
    def calculate_discount(self):
        if self.total > 250000:
            return self.total * 0.15
        elif self.total > 100000:
            return self.total * 0.1
        return 0
    
    def display_bill(self):
        discount = self.calculate_discount()
        final_total = self.total - discount
        for item, quantity in self.items:
            print(f"{item.title} x {quantity} = {item.price*quantity}")
        print(f"Harga Total: {self.total}")
        print(f"Diskon: {discount}")
        print(f"Harga Setelah Diskon: {final_total}")
    
    def clear_items(self):
        self.items = []
        self.total = 0