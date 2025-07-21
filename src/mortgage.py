from file_utils import *
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Mortgage:
    name: str
    property_price: Decimal
    down_payment: Decimal
    interest_rate: Decimal

    def __init__(self, name, property_price="0", down_payment="0", interest_rate="0"):
        self.name = name
        self.property_price = Decimal(property_price)
        self.down_payment = Decimal(down_payment)
        self.interest_rate = Decimal(interest_rate)

    def set_property_price(self, price):
        try:
            self.property_price = Decimal(price)
        except:
            raise Exception("The property price must be a Decimal number.")

    def set_down_payment(self, payment):
        try:
            self.down_payment = Decimal(payment)
        except:
            raise Exception("The down payment must be a Decimal number.")

    def set_interest_rate(self, rate):
        try:
            self.interest_rate = Decimal(rate)
        except:
            raise Exception("The interest rate must be a Decimal number.")

    def save_to_file(self):
        files_directory = "files"
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
    def get_short_form_string(self):
        return f"Name: '{self.name}' | Value: {self.property_price}"

def get_data_from_file(mortgage_name):
    with open(f"files/{mortgage_name}.mortgage.json", "r") as f:
        data = json.load(f)
        return Mortgage(**data)

def validate_mortgage_file(mortgage_name):
    try:
        get_data_from_file
    except Exception as error:
        print(f"Error! The mortgage you entered ({mortgage_name}) couldn't be found. Error message: {error}")

def read_all_mortgage_files():
    read_mortgages = []
    file_paths = get_all_mortgage_files_in_directory("files")
    for file_path in file_paths:
        with open(file_path, "r") as f:
            data = json.load(f)
            read_mortgages.append(Mortgage(**data))
    return read_mortgages