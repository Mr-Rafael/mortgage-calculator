from file_utils import *
from dataclasses import dataclass
from decimal import *
from mortgage import get_data_from_file

@dataclass
class PaymentPlan:
    name: str
    source_mortgage: str
    term_in_months: int
    monthly_payment: Decimal
    escrow_payment: Decimal

    def __init__(self, name, source_mortgage, term=0, payment=Decimal("0"), escrow=Decimal("0")):
        self.name = name
        self.source_mortgage = source_mortgage
        self.term_in_months = term
        self.monthly_payment = payment
        self.escrow_payment = escrow

    def set_term(self, term):
        self.term_in_months = int(term) * 12
    
    def set_monthly_payment(self, payment):
        self.monthly_payment = Decimal(payment)

    def set_escrow_payment(self, payment):
        self.escrow_payment = Decimal(payment)

    def save_to_file(self):
        files_directory = "files"
        file_path = f"{files_directory}/{self.name}.plan.json"
        create_directory_if_nonexistent(files_directory)
        dump_json(file_path, self)

    def generate_payment_plan(self):
        mortgage_data = get_data_from_file(self.source_mortgage)
        self.calculate_missing_value(mortgage_data)

    def calculate_missing_value(self, mortgage_data):
        if (self.term_in_months == Decimal(0) and self.monthly_payment != Decimal(0)):
            print(f"\nCalculating the term from the payment amount.")
            self.term_in_months = self.calculate_term_from_monthly_payment(mortgage_data)
        elif (self.term_in_months != Decimal(0) and self.monthly_payment == Decimal(0)):
            print(f"\nCalculating the monthly payment from the term.")
            self.monthly_payment = self.calculate_payments_from_term(mortgage_data) + self.escrow_payment
            print(f"The total monthly payment was calculated at {self.monthly_payment}")

    def calculate_payments_from_term(self, mortgage_data):
        principal = mortgage_data.property_price - mortgage_data.down_payment
        monthly_interest_rate = mortgage_data.interest_rate / Decimal(12)
        term = Decimal(self.term_in_months)
        calculation_dividend = principal * monthly_interest_rate * ((Decimal(1) + monthly_interest_rate) ** term)
        calculation_divisor = ((Decimal(1) + monthly_interest_rate) ** term) - 1
        rounded_payment = round(calculation_dividend / calculation_divisor, 2)
        print(f"The monthly payment without escrow was calculated at {rounded_payment}")
        return rounded_payment
    
    def calculate_term_from_monthly_payment(self, mortgage_data):
        principal = mortgage_data.property_price - mortgage_data.down_payment
        monthly_interest_rate = mortgage_data.interest_rate / Decimal(12)
        actual_monthly_payment = self.monthly_payment - self.escrow_payment
        calculation_dividend = Decimal.log10(actual_monthly_payment/(actual_monthly_payment - (principal * monthly_interest_rate)))
        calculation_divisor = Decimal.log10(1 + monthly_interest_rate)
        number_of_payments = round((calculation_dividend / calculation_divisor), 0)
        print(f"The loan will be paid in {number_of_payments} months, or {round(number_of_payments / 12, 2)} years.")
        return number_of_payments