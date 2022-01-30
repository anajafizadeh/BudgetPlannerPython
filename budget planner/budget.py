class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=''):
        new_dict = {}
        self.balance += amount
        new_dict['amount'] = amount
        new_dict['description'] = description
        self.ledger.append(new_dict)

    def withdraw(self, amount, description=''):
        new_dict = {}
        if self.check_funds(amount):
            new_dict['amount'] = amount * (-1)
            new_dict['description'] = description
            self.balance -= amount
            self.ledger.append(new_dict)
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other):
        description1 = "Transfer to " + other.category
        description2 = "Transfer from " + self.category
        if self.check_funds(amount):
            self.withdraw(amount, description1)
            other.deposit(amount, description2)
            return True
        return False

    def check_funds(self, amount):
        if self.balance - amount >= 0:
            return True
        return False

    def __str__(self):
        leading_stars = ((30 - len(self.category)) // 2) * '*'
        front_stars = (30 - (len(leading_stars) + len(self.category))) * '*'
        title = leading_stars + self.category + front_stars
        body = ''
        for ledge in self.ledger:
            if 0 < len(ledge.get('description')) <= 23:
                body += ledge.get('description') + ((24 - len(ledge.get('description'))) * ' ') + str(format(ledge.get('amount'), '.2f')) + '\n'
            elif len(ledge.get('description')) == 0:
                body += 24 * ' ' + str(format(ledge.get('amount'), '.2f')) + '\n'
            else:
                body += ledge.get('description')[0:23] + ' ' + str(format(ledge.get('amount'), '.2f')) + '\n'
        total = 'Total: ' + str(format(int(self.get_balance()), '.2f'))
        return title + '\n' + body + '\n' + total
