data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
tim = data.find('.')
print(tim)
timm = data.find('@',tim)
print(timm)
host = data[tim+1:timm]
print(host)