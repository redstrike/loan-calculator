number = float(input())
decimal_count = int(input())

print(f'{number:.{decimal_count}f}')
# print('{0:.{1}f}'.format(number, decimal_count))
# print('%.{}f'.format(decimal_count) % number)
