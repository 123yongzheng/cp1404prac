"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def get_incomes(months):
    incomes = []
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_report(income):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(income, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    num_months = int(input("How many months? "))
    incomes = get_incomes(num_months)
    print_report(incomes)


main()
