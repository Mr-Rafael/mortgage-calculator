from file_utils import *
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class PaymentPlan:
    name: str
    source_mortgage: str
    term: int
    monthly_payment: Decimal
    escrow_payment: Decimal

    def __init__(self, name, source_mortgage, term=0, payment=Decimal("0"), escrow=Decimal("0")):
        self.name = name
        self.source_mortgage = source_mortgage
        self.term = term
        self.monthly_payment = payment
        self.escrow_payment = escrow

    def set_term(self, term):
        self.term = term
    
    def set_monthly_payment(self, payment):
        self.monthly_payment = Decimal(payment)

    def set_escrow_payment(self, payment):
        self.escrow_payment = Decimal(payment)

    def save_to_file(self):
        files_directory = "files"
        file_path = f"{files_directory}/{self.name}.plan.json"
        create_directory_if_nonexistent(files_directory)
        dump_json(file_path, self)