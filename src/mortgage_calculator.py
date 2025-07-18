import argparse
from mortgage import Mortgage, get_data_from_file

def main():
    parser = argparse.ArgumentParser(description="Mortgage Calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a new mortgage")

    edit_parser = subparsers.add_parser("edit", help="Modify an existing mortgage")
    edit_parser.add_argument("--name", type=str, required=True, help="The name of the mortgage to edit")

    args = parser.parse_args()
    
    if args.command == "create":
        create_new_mortgage()
    elif args.command == "edit":
        edit_mortgage(args.name)
        
def create_new_mortgage():
    name = input("Please enter a name for the mortgage: ")
    new_mortgage = Mortgage(name)
    new_mortgage.set_property_price(input("Please enter the property's price: "))
    new_mortgage.set_down_payment(input("Please enter the down payment: "))
    new_mortgage.set_interest_rate(input("Please enter the interest rate: "))
    new_mortgage.save_to_file()
    print(f"\nSuccessfully created a new mortgage: {new_mortgage}")

def edit_mortgage(name):
    current_mortgage = get_data_from_file(name)
    print(f"Editing Mortgage: '{name}'")
    user_input = input(f"The property's price is currently {current_mortgage.property_price}. To update, enter the new price. To leave as is, enter blank:")
    if(len(user_input) > 0):
        print(f"Updated to {user_input}.")
        current_mortgage.set_property_price(user_input)
    user_input = input(f"The down payment is currently {current_mortgage.down_payment}. To update, enter the new value. To leave as is, enter blank:")
    if(len(user_input) > 0):
        print(f"Updated to {user_input}.")
        current_mortgage.set_down_payment(user_input)
    user_input = input(f"The interest rate is currently {current_mortgage.interest_rate}. To update, enter the new rate. To leave as is, enter blank:")
    if(len(user_input) > 0):
        print(f"Updated to {user_input}.")
        current_mortgage.set_interest_rate(user_input)
    current_mortgage.save_to_file()
    print(f"\nSuccessfully updated the mortgage to: {current_mortgage}")
    

main()