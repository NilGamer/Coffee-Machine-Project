# Starting data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# money values
quarter_value = 0.25
dimes_value = 0.1
nickel_value = 0.05
pennies_value = 0.01


def get_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\nMoney: ${profit}")


def check_resources(coffee):
    water_left = resources['water'] - MENU[coffee]['ingredients']['water']
    milk_left = resources['milk'] - MENU[coffee]['ingredients']['milk']
    coffee_left = resources['coffee'] - MENU[coffee]['ingredients']['coffee']

    if water_left < 0:
        return 'water'
    elif milk_left < 0:
        return 'milk'
    elif coffee_left < 0:
        return 'coffee'
    else:
        return False


def deduct_resource(coffee):
    resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']


def process_coins(coffee):
    print('Please insert coins.')
    quarters = float(input('how many quarters?: '))
    dimes = float(input('how many dimes?: '))
    nickles = float(input('how many nickles?: '))
    pennies = float(input('how many pennies?: '))

    money_got = (quarters * quarter_value) + (dimes * dimes_value) + (nickles * nickel_value) + \
                (pennies * pennies_value)

    change_left = money_got - MENU[coffee]['cost']
    global profit
    profit += MENU[coffee]['cost']
    return round(change_left, 2)


while True:
    userInput = input("What would you like? (espresso/latte/cappuccino): ")

    if userInput == "report":
        get_report()
    elif userInput == "off":
        break
    elif userInput == 'espresso' or userInput == 'latte' or userInput == 'cappuccino':
        # check resources
        resource_not_available = check_resources(userInput)
        if resource_not_available:
            print(f"Sorry there is not enough {resource_not_available}")
            continue
        else:
            # Process Coins
            change = process_coins(userInput)

            if change > 0:
                deduct_resource(userInput)
                print(f"Here is ${change} dollars in change.")
                print("Thank you for waiting..")
                print(f"Here is your special {userInput} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue
