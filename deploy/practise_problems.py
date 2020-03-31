is_magician=True
is_expert=False

if is_magician and is_expert:
  print("you are a master magician")
elif is_magician and not is_expert:
  print("at least you are getting there")
else:
  print("you need magic power")

#counter
numbers=[]
n=int(input('Enter how many u want to put?'))
for i in range(0,n):
  numbers.append(int(input()))
sum=0
for item in numbers: #i in range(0,len(numbers)):
  sum+=item
print(f'sum is: {sum}')

#find duplicate

letters=[]
check=0
duplicates=[]
n=int(input('enter how many u want to push:'))
for i in range(0,n):
  letters.append(input())
for item in letters:
  check=letters.count(item)
  if(check>1):
    if item not in duplicates:
      duplicates.append(item)
print(duplicates)

# for loops
str = 'Zero to mastery'
for i in range(0, len(str)):
    print(i, str[i])
# dictianry in a for loops
user = {
    'name': 'Golem',
    'age': '23'

}
for item in user.items():
    print(item)

# another one
for item in user.values():
    print(item)
for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)
# range
for i in range(10, 0, -1):
    print(i)  # print(list(range(10)))quick way to create a list
    # enumerate
for i, char in enumerate((1, 2, 3)):
    print(i, char)
num = list(range(100))
for i in range(0, len(num)):
    if (num[i] == 50):
        print(i, num[i])
# using enumerate
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i, char)
# Pattern
# if 0->print' '
# if 1 -> *
pattern = []
fill = '*'
empty = ' '
s = int(input('how many lists do u want'))
for i in range(s):
    str1 = input()

    pattern.append(str1.split())
for item in pattern:
    # print(item)
    for pixels in item:
        if (pixels == '1'):
            print(fill, end='')
        else:
            print(empty, end='')
    print('')





