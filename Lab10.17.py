#Name: Nguyen Vo
#PISD: 1673509


class ItemToPurchase:        #Start itemtopurchase definition
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):             #this will print statment for items being call in main body part
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(int(self.item_price)) + ' = $' + str(int(self.item_price * self.item_quantity)))
        
        
#main body part         
if __name__ == '__main__':
    print('Item 1')
    item1 = ItemToPurchase()
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = float(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nItem 2')
    item2 = ItemToPurchase()
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

#after getting info from both items then proceed to calculate total Cost
    totalCost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    print('\nTOTAL COST')          #complete program by output statement for items after retrieving info 
    item1.print_item_cost()
    item2.print_item_cost()
    print('\nTotal: $' + str(int(totalCost)))
