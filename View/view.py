from prettytable import PrettyTable
import os
import sys # untuk mengeluarkan program
import datetime
import time
import getpass # untuk menghilangkan inputan password

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def exit_program():
    sys.exit()

class View:
    def __init__(self, user_controller, product_controller, cart_controller):
        self.user_controller = user_controller
        self.product_controller = product_controller
        self.cart_controller = cart_controller
        self.cart = self.cart_controller.cart
        self.user = None
    
    def display_menu(self):
        clear_screen()
        while True:
            current_time = datetime.datetime.now()
            if current_time.hour < 0 or current_time.hour >= 24:
                clear_screen()
                print("Mohon maaf, toko hanya beroperasi dari jam 8.00-16.00 WITA.")
                return
            if not self.user:
                user, gender = self.login()
                if not self.user:
                    continue
            if self.user.role == "admin":
                self.admin_menu(user, gender)
            elif self.user.role == "customer":
                self.customer_menu(user, gender)
    
    def login(self):
        clear_screen()
        print("Apabila ingin Exit, silahkan mengetik 'exit' pada username atau password.")
        print("Ingin mendaftar? Silahkan mengetik 'register' di kolom username.")
        username = input("Masukkan username: ")
        if username.lower() == 'exit':
            print("Terima Kasih!")
            exit_program()
            return None, None
        elif username.lower() == 'register':
            result = self.user_controller.register()
            if result is None:
                return None, None
            return result
        pin = getpass.getpass("Masukkan PIN anda: ")
        if pin.lower() == 'exit':
            print("Terima Kasih!")
            exit_program()
            return None, None
        user, gender = self.user_controller.login(username, pin)
        print("Mohon Menunggu Sebentar...")
        time.sleep(0.5)
        if user:
            print("Login berhasil! Mohon Menunggu...")
            time.sleep(1.0)
            self.user = user
            return user, gender
        print("Username atau password salah!")
        time.sleep(1.0)
        return None, None

    
    def admin_menu(self, user, gender):
        if gender == "L":
            clear_screen()
            while True:
                print("+ ------ ADMIN YUKI ------ +")
                print("| 1. Tambahkan produk      |")
                print("| 2. Tampilkan Produk      |")
                print("| 3. Update produk         |")
                print("| 4. Hapus produk          |")
                print("| 5. Logout                |")
                print("| 6. Keluar Program        |")
                print("+ ------------------------ +")
                choice = input("Masukkan pilihan: ")
                if choice == "1":
                    clear_screen()
                    self.add_product()
                elif choice == "2":
                    clear_screen()
                    self.show_product()
                elif choice == "3":
                    clear_screen()
                    self.update_product()
                elif choice == "4":
                    clear_screen()
                    self.delete_products()
                elif choice == "5":
                    clear_screen()
                    print("Logout Berhasil! Mohon Menunggu...")
                    time.sleep(1.0)
                    self.user = None
                    return
                elif choice == "6":
                    print("Terima Kasih!")
                    exit_program()
                else:
                    print("Pilihan tidak valid!")
                    time.sleep(0.5)
                    clear_screen()
        else:
            clear_screen()
            while True:
                print("+ ------ ADMIN MIKU ------ +")
                print("| 1. Tambahkan produk      |")
                print("| 2. Tampilkan Produk      |")
                print("| 3. Update produk         |")
                print("| 4. Hapus produk          |")
                print("| 5. Logout                |")
                print("| 6. Keluar Program        |")
                print("+ ------------------------ +")
                choice = input("Masukkan pilihan: ")
                if choice == "1":
                    clear_screen()
                    self.add_product()
                elif choice == "2":
                    clear_screen()
                    self.show_product()
                elif choice == "3":
                    clear_screen()
                    self.update_product()
                elif choice == "4":
                    clear_screen()
                    self.delete_products()
                elif choice == "5":
                    clear_screen()
                    print("Logout Berhasil! Mohon Menunggu...")
                    time.sleep(1.0)
                    self.user = None
                    return
                elif choice == "6":
                    print("Terima Kasih!")
                    exit_program()
                else:
                    print("Pilihan tidak valid!")
                    time.sleep(0.5)
                    clear_screen()
    
    def add_product(self):
        try:
            id = input("Masukkan ID: ")
            title = input("Masukkan nama produk: ")
            price = int(input("Masukkan harga: "))
            self.product_controller.add_product(id, title, price)
            print("Produk ditambahkan!")
            time.sleep(0.5)
            clear_screen()
        except ValueError:
            print("Harga harus berupa angka!")
        
    def update_product(self):
        try:
            id = input("Masukkan ID produk yang ingin diperbaharui: ")
            title = input("Masukkan nama produk baru: ")
            price = int(input("Masukkan harga baru: "))
            self.product_controller.update_product(id, title=title, price=price)
            print("Produk diperbaharui!")
            time.sleep(0.5)
            clear_screen()
        except ValueError:
            print("Harga harus berupa angka!")
        
    def delete_products(self):
        id = input("Masukkan ID produk yang ingin dihapus: ")
        self.product_controller.delete_products(id)
        print("Produk dihapus!")
        time.sleep(0.5)
        clear_screen()
    
    def customer_menu(self, user, gender):
        if gender == "L":
            clear_screen()
            while True:
                print("+ ------------ HALO BROKU! ------------ +")
                print("| 1. Tambahkan Game ke Keranjang        |")
                print("| 2. Lihat Keranjang                    |")
                print("| 3. Checkout Keranjang                 |")
                print("| 4. Tampilkan Produk                   |")
                print("| 5. Top Up e-Money                     |")
                print("| 6. Tampilkan e-Money                  |")
                print("| 7. Cari Produk                        |")
                print("| 8. Urutkan Produk berdasarkan Harga   |")
                print("| 9. Logout                             |")
                print("| 10.Exit Program                       |")
                print("+ ------------------------------------- +")
                choice = input("Masukkan pilihan: ")
                if choice == "1":
                    clear_screen()
                    self.add_cart()
                elif choice == "2":
                    clear_screen()
                    self.show_cart(self.cart)
                elif choice == "3":
                    clear_screen()
                    self.checkout(self.cart)
                elif choice == "4":
                    clear_screen()
                    self.show_product()
                elif choice == "5":
                    clear_screen()
                    self.top_up_emoney(user)
                elif choice == "6":
                    clear_screen()
                    self.check_emoney(user)
                elif choice == "7":
                    clear_screen()
                    self.search_product()
                elif choice == "8":
                    clear_screen()
                    self.sort_product()
                elif choice == "9":
                    clear_screen()
                    print("Logout Berhasil! Mohon Menunggu...")
                    time.sleep(1.0)
                    self.user = None
                    return
                elif choice == "10":
                    print("Terima Kasih!")
                    exit_program()
                else:
                    print("Pilihan tidak valid!")
                    time.sleep(0.5)
                    clear_screen()
        else:
            clear_screen()
        while True:
            print("+ ------------- HAI SIST! ------------- +")
            print("| 1. Tambahkan Game ke Keranjang        |")
            print("| 2. Lihat Keranjang                    |")
            print("| 3. Checkout Keranjang                 |")
            print("| 4. Tampilkan Produk                   |")
            print("| 5. Top Up e-Money                     |")
            print("| 6. Tampilkan e-Money                  |")
            print("| 7. Cari Produk                        |")
            print("| 8. Urutkan Produk berdasarkan Harga   |")
            print("| 9. Logout                             |")
            print("| 10.Exit Program                       |")
            print("+ ------------------------------------- +")
            choice = input("Masukkan pilihan: ")
            if choice == "1":
                clear_screen()
                self.add_cart()
            elif choice == "2":
                clear_screen()
                self.show_cart(self.cart)
            elif choice == "3":
                clear_screen()
                self.checkout(self.cart)
            elif choice == "4":
                clear_screen()
                self.show_product()
            elif choice == "5":
                clear_screen()
                self.top_up_emoney(user)
            elif choice == "6":
                clear_screen()
                self.check_emoney(user)
            elif choice == "7":
                clear_screen()
                self.search_product()
            elif choice == "8":
                clear_screen()
                self.sort_product()
            elif choice == "9":
                clear_screen()
                print("Logout Berhasil! Mohon Menunggu...")
                time.sleep(1.0)
                self.user = None
                return
            elif choice == "10":
                print("Terima Kasih!")
                exit_program()
            else:
                print("Pilihan tidak valid!")
                time.sleep(0.5)
                clear_screen()
    
    def search_product(self):
        search_term = input("Masukkan nama game yang ingin dicari: ")
        found_products = self.product_controller.search_products(search_term)
        if found_products:
            for product in found_products:
                table = PrettyTable()
                table.field_names = ["ID Produk", "Judul Game", "Harga"]
                for product in found_products:
                    table.add_row([product.id, product.title, product.price])
                print(table)
        else:
            print("Tidak ada produk yang cocok dengan pencarian.")
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def sort_product(self):
        order = input("Urutkan harga (termurah/termahal): ")
        if order.lower() not in ['termurah', 'termahal']:
            print("Pilihan tidak valid, menggunakan urutan termurah")
            order = 'termurah'
        sorted_products = self.product_controller.sort_products(ascending=order == 'termurah')
        table = PrettyTable()
        table.field_names = ["ID Produk", "Judul Game", "Harga"]
        for product in sorted_products:
            table.add_row([product.id, product.title, product.price])
        print(table)
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def show_product(self):
        table = PrettyTable()
        table.field_names = ["ID Produk", "Judul Game", "Harga"]
        for product in self.product_controller.products:
            table.add_row([product.id, product.title, product.price])
        print(table)
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def check_emoney(self, user):
        print(f"Saldo e-Money Anda saat ini adalah: Rp {user.emoney}")
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def add_cart(self):
        table = PrettyTable()
        table.field_names = ["ID Produk", "Judul Game", "Harga"]
        for product in self.product_controller.products:
            table.add_row([product.id, product.title, product.price])
        print(table)
        product_id = input("Masukkan ID produk yang ingin ditambahkan ke keranjang: ")
        self.cart_controller.add_cart(product_id, self.product_controller.products)
        time.sleep(0.5)
        print("Produk ditambahkan ke keranjang!")
        time.sleep(0.5)
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def show_cart(self, cart):
        if not cart.items:
            print("Keranjang Kosong!")
            time.sleep(0.5)
            clear_screen()
            return
        self.cart.display_bill()
        time.sleep(1.0)
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def checkout(self, cart):
        if not cart.items:
            print("Keranjang Kosong!")
            time.sleep(0.5)
            clear_screen()
            return
        cart.display_bill()
        confirmation = input("Apakah Anda ingin melanjutkan transaksi? (y/n): ")
        if confirmation.lower() == 'y':
            final_price = cart.calculate_final_price()
            if final_price <= self.user.emoney:
                self.user.emoney -= final_price
                print("Transaksi Berhasil!")
                cart.clear_items()
                time.sleep(1.0)
                input("Tekan enter untuk kembali ke menu utama...")
                clear_screen()
            else:
                print("Saldo anda tidak mencukupi!")
                time.sleep(1.0)
                input("Tekan enter untuk kembali ke menu utama...")
                clear_screen()
    
    def top_up_emoney(self, user):
        try:
            amount = float(input("Masukkan jumlah yang ingin ditambahkan: "))
            if amount == 0:
                print("Saldo yang diisi tidak boleh 0!")
                time.sleep(0.5)
                clear_screen()
                return
            self.user_controller.top_up_emoney(user, amount)
            input("Tekan enter untuk kembali ke menu utama...")
            clear_screen()
        except ValueError:
            print("Inputan harus berupa angka!")
