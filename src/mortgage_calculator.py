import argparse
from mortgage import Mortgage, get_data_from_file, read_all_mortgage_files

def main():
    parser = argparse.ArgumentParser(description="Mortgage Calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a new mortgage")

    edit_parser = subparsers.add_parser("edit", help="Modify an existing mortgage")
    edit_parser.add_argument("--name", type=str, required=True, help="The name of the mortgage to edit")
    
    view_parser = subparsers.add_parser("view", help="View information on an existing mortgage")
    view_parser.add_argument("--name", type=str, required=True, help="The name of the mortgage to view")

    viewall_parser = subparsers.add_parser("viewall", help="View information on all saved mortgages")

    generate_plan_parser = subparsers.add_parser("generate-payment-plan", help="Generate a payment plan based on a Mortgage")
    generate_plan_parser.add_argument("--name", type=str, required=True, help="The name of the mortgage used to generate the plan")

    args = parser.parse_args()
    
    if args.command == "create":
        create_new_mortgage()
    elif args.command == "edit":
        edit_mortgage(args.name)
    elif args.command == "view":
        view_mortgage(args.name)
    elif args.command == "viewall":
        view_all_mortgages()
    elif args.command == "generate-payment-plan":
        generate_payment_plan(args.name)
        
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

def view_mortgage(name):
    current_mortgage = get_data_from_file(name)
    print(f"Viewing Mortgage '{name}'{current_mortgage}")

def view_all_mortgages():
    print(f"Looking for mortgages in the files directory...")
    mortgage_list = read_all_mortgage_files()
    print(f"\nFound the following saved mortgages:\n")
    for mortgage in mortgage_list:
        print(f"- {mortgage.get_short_form_string()}")
    print("")

def generate_payment_plan(mortgage_name):
    name = input("Please enter a name for the payment plan:")

def list_to_string(list_to_print):
    return_string = ""
    for element in list_to_print:
        return_string += f"\n- {element}"
    return return_string

main()