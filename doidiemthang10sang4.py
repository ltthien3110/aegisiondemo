try:
    a = float(input('Score in 10: ')) 
    if 0<=a<4.0:
        print('Letter grade: F')
        print('Score in 4: 0')
    elif 4.0<=a<=5.4:
        print('Letter grade: D')
        print('Score in 4: 1.0')
    elif 5.5<=a<=6.9:
        print('Letter grade: C')
        print('Score in 4: 2.0')
    elif 7.0<=a<=8.4:
        print('Letter grade: B')
        print('Score in 4: 3.0')
    elif a<0 or a>10:
        print('Error')
    else:
        print('Letter grade: A')
        print('Score in 4:4.0')
except:
    print('Try again! Only number 0 to 10.')
    