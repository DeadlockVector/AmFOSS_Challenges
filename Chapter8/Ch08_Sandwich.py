import pyinputplus as pyip

def Price(bread, protien, cheese, sauce, number):
    list_order = [bread, protien, cheese, sauce]
    costs = {'bread':{'Wheat':30, 'White':40, 'Sour Dough':35}, 
        'protien':{'Chicken':100, 'Turkey':125, 'Ham':115, 'Tofu':195}, 
        'cheese':{'Cheddar':10, 'Swiss':15, 'Mozarella':20, 'nay':0}, 
        'sauce':{'Mayo':12, 'Mustard':18, 'Lettuce':8, 'Tomato':8, 'nay':0}}

    total_cost = 0
    j = 0
    for i in costs:
        total_cost += costs[i][list_order[j]]
        j += 1

    return total_cost*number
    


    
print('Monsiuer` Bague`tte Resto')
bread = pyip.inputMenu(['Wheat', 'White', 'Sour Dough'], prompt = "Choose a bread type\n")

protein  = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt = "What protien could we delight you with?\n")

cheese_choice = pyip.inputYesNo(prompt = "Do you have an appetite for cheese monsieur`(Yes or No)?\n")
if cheese_choice.lower() == "yes":
    cheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozarella'], prompt = "Take the luxury of having a look at some of our finest Cheese\n")
else:
    cheese = 'nay'

sauce_choice = pyip.inputYesNo(prompt = "Does your appetite call for some sauce monsieur`(Yes or No)?\n")
if sauce_choice.lower() == "yes":
    sauce = pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'], prompt = "Have a look at the finest sauces of the East Coast\n")
else:
    cheese = 'nay'

number = pyip.inputInt('Enter the number of sandwiches - ', greaterThan=1)


print('Total Cost -', Price(bread, protein, cheese, sauce, number))
print('We extensively aprreciate your deciosion of visiting our humble restaurant')