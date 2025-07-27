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
python3 mortgage-calculator edit --name <mortgage name>
```

The program will run you through all the fields. You can either enter a new value to update it, or just press enter to leave it as it is.

### View a Mortgage

Prints the mortgage information in a readable format.

```
python3 mortgage-calculator view --name <mortgage name>
```

### View All Mortgages

Prints brief information on all the mortgages stored in the data/mortgages folder. 

```
python3 mortgage-calculator viewall
```

### Generate a Payment Plan

Payment plans are level payment plans (the same amount every month), generated based on a previously saved mortgage. They can be based on:

- A payment term. For example, "I want to pay the mortgage in **20 years**".
- A payment amount. For example, "I want to make payments of **1,000 monthly**".

Generate a plan from a mortgage:

```
python3 mortgage_calculator generate-payment-plan --mortgage <mortgage name>
```

The program will prompt you for all the necessary information (whether the plan is based on term or amount, insurance payments, etc.)

The payment plan will be stored in CSV format in the *files* folder with the payment plan. The payment plan details (term, monthly payment, etc.) will also be stored in JSON format. This can later be used to make modifications on the payment plans.

### Add Extraordinary Paydowns

Work In Progress

Will allow you to add extraordinary paydowns to an existing Payment Plan. This will allow you to see how much the term shortens, how the interest paid is reduced, etc.