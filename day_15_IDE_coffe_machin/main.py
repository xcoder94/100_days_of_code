from recources import MENU, resources

# Variables (for remaining)
imported_res = resources
# Constants for money
QUARTER = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


# checking remains of ingredients
def check_resources(client_want, drinks, remaining):
    # print(drinks['espresso']["ingredients"]['water'])
    recipe = drinks[client_want]['ingredients']
    for i in recipe:
        if i in remaining:
            if recipe[i] > remaining[i]:
                print(f'Sorry there is not enough {i}.')
                return False
            else:
                return True


# Receive payments for drinks
def process_coins(client_want, drinks, cash):
    drink_cost = drinks[client_want]['cost']
    client_payment = 0
    quarter = int(input('How many quarters? (0.25): '))
    client_payment += QUARTER * quarter
    print(f'Your payment ${client_payment}')

    dimes = int(input('How many dimes? (0.10): '))
    client_payment += DIMES * dimes
    print(f'Your payment ${client_payment}')

    nickles = int(input('How many nickles? (0.05): '))
    client_payment += NICKLES * nickles
    print(f'Your payment ${client_payment}')

    pennies = int(input('How many pennies? (0.01): '))
    client_payment += PENNIES * pennies
    print(f'Your payment ${client_payment}')

    if client_payment >= drink_cost:
        change = client_payment - drink_cost
        print(f'Here is your {client_want} ☕ Enjoy!')
        cash += (client_payment - change)
        if change > 0:
            print(f'Here is {change} in change')
    else:
        print('Sorry that\'s not enough money. Money refunded')


def subtract_remains(client_want, drinks):
    recipe = drinks[client_want]['ingredients']
    global imported_res
    for item in recipe:
        imported_res[item] -= recipe[item]
    return imported_res


machine_is_working = True
while machine_is_working:
    customer_order = input('What would you like? (espresso/latte/cappuccino): ')
    if customer_order in MENU:
        check_resources(customer_order, MENU, imported_res)
        process_coins(customer_order, MENU, imported_res['money'])
        subtract_remains(customer_order, MENU)
    elif customer_order == 'off':
        machine_is_working = False
    elif customer_order == 'report':
        print(f"Water: {imported_res['water']}ml")
        print(f"Milk: {imported_res['milk']}ml")
        print(f"Coffee: {imported_res['coffee']}g")
        print(f"money: {imported_res['money']}$")
    else:
        print('Please enter the correct name')
