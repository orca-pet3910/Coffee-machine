from data import MENU, resources


def report():
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"money: {resources['money']}")


def ingredient_check(product):
    result = ''
    can_make = True
    # if resources['water'] - MENU[product]['water'] < 0:
    #     result += "There's not enough water\n"
    #     can_make = False
    for ingredient in MENU[product]['ingredients']:
        if resources[ingredient] - MENU[product]['ingredients'][ingredient] < 0:
            result += f"There's not enough {ingredient}\n"
            can_make = False
    return [can_make, result]


def insert_coins(product):
    pennies = int(input("please insert your pennies "))
    nickels = int(input("please insert your nickels "))
    dimes = int(input("please insert your dimes "))
    quarters = int(input("please insert your quarters "))
    money_inserted = pennies*0.01 + nickels*0.05 + dimes*0.1 + quarters*0.25
    return money_inserted - MENU[product]['cost']


def brew_coffee(product):
    for ingredient in MENU[product]['ingredients']:
        resources[ingredient] -= MENU[product]['ingredients'][ingredient]
    resources['money'] += MENU[product]['cost']
    print("here is your coffee: ☕ enjoy!")


print("Hello! What do you want to order?")
while True:
    order = input("(quit/espresso/latte/cappuccino/water) ")
    if order == 'quit':
        break
    elif order == 'report':
        report()
    elif order in MENU:
        can_we_make = ingredient_check(order)
        if can_we_make[0]:
            change = insert_coins(order)
            if change >= 0:
                if change > 0:
                    print(f'here is ur change: {change}$')
                brew_coffee(order)
            else:
                print('sorry, that\'s not enough money, returning credits')
        else:
            print(can_we_make[1])
    else:
        print("Sorry, that item isn't on the list.")
