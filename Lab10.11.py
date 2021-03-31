#Name: Nguyen Vo
#PISD: 1673509


class FoodItem:
    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

    #def unit_test(self):
        #print('FoodItem properly initialized with default constructor param value.')
        #print('name is: {}'.format(self.name))
        #print('fat is: {:.2f}'.format(self.fat))
        #print('carbs is: {:.2f}'.format(self.carbs))
        #print('protein is: {:2f}'.format(self.protein))
if __name__ == '__main__':
    food = FoodItem()
    item = input()
    amt_fat = float(input())
    amt_carbs = float(input())
    amt_protein = float(input())

    food1 = FoodItem(item, amt_fat, amt_carbs, amt_protein)

    num_servings = float(input())

    food.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food.get_calories(num_servings)))

    #food.unit_test()
    #print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food.get_calories(num_servings)))
    print()

    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food1.get_calories(num_servings)))

