def main():
    print("This is a monthly payment calaulator")
    print("")
    
    principal = float(input("enter the loan number: "))
    apr = float(input("enter the annual payment interest: "))
    years = int(input("enter the number of years: "))
    
    monthly_interet_rate = apr / 1200
    the_number_of_months = years*12
    monthly_payment = principal * monthly_interet_rate / (1-(1+monthly_interet_rate)** (-the_number_of_months))
    print("The monthly payment is: %.2f"% monthly_payment)
main()