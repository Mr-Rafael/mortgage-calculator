from file_utils import *
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Mortgage:
    name: str
    property_price: Decimal
    down_payment: Decimal
    interest_rate: Decimal

    def __init__(self, name):
        self.name = name
        self.property_price = Decimal("0")
        self.down_payment = Decimal("0")
        self.interest_rate = Decimal("0")

    def __init__(self, name, property_price, down_payment, interest_rate):
        self.name = name
        self.property_price = Decimal(property_price)
        self.down_payment = Decimal(down_payment)
        self.interest_rate = Decimal(interest_rate)

    def set_property_price(self, price):
        self.property_price = Decimal(price)

    def set_down_payment(self, payment):
        self.down_payment = Decimal(payment)

    def set_interest_rate(self, rate):
        self.interest_rate = Decimal(rate)

    def save_to_file(self):
        files_directory = "../files"
        file_path = f"{files_directory}/{self.name}.mortgage.json"
        create_directory_if_nonexistent(files_directory)
        dump_json(file_path, self)

    def __repr__(self):
        return f'''
        \n-----| Mortgage: {self.name} |-----
        \nProperty Price: {self.property_price}
        \nDown Payment: {self.down_payment}
        \nInterest Rate: {self.interest_rate}
        '''

def get_data_from_file(mortgage_name):
    with open(f"../files/{mortgage_name}.mortgage.json", "r") as f:
        data = json.load(f)
        return Mortgage(**data)