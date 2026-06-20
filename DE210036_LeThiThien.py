'''
print('----ex1----')
a = float(input('Enter your number a: '))
b = float(input('Enter your number b: '))
c = float(input('Enter your number c: '))
tong = [a,b,c]
d = sum(tong)
print('Sum 3 real numbers: ', round(d,2))'''
'''
print('----ex2----')
for i in range(10):
    if i==0:
        a = 0
    else:
        a=i-1
    tong = i+a
    print('Previous: ', a,'Current: ', i,'Sum: ', tong)'''
'''
print('----ex3----')
total = 0
count = 0
while True:
    value = input('Enter a number (or Done to stop): ')
    if value == 'Done':
        break
    try:
        number = float(value)
        total = total + number
        count = count + 1
    except ValueError:
        print('Invalid input. Please enter a valid number')
if count > 0:
    average = total/count
else:
    average = 0
print('Sum: ',total,'Valid number: ',count,'Average: ', average)'''
'''print('----ex4----')
text = input('Enter a string: ')
if text == text[::-1]:
    print('This is palindrome.')
else:
    print('This is not palindrome.')'''
'''
print('----ex5----')
def display_student(name, age=18):
    print('Name: ', name)
    print('Age: ', age)
display_student('Thien')
display_student('Thien',19)
def outer_function(a,b):
    def inner_function():
        c = a + b
        return c
    d = inner_function() + 5
    return d
result = outer_function(15,15)
print('Result: ',result)'''
'''
print('----ex6----')
def number(*args):
    total = sum(args)
    maximum = max(args)
    return total, maximum
numbers = number
total, maximum = numbers(10, 12, 36, 40)
print('Sum: ', total)
print('Max: ', maximum)
def recursive(n):
    if n==0:
        return 0
    else:
        a = n + recursive(n - 1)
        return a
sumrecursive = recursive(10)
print('Sum recursive from 0 to 10: ', sumrecursive)'''
'''
print('----ex7----')
text = 'X-DSPAM-Confidence: 0.8475'
found = text.find(':')
n = text[found+1:]
m = n.strip()
number = float(m)
print('Position: ',found,'Before strip: ', n, 'After strip: ', m,'Float value: ', number)'''
'''
print('----ex8----')
while True:
    try:
        c = float(input('Enter temperature in C: '))
        f = c*1.8 + 32
        print(round(f,2), '\u00B0F')
        break
    except ValueError:
        print('Please enter valid temperature')'''
