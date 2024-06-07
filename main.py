from Controller.controller import UserController
from Controller.controller import ProductController
from Controller.controller import CartController
from Model.model import User
from Model.model import Product
from View.view import View

def main():
    users = []
    products = []
    
    admin_user = User(username="adminyuki", pin="885321", role="admin", name="khairu", gender="L", age=18, emoney=0)
    users.append(admin_user)
    
    admin_user = User(username="adminmiku", pin="885321", role="admin", name="khairu", gender="P", age=18, emoney=0)
    users.append(admin_user)
    
    customer_user = User(username="customer", pin="112358", role="customer", name="khairu", gender="L", age=18, emoney=0)
    users.append(customer_user)
    
    products.append(Product("G001", "Grand Theft Auto V: Premium Edition", 153600))
    products.append(Product("G002", "MotoGP™24", 699000))
    products.append(Product("G003", "Call of Duty®: Modern Warfare® III", 1050000))
    products.append(Product("G004", "FC 24", 759000))
    products.append(Product("G005", "DreadOut", 19199))
    products.append(Product("G006", "Manny's", 74000))
    
    user_controller = UserController(users)
    product_controller = ProductController(products)
    cart_controller = CartController()
    
    view = View(user_controller, product_controller, cart_controller)
    
    view.display_menu()

if __name__ == "__main__":
    main()