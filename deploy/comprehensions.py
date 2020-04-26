from functools import reduce
lists=[]
n=int(input())
for i in range(0,n):
  lists.append(int(input()))
li=[]
for i in range(0,n):
  li.append(int(input()))
#lambda expressions
#hocche annonymous function type jtake 1 bar execute korar por interpreter r mone rakhbe na  one time use eta chinese maal
#lambda param :action(param)

print(list(map(lambda item:item*3,lists)))#lamda die ei function gula one time hoe gelo jshb function  one time use korte hbe shegular jnne lambda use kora easy
print(list(filter(lambda item:item%2==0 ,lists)))
print(reduce(lambda acc,item:acc+item,lists))

#lambda exercise
#square the list
print(list(map(lambda item:pow(item,2),lists)))
#list Sorting
li1=[]
li1=list(zip(lists,li))
print(li1)
li1.sort(reverse=True)#desc boro theke choto
print(li1)
li1.sort(key=lambda item:item)#asc choto theke boro but key hocche 2nd value onujai sort hbe
print(li1)

#list comprehension
#list1=[variable Name(jta ekta expression hishebe use kora jete parre like var_name**2)for variable name in iterable(mane elkhane loop ghurbe) condition]
list1=[num**2 for  num in  range(0,100) if num%2 == 0]
print(list1)
list1=[num**2 for  num in  range(0,100) ]
print(list1)
list1=[num for  num in  range(0,100) ]
print(list1)
list1=[num for  num in  'Jill Valentine' ]
print(list1)
#set comprehension same as list just {}
set1={num for  num in  'Jill Valentine' }#defference ektai set only unique nai no duplicates
print(set1)
list1={num**2 for  num in  range(0,100) if num%2 == 0}#1st bracket object create hoi er address debe she
print(list1)
#dict comprehension

simple_dict={
  'a':1,
  'b':2
}
my_dict ={key:value**2 for key,value in simple_dict.items()}
print(my_dict)
my_dict ={key:value**2 for key,value in simple_dict.items() if value%2 == 0}
print(my_dict)
my_dict={num:num**2 for num in lists}
print(my_dict)
my_dict={num:num+'1' for num in set1}
print(my_dict)
#exercise
#print the duplicate value only once
somelist=['a','b','c','b','d','m','n','n']
duplicates= list(set([item for item in somelist if somelist.count(item)>1]))
print(duplicates)