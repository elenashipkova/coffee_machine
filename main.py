class CoffeeMachine:
    ESPRESSO = {
        'water': 250,
        'milk': 0,
        'coffee beans': 16,
        'disposable cups': 1,
        'money': 4
    }
    LATTE = {
        'water': 350,
        'milk': 75,
        'coffee beans': 20,
        'disposable cups': 1,
        'money': 7
    }
    CAPPUCCINO = {
        'water': 200,
        'milk': 100,
        'coffee beans': 12,
        'disposable cups': 1,
        'money': 6
    }
    COFFEE_TYPES = {
        '1': ESPRESSO,
        '2': LATTE,
        '3': CAPPUCCINO
    }
    UNITS = {
        'water': 'ml',
        'coffee beans': 'g',
        'money': '$'
    }

    def __init__(self, coffee_remains):
        self.coffee_remains = coffee_remains

    def output_remains(self):
        print(f'The coffee machine has:')
        for item, value in self.coffee_remains.items():
            if item in ('water', 'milk'):
                message = f"{value} {self.UNITS['water']} of {item}"
            elif item in 'coffee beans':
                message = f"{value} {self.UNITS['coffee beans']} of {item}"
            elif item in 'disposable cups':
                message = f'{value} {item}'
            else:
                message = f"{self.UNITS['money']}{value} of {item}"
            print(message)

    def choose_action(self):
        action = input('Write action (buy, fill, take, remaining, exit):')
        return action

    def buy_coffee(self):
        coffee_type = input('''
            What do you want to buy?
            1 - espresso,
            2 - latte,
            3 - cappuccino,
            back - to main menu:
        ''')

        if coffee_type == 'back':
            return None
        shared_dict = {}
        for i in self.coffee_remains:
            if self.coffee_remains[i] < self.COFFEE_TYPES[coffee_type][i]:
                if i == 'money':
                    continue
                shared_dict[i] = self.coffee_remains[i]
        if len(shared_dict) == 0:
            print('I have enough resources, making you a coffee!')
            for j in self.coffee_remains:
                if j == 'money':
                    self.coffee_remains[j] += self.COFFEE_TYPES[coffee_type][j]
                else:
                    self.coffee_remains[j] -= self.COFFEE_TYPES[coffee_type][j]
        else:
            shared_list = ', '.join(list(shared_dict.keys()))
            print(f'Sorry, not enough {shared_list}!')

    def fill_coffee_machine(self):
        water = int(input('Write how many ml of water you want to add:'))
        self.coffee_remains['water'] += water
        milk = int(input('Write how many ml of milk you want to add:'))
        self.coffee_remains['milk'] += milk
        coffee_beans = int(input('Write how many grams of coffee beans you want to add:'))
        self.coffee_remains['coffee beans'] += coffee_beans
        cups = int(input('Write how many disposable cups you want to add:'))
        self.coffee_remains['disposable cups'] += cups
        return None

    def withdraw_cash_from_coffee_machine(self):
        print(f"I gave you {self.UNITS['money']}{self.coffee_remains['money']}")
        self.coffee_remains['money'] = 0
        return None


def machine():
    coffee_machine = CoffeeMachine(
        {
            'water': 400,
            'milk': 540,
            'coffee beans': 120,
            'disposable cups': 9,
            'money': 550
        }
    )
    while True:
        action = coffee_machine.choose_action()
        if action == 'remaining':
            coffee_machine.output_remains()
        elif action == 'buy':
            coffee_machine.buy_coffee()
        elif action == 'fill':
            coffee_machine.fill_coffee_machine()
        elif action == 'take':
            coffee_machine.withdraw_cash_from_coffee_machine()
        elif action == 'exit':
            break


machine()
