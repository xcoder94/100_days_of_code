from recources import MENU, resources

# Variables (for remaining)
water_remaining = resources['water']
milk_remaing = resources['milk']
cofee_remaing = resources['coffee']
money = resources['money']
# Constants for money
QUARTER = 0.25
DIMES = 0.10
NICKLES = 0.05
PENIES = 0.01

# Reporting to client about remaining recources in machine
def print_report():    
    print(f'Water: {water_remaining}\nMilk: {milk_remaing}\nCoffee: {cofee_remaing}\nMoney: {money}')


# checking remains of ingrideints
def check_recources(client_want, drinks, remaining):
    # print(drinks['espresso']["ingredients"]['water'])
    resepie = drinks[client_want]['ingredients']
    for i in resepie:
        if i in remaining:
            if resepie[i] > remaining[i]:
                print(f'Sorry there is not enough {i}.')
                return False
            else:
                return True
        

# Recieve payments for drinks
def process_coins(client_want, drinks, money):
    drink_cost = drinks[client_want]['cost']
    client_payment = 0
    change = 0
    quarter = int(input('How many quarters? (0.25): '))
    client_payment += QUARTER * quarter
    print(f'Your payment ${client_payment}')

    dimes = int(input('How many dimes? (0.10): '))
    client_payment += DIMES * dimes
    print(f'Your payment ${client_payment}')

    nickles = int(input('How many nickles? (0.05): '))
    client_payment += NICKLES * nickles
    print(f'Your payment ${client_payment}')

    penies = int(input('How many penies? (0.01): '))
    client_payment += PENIES * penies    
    print(f'Your payment ${client_payment}')

    if client_payment >= drink_cost:
        change = client_payment - drink_cost
        print(f'Here is your {client_want} ☕ Enjoy!')
        money += client_payment - change
        if change > 0:
            print(f'Here is {change} in change')
    else:
        print('Sorry that\'s not enough money. Money refunded')


# process_coins('cappuccino', MENU, resources['money'])
# print_report()


machine_is_working = True
while machine_is_working:
    customer_order = input('“What would you like? (espresso/latte/cappuccino): ')
    if customer_order in MENU:
        check_recources(customer_order, MENU, resources)
        process_coins(customer_order, MENU, resources['money'])
    elif customer_order == 'off':
        machine_is_working = False
    elif customer_order == 'report':
        print_report()
    else:
        print('Please enter the correct name')

