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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0
def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    if user_input == "off":
        print("Shutting off. Goodbye!")
        return 0
    elif user_input == "report":
        print("Water: " + str(resources["water"])+"ml")
        print("Milk: " + str(resources["milk"])+"ml")
        print("Coffee: " + str(resources["coffee"])+"g")
        print("Money: $" + str(money))
    elif user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
        for ingredient in ["water", "milk", "coffee"]:
            if MENU[str(user_input)]["ingredients"][ingredient] > resources[ingredient]:
                print("Sorry, there is not enough" + [ingredient])
                break
        print("Please insert coins")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels?"))
        pennies = int(input("How many pennies?"))
        total = .25*quarters + .1*dimes + .05*nickels + .01*pennies
        print("Your total is:", total)
coffee_machine()
