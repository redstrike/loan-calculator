income = int(input())

if income <= 15527:
    tax_rate = 0
elif income <= 42707:
    tax_rate = 15
elif income <= 132406:
    tax_rate = 25
else:
    tax_rate = 28

tax = round(income / 100 * tax_rate)
print(f'The tax for {income} is {tax_rate}%. That is {tax} dollars!')
