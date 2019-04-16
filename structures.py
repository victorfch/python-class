colors = ['blue', 'red', 'yellow', 'white', 'black', 'red']
colors[2] = 'green'
color = colors[0]
if 'blue' in colors:
    print('Blue appears in color list')
colors.append('grey')
print(colors)
print(color)
colors.insert(1, 'violet')
print('Colors are: {}'.format(colors))
colors.remove('red') #remove only first ocurrence
del colors[0]
print('All colors are {}'.format(colors))
print('--------------')

# Tuples
fruits = ('orange', 'apple', 'banana')
# fruits[2] = 'watermelon' cannot change value
print('Fruits are: {}'.format(fruits))
print('--------------')

# Sets
companies = {'Apple', 'Microsoft', 'Apple'} #sets eliminate duplicates
companies.add('Coca Cola')
companies.add('Apple')
companies.update(['more element', 'one more'])
isInList = 'Apple' in companies
print(isInList)
print(companies)

