from math import ceil

print('Enter the loan principal:')
principal = int(input())
print('What do you want to calculate?')
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
cal_type = input()

if cal_type == 'm':
    print('Enter the monthly payment:')
    monthly_payment = int(input())
    months = principal // monthly_payment
    if principal % monthly_payment != 0:
        months += 1
    print('\nIt will take', months, 'month' if months == 1 else 'months', 'to repay the loan')

elif cal_type == 'p':
    print('Enter the number of months:')
    months = int(input())
    if principal % months == 0:
        print('Your monthly payment =', principal // months)
    else:
        fixed_payment = ceil(principal / months)
        last_payment = principal - (months - 1) * fixed_payment
        print('\nYour monthly payment =', fixed_payment, 'and the last payment =', last_payment, '.')
