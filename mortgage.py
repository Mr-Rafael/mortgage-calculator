class Mortgage:
    def __init__(self, name):
        self.name = name
        self.property_price = 0
        self.down_payment = 0
        self.interest_rate = 0

    def set_property_price(self, price):
        self.property_price = price

    def set_down_payment(self, payment):
        self.down_payment = payment

    def set_interest_rate(self, rate):
        self.interest_rate = rate

    def __repr__(self):
        return f'''
        \n-----| Mortgage: {self.name} |-----
        \nProperty Price: {self.property_price}
        \nDown Payment: {self.down_payment}
        \nInterest Rate: {self.interest_rate}
        '''