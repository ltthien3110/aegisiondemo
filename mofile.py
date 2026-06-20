def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
year_list = list()
while True:
    y = input('Enter a year: ')
    if y == 'done':
        break
    y = int(y)
    year_list.append(y)
for year in year_list:
    if check_leap_year(year):
        print('Leap year: ', year)
print('Lastest year: ', max(year_list))
print('Oldest year: ', min(year_list))
