bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Printing the first item in the list 
print(bicycles[0])

#Using string formatting on an element within a list 
print(bicycles[0].title())

#Printing the first and last item in the list (index = position - 1)
print(bicycles[0])
print(bicycles[3])

#An alerntaive way to print the last item within a list, can be repeated (i.e [-1] = last item, [-2] = second to last item, etc.)
print(bicycles[-1])

#Using a list element as in a string 
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)