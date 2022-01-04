#Given constants
rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

#Taking input from the user
gross_income = float(input("\nEnter your gross income : "))
number_of_dependents = int(input("Enter number of dependents : "))

#Calculation tax
taxable_income = round(gross_income-standard_deduction-(dependent_deduction*number_of_dependents), 1)
tax = taxable_income*rate
if tax <0 :
    tax = 0

#Output
print("Your tax is $",tax,"\n")