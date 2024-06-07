#from Model.model import Transaksi
from Model.model import Cart
from Model.model import Product
from Model.model import User
import time
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class UserController: # untuk mengatur login
    def __init__(self, users):
        self.users = users
    
    def login(self, username, pin):
        for user in self.users:
            if user.username == username and user.pin == pin:
                return user, user.gender
        return None, None
    
    def register(self):
        clear_screen()
        print("Halo! Silahkan isi data diri anda terlebih dahulu.")
        username = input("Masukkan username yang diinginkan: ")
        if username in [user.username for user in self.users]:
            print("Username sudah terdaftar!")
            return False
        pin = input("Masukkan PIN baru anda: ")
        name = input("Masukkan nama: ")
        gender = input("Masukkan jenis kelamin (L/P): ")
        age = int(input("Masukkan umur: "))
        new_user = User(username, pin, 'customer', name, gender, age)
        self.users.append(new_user)
        time.sleep(1.0)
        print("Registrasi Sukses!")
        time.sleep(1.0)
        clear_screen()
    
    def top_up_emoney(self, user, amount):
        user.top_up(amount)

class ProductController: # untuk mengatur produk 
    def __init__(self, products):
        self.products = products
    
    def add_product(self, id, title, price):
        new_product = Product(id, title, price)
        self.products.append(new_product)
    
    def update_product(self, product_id, **updates):
        product = next((prod for prod in self.products if prod.id == product_id), None)
        if product:
            product.__dict__.update(**updates)
            print(f"Produk dengan ID {product_id} telah diperbarui.")
        else:
            print("Produk tidak ditemukan!")
    
    def delete_products(self, product_id):
        self.products = [prod for prod in self.products if prod.id != product_id]
        print(f"Produk dengan ID {product_id} telah dihapus!")
    
    def search_products(self, search_term):
        return [prod for prod in self.products if search_term in prod.title]
    
    def sort_products(self, ascending=True):
        return sorted(self.products, key=lambda prod: prod.price, reverse=not ascending)
    
class CartController:
    def __init__(self):
        self.cart = Cart()
    
    def add_cart(self, product_id, products):
        self.cart.add_item(product_id, products)
    
    def get_items(self):
        return self.cart.items