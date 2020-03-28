#dictionary
dicto={
  'a':[1,2,3],
  'b':'Name',
  'c':3
}
print(dicto['c'])
print(dicto)
my_list=[
  {
  'a':[1,2,3],
  'b':'Name',
  'c':3
  },
  {
  'd':[1,2,3],
  'e':'Name',
  'f':3
  }
]
print(my_list)
print(my_list[0]['b'])
#using dict()
Dict={}
print(Dict)
Dict=dict({
  'a':[1,2,3],
  1:'Bloodseeker'
})
print(Dict)
#using as a pair
Dict=dict([('a',[1,2,3]),(2,'Silencer')])
print(Dict)
#get access to dictionary item
print(Dict.get(3,'Drow'))
#find items
print(2 in Dict.keys())
print('Drow' in Dict.values())
print(Dict.items())
#copy dictionary
Dict1=Dict.copy()
print(Dict1)
print(len(Dict))
print(Dict)
#remove
print(Dict1.pop(2))
print(Dict1.pop(3,'No value'))
print(Dict1)
print(Dict)
print(Dict.popitem())
print(Dict)
#update
print(Dict.update({
  'agility':'Bloodseeker',
  'strength':'Wraith king'
}))
print(Dict)
print(len(Dict))#length of Dictionary
print(type(Dict))
#Tuples
my_tupules=(1,2,3,3,4,5)#no sort,reverse but more faster
print(my_tupules)
print(my_tupules[0])
print(3 in my_tupules)
user={
  (1,2):'Raisa',#tupules can be used as key
  True:'hi'
}
print(user)
print(user[(1,2)])
print(my_tupules[1:3])
#tuplues has also properties like list unpacking
print(my_tupules.count(3))
print(my_tupules.index(3))
print(len(my_tupules))
#sets
my_set={1,2,3,4,5,5}
print(my_set)
my_set.add(100)
my_set.add(2)
print(my_set)
my_list=[1,2,3,4,5,5,5]
print(set(my_list))#list to set
print(1 in my_set)
print(len(my_set))
new_set =my_set.copy()
print(list(new_set))#set to list
#my_set.clear()
sets={1,2,3,5,6,7}
print(sets.difference(my_set))#difference duita set er modhe
# print(my_set.discard(5))
# print(my_set)
print(sets.difference_update(my_set))
print(my_set)#difference ta print kore sets er
print(sets)
print(sets.intersection(my_set))#common duita sets er moddhe
print(my_set.isdisjoint(sets))#common thkle false debe r na hole true
print(my_set|sets)
#my_set.union (sets) same
seta={1,2,3,4,5}
setb={2,3}
print(setb.issubset(seta))
print(setb.issuperset(seta))
print(seta.issuperset(setb))
