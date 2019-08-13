li = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []

for x in li:
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)


#The alternate system using list comprehensions would be

even_numebers1 = [ x for x in range(1,11) if x % 2 == 0]
print(even_numebers1)
