motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Changing the first element in the list 
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding a new element to the list using the append method, always adds to the end of a list.
motorcycles.append('ducati')
print(motorcycles)

#Inserting elements into a list using the insert method, which allws you to add an element at a specific index.
motorcycles_v2 = ['honda', 'yamaha', 'suzuki']
motorcycles_v2.insert(0, 'ducati')
print(motorcycles_v2)

#Deleting an item using the del statement
del motorcycles_v2[0]
print(motorcycles_v2)

#Using the pop method to remove an item from a list, which removes the last item by default.
popped_motorcycle = motorcycles_v2.pop()
print(motorcycles_v2)
print(popped_motorcycle)

#The pop method can also be used to remove an item at a specific index. 
first_owned = motorcycles_v2.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#The remove method can be used to remove an item by its value rather than its index. (Only deletes the first occurnce of the value specified)
motorcycles_v3 = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles_v3.remove('ducati')
print(motorcycles_v3)
too_expensive = 'honda'
motorcycles_v3.remove(too_expensive)
print(motorcycles_v3)
print(f"\nA {too_expensive.title()} is too expensive for me.")