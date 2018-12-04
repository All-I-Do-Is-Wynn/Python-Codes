list1 =[1,2,3,4,5,6,7]
list2 = ['apple','grape','orange']
list3 =[3,4,6,7,8,9]
print(list1[1])   #=2
print(list2[2])   #=orange
print(list1[2:4])  #=['apple','orange']

#Deletes list2[1] and prints new list
del list2[1]
print(list2)

#Prints all number in the list
for x in list1: print (x)

#Length of list +5
print(len(list1)+5)

atuple = (234, 'abc', "fruit")
#del atuple[1]
#tuple cant have an element deleted so we change it to a list
atuple = list(atuple)
del atuple[1]
#atuple[1] is deleted and we can print it
print(atuple)
#now we add an element 678 and change the list back to a tuple and print
atuple.append(678)
atuple = tuple(atuple)
print(atuple)

#add list3 onto the end of list1 aka concatenation
list1.extend(list3)
print(list1)
print(list3)

#finds the first occurence of obj aka 3
print(list1.index(3))

#inserting 564 in the [1] of list1
list1.insert(1,564)
print(list1)

#pop and return the [1] element in list1
print(list1.pop(1))
print(list1)
#max of list1 = 9  so pop list1[9] which =6
print(list1.pop(max(list1)))