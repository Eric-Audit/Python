from decimal import Decimal
import locale as lc

def get_monthly_payment(loan_amount, yearly_interest, years):
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12
    monthly_payment = loan_amount * monthly_interest_rate / (1 -1 / (1 + monthly_interest_rate) ** months)
    monthly_payment = monthly_payment.quantize(Decimal("1.00"))
    return monthly_payment

def main():
    print("Monthly Payment Calculator")
    print()
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        print("DATA ENTRY")
        loan_amount = Decimal(input("Loan amount:\t\t"))
        yearly_interest = Decimal(input("Yearly interest rate:\t"))
        years = int(input("Years:\t\t\t"))
        monthly_payment = get_monthly_payment(
            loan_amount, yearly_interest, years)
        print()

        # format and display the results
        print("FORMATTED RESULTS")
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        line = "{:25} {:>15}"
        line1 = "{:25} {:>15.1%}"
        print(line.format("Loan amount:",
            lc.currency(loan_amount, grouping=True)))
        print(line1.format("Yearly interest rate", (yearly_interest/100)))
        print(line.format("Number of years:", years))
        print(line.format("Monthly payment:",
            lc.currency(monthly_payment, grouping = True)), "\n")
    
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
