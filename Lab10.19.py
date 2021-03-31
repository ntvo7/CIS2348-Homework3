#Name: Nguyen Vo
#PISD: 1673509


class ItemToPurchase:
    def __init__(self, name = 'none', price = 0, quantity = 0, description = 'none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(int(self.item_price)) + ' = $' + str(int(self.item_price * self.item_quantity)))

    def print_item_description(self):
        print(self.item_name + ': ' + self.item_description)

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, itemName):
        removeItem = False
        for i in self.cart_items:
            if i.item_name == itemName:
                self.cart_items.remove(i)
                removeItem = True
                break
        if not removeItem:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase):
        modifyItem = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == ItemToPurchase.item_name:
                modifyItem = True
                if (ItemToPurchase.item_price == 0 and ItemToPurchase.item_quantity == 0 and ItemToPurchase.item_description == 'none'):
                    break
                else:
                    if (ItemToPurchase.item_price != 0):
                        self.cart_items[i].item_price = ItemToPurchase.item_price
                    elif (ItemToPurchase.item_quantity != 0):
                        self.cart_items[i].item_quantity = ItemToPurchase.item_quantity
                    elif (ItemToPurchase.item_description != 'none'):
                        self.cart_items[i].item_description = ItemToPurchase.item_description
                    break
        if not modifyItem:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        numItems = 0
        for i in self.cart_items:
            numItems += i.item_quantity
        return numItems

    def get_cost_of_cart(self):
        totalCost = 0
        Cost = 0
        for i in self.cart_items:
            Cost = i.item_quantity * i.item_price
            totalCost += Cost
        return totalCost

    def print_total(self):
        totalCost = self.get_cost_of_cart()
        if totalCost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print('Number of Items: ' + str(self.get_num_items_in_cart()) + '\n')
            for i in self.cart_items:
                i.print_item_cost()

            print('\nTotal: $' + str(totalCost))

    def print_description(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()

    def print_menu(newCart):
        customerCart = newCart
        menu = ('\nMENU\n'
                'a - Add item to cart\n'
                'r - Remove item from cart\n'
                'c - Change item quantity\n'
                "i - Output items' descriptions\n"
                'o - Output shopping cart\n'
                'q - Quit\n')
        cmd = ''
        while cmd != 'q':
            print(menu)
            cmd = input('Choose an option:\n')
            while (cmd != 'a' and cmd != 'o' and cmd != 'i' and cmd != 'q' and cmd != 'r' and cmd != 'c'):
                cmd = input('Choose an option:\n')
            if cmd == 'a':
                print("ADD ITEM TO CART")
                item_name = input('Enter the item name:\n')
                item_description = input('Enter the item description:\n')
                item_price = int(input('Enter the item price:\n'))
                item_quantity = int(input('Enter the item quantity:\n'))
                itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                customerCart.add_item(itemtoPurchase)
            elif cmd == 'o':
                print('OUTPUT SHOPPING CART')
                customerCart.print_total()
            elif cmd == 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                customerCart.print_description()

            elif cmd == 'r':
                print('REMOVE ITEM FROM CART')
                itemName = input('Enter name of item to remove:\n')
                customerCart.remove_item(itemName)
            elif cmd == 'c':
                print('CHANGE ITEM QUANTITY')
                itemName = input('Enter the item name:\n')
                Qty = int(input('Enter the new quantity:\n'))
                itemToPurchase = ItemToPurchase(itemName,0,Qty)
                customerCart.modify_item(itemToPurchase)

if __name__ == '__main__':
    customerName = input("Enter customer's name:\n")
    Date = input("Enter today's date:\n")

    print('\nCustomer name:', customerName)
    print("Today's date:", Date)

    newCart = ShoppingCart(customerName, Date)
    newCart.print_menu()