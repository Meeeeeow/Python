# password checker practise
username = input('please enter your Name: ')
password = input('Your Password: ')
length = len(password)
encrypt = '*' * length
# print(encrypt)
print(f'Greetings,Hooman!!{username}.Your Password {encrypt} is {length} letters long')
# list

cart = ['Books', 'Cheese', 'cat food', 'tissue', 'sanitizers']
print(cart)
print(cart[0])
print(cart[0:2])
print(cart[0:])
print(cart[2:])
print(cart[-1])
print(cart[::2])
print(cart[::-1])
# user input using loop
books = []
number = int(input('enter how many you want?'))
for i in range(0, number):
    books.append(input())

print(books)
print(books[0])
print(books[0:])
print(books[0:number])
print(books[:number])
print(books[::-1])
# user input using try catch
language = []
try:
    while True:
        language.append(int(input()))
except:
    print(language)
    print(language[0])
    print(language[0:len(language)])
    print(language[1:len(language)])
    print(language[::-1])
# list of lists as input

code = []
number = int(input('enter how many you want?'))
for i in range(0, number):
    ele = [input(), float(input())]
    code.append(ele)
print(code)
print(code[0])
print(code[::-1])
# not immutable
code[0] = 'python', 4.1
print(code)
print(code[0])
# copying list
books = language[:]
books[0] = 1
print(books)
print(language)
# modifying list
books = language
books[0] = 32
print(books)
print(language)
# matrix
matrix = [
    [1, 5, 4],
    [2, 3, 5]
]
print(matrix[0][1])

# user input matrix
matrix1 = []
R = int(input('Enter row:'))
C = int(input('Enter column:'))

for i in range(0, R):
    a = []
    for i in range(0, C):
        a.append(int(input()))
    matrix1.append(a)

# print matrix
for i in range(0, R):
    for j in range(0, C):
        print(matrix1[i][j], end=' ')
#   print()  #new line
# list method
# add
basket = [1, 2, 54, 6, 3, 45]
basket.append(199)
newlist = basket
print(newlist)
print(basket)

basket.insert(2, 50)
print(basket)
basket.extend([100, 110])
print(basket)

# removing
basket.pop()
print(basket)
basket.pop(1)
print(basket)
basket.remove(3)
print(basket)
new = basket.pop()
print(new)
new1 = basket.remove(1)
print(new1)
print(basket)
# to find a value
basket1 = ['a', 'b', 'c', 'd', 'e']
print(basket1.index('c'))
print(basket1.index('c', 0, 3))
# basket1.index('c',0,2) error
if 'x' in basket1:
    print(basket1.index('d'))
else:
    print(f'the word is not here!')
print(basket1.count('d'))
# sort
# basket.sort() main list ke modify kore
print(sorted(basket))  # main er copy banai
print(basket)  # main ta thk e ache
# reverse list
basket.sort()
basket.reverse()
print(basket)
# join die list of items add kora hoi
new_sentence = ' '.join(['hi', 'i', 'am', 'X'])
print(new_sentence)
ne = basket1[0].join(['ho', 'ho', 'ho'])
print(ne)
# list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

# password checker practise
username = input('please enter your Name: ')
password = input('Your Password: ')
length = len(password)
encrypt = '*' * length
# print(encrypt)
print(f'Greetings,Hooman!!{username}.Your Password {encrypt} is {length} letters long')
# list

cart = ['Books', 'Cheese', 'cat food', 'tissue', 'sanitizers']
print(cart)
print(cart[0])
print(cart[0:2])
print(cart[0:])
print(cart[2:])
print(cart[-1])
print(cart[::2])
print(cart[::-1])
# user input using loop
books = []
number = int(input('enter how many you want?'))
for i in range(0, number):
  books.append(input())

print(books)
print(books[0])
print(books[0:])
print(books[0:number])
print(books[:number])
print(books[::-1])
# user input using try catch
language = []
try:
  while True:
    language.append(int(input()))
except:
  print(language)
  print(language[0])
  print(language[0:len(language)])
  print(language[1:len(language)])
  print(language[::-1])
# list of lists as input

code = []
number = int(input('enter how many you want?'))
for i in range(0, number):
  ele = [input(), float(input())]
  code.append(ele)
print(code)
print(code[0])
print(code[::-1])
# not immutable
code[0] = 'python', 4.1
print(code)
print(code[0])
# copying list
books = language[:]
books[0] = 1
print(books)
print(language)
# modifying list
books = language
books[0] = 32
print(books)
print(language)
# matrix
matrix = [
  [1, 5, 4],
  [2, 3, 5]
]
print(matrix[0][1])

# user input matrix
matrix1 = []
R = int(input('Enter row:'))
C = int(input('Enter column:'))

for i in range(0, R):
  a = []
  for i in range(0, C):
    a.append(int(input()))
  matrix1.append(a)

# print matrix
for i in range(0, R):
  for j in range(0, C):
    print(matrix1[i][j], end=' ')
#   print()  #new line
# list method
# add
basket = [1, 2, 54, 6, 3, 45]
basket.append(199)
newlist = basket
print(newlist)
print(basket)

basket.insert(2, 50)
print(basket)
basket.extend([100, 110])
print(basket)

# removing
basket.pop()
print(basket)
basket.pop(1)
print(basket)
basket.remove(3)
print(basket)
new = basket.pop()
print(new)
new1 = basket.remove(1)
print(new1)
print(basket)
# to find a value
basket1 = ['a', 'b', 'c', 'd', 'e']
print(basket1.index('c'))
print(basket1.index('c', 0, 3))
# basket1.index('c',0,2) error
if 'x' in basket1:
  print(basket1.index('d'))
else:
  print(f'the word is not here!')
print(basket1.count('d'))
# sort
# basket.sort() main list ke modify kore
print(sorted(basket))  # main er copy banai
print(basket)  # main ta thk e ache
# reverse list
basket.sort()
basket.reverse()
print(basket)
# join die list of items add kora hoi
new_sentence = ' '.join(['hi', 'i', 'am', 'X'])
print(new_sentence)
ne = basket1[0].join(['ho', 'ho', 'ho'])
print(ne)
# list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

