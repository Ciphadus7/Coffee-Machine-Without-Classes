from replit import clear
import sys


off = False
enoughWater = bool
enoughCoffee = bool
enoughMilk = bool


resources = {'Water': 500, 'Milk':400, 'Coffee': 200, 'Money': 10 }

def report():
    print(f"Current resources:\nWater: {resources['Water']}ml\nMilk: {resources['Milk']}ml\nCoffee: {resources['Coffee']}g\nMoney: ${resources['Money']}")

coffee = [{'espresso': {'Water': 100, 'Milk': 30, 'Coffee': 25, 'Money': 3}},{'latte': {'Water': 80, 'Milk': 50, 'Coffee': 20, 'Money': 4}},
          {'cappuccino': {'Water': 100, 'Milk': 50, 'Coffee': 25, 'Money': 5}}]

print(coffee[0]['espresso']['Water'])


def getValCoffee(coffee_type):
    if coffee_type == "espresso":
        return coffee[0]['espresso']['Money']
    elif coffee_type == "latte":
        return coffee[1]['latte']['Money']
    elif coffee_type == "cappuccino":
        return coffee[2]['cappuccino']['Money']


def reduceResourcesAddMoney(coffee_type):
    global coffee
    global resources

    if coffee_type == "espresso":
        water = int(coffee[0]['espresso']['Water'])
        milk = int(coffee[0]['espresso']['Milk'])
        coffee_amount = int(coffee[0]['espresso']['Coffee'])
        money = int(coffee[0]['espresso']['Money'])

        resources['Water'] = resources['Water'] - water
        resources['Milk'] = resources['Milk'] - milk
        resources['Coffee'] = resources['Coffee'] - coffee_amount
        resources['Money'] = resources['Money'] + money
    elif coffee_type == "latte":
        water = int(coffee[1]['latte']['Water'])
        milk = int(coffee[1]['latte']['Milk'])
        coffee_amount = int(coffee[1]['latte']['Coffee'])
        money = int(coffee[1]['latte']['Money'])

        resources['Water'] = resources['Water'] - water
        resources['Milk'] = resources['Milk'] - milk
        resources['Coffee'] = resources['Coffee'] - coffee_amount
        resources['Money'] = resources['Money'] + money

    if coffee_type == "cappuccino":
        water = int(coffee[2]['cappuccino']['Water'])
        milk = int(coffee[2]['cappuccino']['Milk'])
        coffee_amount = int(coffee[2]['cappuccino']['Coffee'])
        money = int(coffee[2]['cappuccino']['Money'])

        resources['Water'] = resources['Water'] - water
        resources['Milk'] = resources['Milk'] - milk
        resources['Coffee'] = resources['Coffee'] - coffee_amount
        resources['Money'] = resources['Money'] + money

def check_if_enough(coffee_type):
    if coffee_type == "espresso":
        if resources['Water'] >= coffee[0]['espresso']['Water'] and resources['Water'] > 0:
            global enoughWater
            enoughWater = True
        else:
            enoughWater = False
        if coffee[0]['espresso']['Milk'] <= resources['Milk'] and resources['Milk'] > 0:
            global enoughMilk
            enoughMilk = True
        else:
            enoughMilk = False
        if coffee[0]['espresso']['Coffee'] <= resources['Coffee'] and resources['Coffee'] > 0: 
            global enoughCoffee
            enoughCoffee = True
        else:
            enoughCoffee = False
    elif coffee_type == "latte":
        if coffee[1]['latte']['Water'] <= resources['Water'] and resources['Water'] > 0:
            enoughWater = True
        else:
            enoughWater = False
        if coffee[1]['latte']['Milk'] <= resources['Milk'] and resources['Milk'] > 0:
            enoughMilk = True
        else:
            enoughMilk = False
        if coffee[1]['latte']['Coffee'] <= resources['Coffee'] and resources['Coffee'] > 0: 
            enoughCoffee = True
        else:
            enoughCoffee = False
    elif coffee_type == "cappuccino":
        if coffee[2]['cappuccino']['Water'] <= resources['Water'] and resources['Water'] > 0:
            enoughWater = True
        else:
            enoughWater = False
        if coffee[2]['cappuccino']['Milk'] <= resources['Milk'] and resources['Milk'] > 0:
            enoughMilk = True
        else:
            enoughMilk = False
        if coffee[2]['cappuccino']['Coffee'] <= resources['Coffee'] and resources['Coffee'] > 0: 
            enoughCoffee = True
        else:
            enoughCoffee = False

clear()

while True:
    try:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            sys.exit(0)
        check_if_enough(choice)
        if enoughWater == True and enoughMilk == True and enoughCoffee == True:
            print("There are enough resources to make your coffee.")
        elif enoughWater == False:
            print("Not enough water.")
            break
        elif enoughMilk == False:
            print("Not enough milk")
            break
        elif enoughCoffee == False:
            print("Not enough coffee.")
            break

        coffeeValue = getValCoffee(choice)
        print(f"Please insert coins worth ${coffeeValue}")
        quarters = int(input("Enter number of quarters($0.25): "))
        dimes = int(input("Enter number of dimes($0.10): "))
        nickles = int(input("Enter number of nickles($0.05): "))
        pennies = int(input("Enter number of pennies($0.01): "))

        moneyReceived = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        print(moneyReceived)
        if moneyReceived < coffeeValue:
            print("Sorry, not enough money. Refunding...")
            break
        elif moneyReceived == coffeeValue:
            print(f"Money received: {moneyReceived}.\nMaking coffee...")
        elif moneyReceived > coffeeValue:
            extra = moneyReceived - coffeeValue
            moneyReceived - extra
            print(f"Money received: {moneyReceived}. Refunding extra amount: {extra}...\nMaking coffee...\n\n\n")


        reduceResourcesAddMoney(choice)
        report()
        print("================================================")
        print(f"\nHere is your {choice}! Enjoy!! \n")
        print("================================================\n\n\n")

    except KeyboardInterrupt:
        print("\nThe maintainers have shut down this machine...")
        sys.exit(0)

