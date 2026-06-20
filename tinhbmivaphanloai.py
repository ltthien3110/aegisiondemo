try:
    weight = float(input('Enter your weight in kilograms:'))
    height = float(input('Enter your height in meters:'))
    def calculate_bmi(weight, height):
        bmi = (weight/(height**2))
        return bmi
    print('BMI value ', calculate_bmi(weight, height))
except:
    print('Try again! Only number height > 0')
bmi = calculate_bmi(weight, height)
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        print('Normal')
        return Normal
    elif bmi < 30:
        print('Overweight')
        return Overweight
    else:
        print('Obese')
        return Obese
print('Get bmi category ', get_bmi_category(bmi))