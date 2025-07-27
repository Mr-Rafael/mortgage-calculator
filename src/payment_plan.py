from file_utils import *
from dataclasses import dataclass
from decimal import *
from mortgage import get_data_from_file
from enum import Enum

class CSVColumns(Enum):
    PAYMENT_ID = 0
    PRINCIPAL = 1
    PAYDOWN = 2
    INTEREST = 3
    INSURANCE_AND_OTHERS = 4
    PAYMENT_AMOUNT = 5

@dataclass
class PaymentPlan:
    name: str
    source_mortgage: str
    term_in_months: int
    monthly_payment: Decimal
    escrow_payment: Decimal
    total_paid_amount: Decimal
    total_escrow_paid: Decimal
    total_interest_paid: Decimal

    def __init__(self, name, source_mortgage, term=0, payment=Decimal("0"), escrow=Decimal("0")):
        self.name = name
        self.source_mortgage = source_mortgage
        self.term_in_months = term
        self.monthly_payment = payment
        self.escrow_payment = escrow
        self.total_paid_amount = Decimal(0)
        self.total_escrow_paid = Decimal(0)
        self.total_interest_paid = Decimal(0)

    def set_term(self, term):
        self.term_in_months = int(term) * 12
    
    def set_monthly_payment(self, payment):
        self.monthly_payment = Decimal(payment)

    def set_escrow_payment(self, payment):
        self.escrow_payment = Decimal(payment)

    def save_to_file(self):
        files_directory = "files"
        json_file_path = f"{files_directory}/{self.name}.plan.json"
        csv_file_path = f"{files_directory}/{self.name}.table.csv"
        create_directory_if_nonexistent(files_directory)
        dump_json(json_file_path, self)
        dump_csv(csv_file_path, self.payment_table)

    def generate_payment_plan(self):
        mortgage_data = get_data_from_file(self.source_mortgage)
        self.calculate_missing_value(mortgage_data)
        self.calculate_totals(mortgage_data)
        self.payment_table = self.generate_payment_table(mortgage_data)

    def calculate_totals(self, mortgage_data):
        self.total_paid_amount = self.monthly_payment * self.term_in_months
        self.total_escrow_paid = self.escrow_payment * self.term_in_months
        self.total_interest_paid = self.total_paid_amount - mortgage_data.property_price - self.total_escrow_paid

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
        return int(number_of_payments)
    
    def convert_to_table_value(self, decimal):
        return f"{round(decimal, 2)}"
    
    def generate_payment_table(self, mortgage_data):
        payment_matrix = [["Payment ID", "Principal", "Paydown", "Interest", "Insurance and Others", "Payment Amount"]]
        current_principal = mortgage_data.property_price - mortgage_data.down_payment
        monthly_interest_rate = mortgage_data.interest_rate / Decimal(12)
        
        for i in range(1, self.term_in_months + 1):
            payment_row = [None] * len(CSVColumns)
            payment_row[CSVColumns.PAYMENT_ID.value] = i

            interest = current_principal * monthly_interest_rate
            payment_row[CSVColumns.PAYDOWN.value] = self.convert_to_table_value(self.monthly_payment - self.escrow_payment - interest)

            current_principal -= self.monthly_payment - self.escrow_payment - interest
            payment_row[CSVColumns.PRINCIPAL.value] = self.convert_to_table_value(current_principal)

            payment_row[CSVColumns.INTEREST.value] = self.convert_to_table_value(interest)
            
            payment_row[CSVColumns.INSURANCE_AND_OTHERS.value] = self.convert_to_table_value(self.escrow_payment)
            payment_row[CSVColumns.PAYMENT_AMOUNT.value] = self.convert_to_table_value(self.monthly_payment)
            payment_matrix.append(payment_row)

        return payment_matrix