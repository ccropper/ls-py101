# define helper functions
def prompt(msg):
    return ">> " + msg + "\n"


def validate_input_is_positive_number(num):
    try:
        num = float(num)
    except ValueError:
        return False

    return bool(num > 0)


# get inputs
loan_amount = input(prompt("What is the amount ($) of your loan?"))

while validate_input_is_positive_number(loan_amount) is False:
    loan_amount = input(prompt("Please enter a valid amount for your loan."))

apr = input(prompt("What is the Annual Percentage Rate (%) of your loan?"))

while validate_input_is_positive_number(apr) is False:
    apr = input(prompt("Please enter a valid percentage number for your APR."))

loan_duration_years = input(prompt("What is the duration (in years) of your loan?"))

while validate_input_is_positive_number(loan_duration_years) is False:
    loan_duration_years = input(prompt("Please enter a valid duration for your loan."))

# process these inputs
loan_amount = float(loan_amount)
apr = float(apr) / 100
loan_duration_years = float(loan_duration_years)

mpr = apr / 12
loan_duration_months = loan_duration_years * 12

monthly_payment = loan_amount * (mpr / (1 - (1 + mpr) ** (-loan_duration_months)))

# display result
print(prompt(f"Your monthly payment is ${monthly_payment:.2f}."))
