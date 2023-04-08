print("Welcome to Income Tax Calculator ")

name = input("Name >>> ")
age = int(input("Age >>> "))
gender = input("gender >>> ")
yearly_income = int(input("Yearly Income >>> "))

income_tax = 0


if(age < 60):
    if (250001 < yearly_income & yearly_income < 500000):
        income_tax = yearly_income * 5 / 100
    if (500001 < yearly_income & 1000000):
        income_tax = 12500 + (yearly_income * 20 / 100)
    if(yearly_income > 1000000):
        income_tax = 112500 + (yearly_income * 30 / 100)

if(60 < age < 80):
    if (300001 < yearly_income & yearly_income < 500000):
        income_tax = yearly_income * 5 / 100
    if (500001 < yearly_income & 1000000):
        income_tax = 10000 + (yearly_income * 20 / 100)
    if(yearly_income > 1000000):
        income_tax = 110000 + (yearly_income * 30 / 100)

if(age < 60):
    # if ( 250001 < yearly_income & yearly_income < 500000):
    #     result = yearly_income * 5 / 100
    if (500001 < yearly_income & 1000000):
        income_tax = yearly_income * 20 / 100
    if(yearly_income > 1000000):
        income_tax = 100000 + (yearly_income * 30 / 100)


print("Your income tax  = ₹ " + str(income_tax))
print("")
print("Thank you  " + name + " vist again !!😎")
print("")
print("-----------------------------")
