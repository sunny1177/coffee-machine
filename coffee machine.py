logo = """
 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗      ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝      ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                             
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def is_sufficient(order_items):
    for item in order_items:
        if order_items[item] >= resources[item]:
            print(f"Sorry out of {item}")
            return False
    return True


def process_coins():
    total = int(input("Insert some quarters"))*0.25
    total += int(input("Insert some dimes"))*0.1
    total += int(input("Insert some nickels"))*0.05
    total += int(input("Insert some pennies"))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is you change sir {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry not enough money to buy a drink.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

print(logo)
order = True
while order:
    user = input("What you would like drink today sir?(cappuccino/latte/expresso) : ").lower()
    if user == "off":
        order = False
    elif user == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"water:{water}ml\nmilk:{milk}ml\ncoffee:{coffee}ml\nPROFIT = {profit}$")
    else:
        drink = MENU[user]
        if is_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user, drink['ingredients'])
