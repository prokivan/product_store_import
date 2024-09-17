from models import Product, ProductStore, History


def options():
    print('''Choice the option (1-9):
        1) Balance
        2) Sale
        3) Buy
        4) Bank account
        5) Warehouse inventory
        6) Product Inventory
        7) Request history
        8) Clear request history
        9) Set discount
        10) Store history
        0) End''')


def show_products_buy():
    print('=' * 64 + '\n|| Products available for purchase:' + ' ' * 28 + '||')
    print('|| 1) Category: Sport | Product: Football T-Shirt | Price: 100 ||')
    print('|| 2) Category: Food | Product: Ramen | Price: 1.5 ' + ' ' * 12 + '||')
    print('|| 3) Category: Sport | Product: Ball | Price: 50 ' + ' ' * 13 + '||')
    print('|| 4) Category: Food | Product: Fish | Price: 20 ' + ' ' * 14 + '||')
    print('|| 5) Category: Sport | Product: Bike | Price: 400 ' + ' ' * 12 + '||')
    print('|| 6) Category: Food | Product: Protein | Price: 70.5 ' + ' ' * 9 + '||')
    print('=' * 64)


def show_and_play():
    p1 = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    p3 = Product('Sport', 'Ball', 50)
    p4 = Product('Food', 'Fish', 20)
    p5 = Product('Sport', 'Bike', 400)
    p6 = Product('Food', 'Protein', 70.5)
    s = ProductStore()
    h = History()

    print('=' * 32 + '\n' + '| Hi, I\'m the store\'s program! |\n| How can I help you?' + ' ' * 10 + '|\n' + '=' * 32)
    while True:
        options()
        choice = input('You choice: ')
        if choice.isdigit():
            if choice == '0':
                h.set_history('End')
                print('See you soon.')
                break
            elif choice == '1':
                h.set_history('Balance')
                print(f'Balance: {s.get_balance()}')
            elif choice == '2':
                h.set_history('Sale product')
                print('Warehouse inventory: ')
                s.get_all_products()
                product = input('Input name product: ')
                quantity = input('Input quantity of products: ')
                s.sell_product(product.capitalize(), int(quantity))

            elif choice == '3':
                h.set_history('Buy product')
                show_products_buy()
                product = input('Input name product: ')
                quantity = input('Input quantity of products: ')
                if product == '1':
                    s.add(p1, int(quantity))
                elif product == '2':
                    s.add(p2, int(quantity))
                elif product == '3':
                    s.add(p3, int(quantity))
                elif product == '4':
                    s.add(p4, int(quantity))
                elif product == '5':
                    s.add(p5, int(quantity))
                elif product == '6':
                    s.add(p6, int(quantity))
            elif choice == '4':
                h.set_history('Banc account')
                print(f'Banc account: {s.get_money()}')
            elif choice == '5':
                h.set_history('Warehouse inventory')
                print('Warehouse inventory: ')
                s.get_all_products()
            elif choice == '6':
                h.set_history('Product Inventory')
                product = input('Input name of product: ')
                print(s.get_product_info(product.capitalize()))
            elif choice == '7':
                h.set_history('Request history')
                print('Enter the number of records required. All history(start=0;end=0):')
                start = int(input('Start: '))
                end = int(input('End: '))
                h.get_history(start, end)
            elif choice == '8':
                print('Clear!')
                h.clear_history()
            elif choice == '9':
                product = input('Enter name or category: ')
                percent = int(input('Enter % discount: '))
                s.set_discount(product.capitalize(), percent)
            elif choice == '10':
                print(s.get_store_history())
            else:
                print('Error')
                continue
        else:
            print('Please enter number (1-9 or 0)')
