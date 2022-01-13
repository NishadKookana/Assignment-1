#Question 2

standard_deduction=10000
dependent_deduction=3000
#Dependent deduction is deduction per head

gross_income=float(input("Enter your gross income= "))
dependents=int(input("Enter number of dependents= "))

taxable_income= gross_income-standard_deduction-(dependent_deduction*dependents)
tax=taxable_income*0.2
print("Your income tax is= ",tax)
