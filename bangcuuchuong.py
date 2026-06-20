def print_table(number):
    if number < 0:
        print('Please enter a positive number.')
    else:
        for i in range(1,11):
            number*i
            print(number, 'x', i, '= ', number*i)
number = int(input('Enter your number: '))
print_table(number)
