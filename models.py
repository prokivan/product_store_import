from datetime import datetime


class Product:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = 0


class ProductStore:

    def __init__(self):
        self.product_store = []
        self.money = 10000
        self.balance = 0
        self.store_info = open('store_history.txt', 'a')
        self.cur_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')

    def add(self, product, amount):
        if self.money >= amount * product.price:
            self.money -= amount * product.price
            self.balance -= amount * product.price
            self.store_info.write(f'Time change: {self.cur_time}\nCurrent balance: {self.get_balance()}\n')
            if product not in self.product_store:
                self.product_store.append(product)
            product.amount += amount
            self.store_info.write(f'Products in store:\n{self.get_all_products()}\n\n')
            print('Product is added!')
        else:
            print('You dont have enough money!')
            raise ValueError

    def set_discount(self, identifier, percent):
        for product in self.product_store:
            if product.category == identifier or product.name == identifier:
                product.discount = percent
                product.price = product.price - (product.price * percent / 100)
        print(f'Discount {percent} for products was set')

    def sell_product(self, product_name, amount):
        for product in self.product_store:
            if product.name == product_name and product.amount >= amount:
                product.amount -= amount
                self.money += amount * (product.price + (product.price * 30 / 100))
                self.balance += amount * (product.price + (product.price * 30 / 100))
                self.store_info.write(f'Time change: {self.cur_time}\nCurrent balance: {self.get_balance()}\n')
                self.store_info.write(f'Products in store:\n{self.get_all_products()}\n\n')
                print('Sell!')
                return
            elif product.name == product_name and product.amount < amount:
                raise ValueError

    def get_money(self):
        return self.money

    def get_balance(self):
        return self.balance

    def get_all_products(self):
        all_products = []
        if self.product_store:
            for product in self.product_store:
                all_products.append(
                    {
                        'Category': product.category,
                        'Name': product.name,
                        'Price': product.price,
                        'Amount': product.amount,
                        'Discount': product.discount

                    }
                )
            for i in all_products:
                print(i)
            return all_products
        else:
            print('Store is empty!')
            raise ValueError

    def get_product_info(self, product_name):
        for product in self.product_store:
            if product_name == product.name:
                return f'Name product: {product.name}, quantity: {product.amount} , price: {product.price}'
        else:
            print('We dont have this product!')
            raise NameError

    def get_store_history(self):
        file = open('store_history.txt', 'r')
        return file.read()


class History:
    def __init__(self):
        self.__set_history = open('history.txt', 'a')
        self.__get_history = open('history.txt', 'r')

    def set_history(self, request):
        cur_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')
        self.__set_history.write(f'Enter: {cur_time}. Request: {request}\n')

    def get_history(self, start, end=0):
        if end == 0:
            print(self.__get_history.read())
        elif end != 0:
            for i in range(start, end + 1):
                print(self.__get_history.readline())
        else:
            print('Error')

    def clear_history(self):
        open('test2.txt', 'w').close()
