try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    def computepay(hours, rate):
        if hours <= 40:
            pay = hours*rate
        else:
            pay = 40*rate + 1.5*(hours-40)*rate
            return pay
    print('Pay: ', computepay(hours, rate))
except:
    print('Try again!')