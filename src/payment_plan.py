from dataclasses import dataclass
from decimal import Decimal

@dataclass
class PaymentPlan:
    name: str
    generated_from_mortgage: str
    term: int
    monthly_payment: Decimal
    other_payments_monthly_amount: Decimal