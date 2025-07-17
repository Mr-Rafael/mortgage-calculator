import argparse
from mortgage import Mortgage

def main():
    print(f"Starting the program.")
    parser = argparse.ArgumentParser(description="Mortgage Calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a new mortgage")

    print(f"parsing the arguments")
    args = parser.parse_args()
    print(f"finished parsing the arguments")

    if args.command == "create":
        create_new_mortgage()
        
        
def create_new_mortgage():
    name = input("Please enter a name for the mortgage: ")
    new_mortgage = Mortgage(name)
    new_mortgage.set_property_price(input("Please enter the property's price: "))
    new_mortgage.set_down_payment(input("Please enter the down payment: "))
    new_mortgage.set_interest_rate(input("Please enter the interest rate: "))
    new_mortgage.save_to_file()
    print(f"\nSuccessfully created a new mortgage: {new_mortgage}")

main()