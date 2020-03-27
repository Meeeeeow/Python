import datetime
name ='iTAAALY'
print(name)
print(name[0])
print(name[0:5])
print(name[:3])
print(name[3:])
print(name[0:5:1])
print(name[::2])
print(name[:-3])
print(name[::-1])
print(name+' is in a big mess')

#build in function
print(len(name))
print(name[:])
#string methods
print(name.capitalize())#1st character will be upper case
print(name.casefold())#convert string to lower case
print(name.upper())
print(name.lower())
print(name.count('A'))
print(name.find('L'))
print(name.replace('A','K',2))
print(name.index('A'))
name1 ="raisa"
name2 ='12345'
print(name1.islower())
print(name2.isdecimal())
print(name2.isdigit())
print(name1.isdecimal())
#print age using datetime
birth_year = input('what year were you born?')
print(birth_year)
now=datetime.datetime.now()
curr_year = now.year
print(curr_year)
age = curr_year - int(birth_year)
print(f'your age is:{age}')