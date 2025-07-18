# mortgage-calculator
Useful tools for mortgage-related calculations:

- Calculating how many years the repayment will take, depending on monthly payments and paydowns.
- Calculating how much the property will actually cost after making all the payments.
- Calculating how much money was lost to interest.
- Currently only supports level payments.

## Program commands:

### Create a Mortgage

Creates a new Mortgage, and saves it as a .json file. The mortgage can then be used to make a payment plan.

Just run:

```
python3 mortgage-calculator create
```

And the program will ask you the necessary information (name, total amount, down payment, interest rate, etc.).

### Edit a Mortgage

Edit the data of a Mortgage. Run:

```
python3 mortgage-calculator edit <mortgage name>
```

The program will run you through all the fields. You can either enter a new value to update it, or just press enter to leave it as it is.

### View a Mortgage

Prints the mortgage information in a readable format.

```
python3 mortgage-calculator view <mortgage name>
```

### View All Mortgages

Prints brief information on all the mortgages stored in the data/mortgages folder. 

```
python3 mortgage-calculator viewall
```

1. Generate a Payment Plan, based on a Time input (**Inputs**: *Mortgage name*).
    1. Ask the user for an intended time to pay the loan, and calculate a monthly payment plan.
    1. Ask the user for a name to save the plan.
    1. If already exists, ask the user if it should be overwritten.

1. Generate a Payment Plan, based on a Monthly amount.
    1. Ask the user for an intended monthly amount, then generate a payment plan and the duration of the loan.
    1. Outputs: csv with all the payments, amount of payments, length of time and interest paid.
    1. Should have some sort of safeguard if the user enters an amout that would take too long to pay. Don't allow loans longer than 50 years.

1. Add one or several capital payments to a plan (**Input**: *Plan name*).
    1. With an already generated plan, the user can insert extraordinary capital payments on specific dates.
    1. The program must re-calculate the payment plan from the Capital Payment onwards, and recalculate all the outputs.
    1. User is prompted to either save this new plan in a new file, or overwrite the existing one.
    1. User is prompted to insert more capital payments, or finish.

1. Integrity check: Open a Plan and check if it makes sense. If it has been edited or something doesn't make sense, recalculate the plan from that point onwards.

