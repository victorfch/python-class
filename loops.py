# For
companies = ['Apple', 'Amazon', 'Netflix', 'Microsoft']
example = 'Example'

for company in companies:
    print(company)
print('----------')

for character in example:
    print(character)
print('----------')

for x in range(7):
    print(x)
print('----------')

for num in range(2,5):
    print(num)
print('----------')

for jump in range(10,30,5):
    print(jump)
print('----------')

# While
i = 0
j = 4
while i < 10 and i < j:
    print(i)
    i += 1
print('----------')

fruits = ['apple', 'banana', 'watermelon', 'kiwi']
for fruit in fruits:
    if fruit == 'apple' or fruit == 'kiwi' :
        continue
    print(fruit)
print('----------')

#Dictionaries are like associatives arrays
item = {
    'brand': 'Apple',
    'model': 'X',
    'year': 2020
}
brand = item.get('brand')
item['year'] = 2010
print(item)
print('----------')
for x, y in item.items():
    print("{} -> {}".format(x, y))

if 2010 in item.values():
    print('2010 appears')
    
i = 0
while i < 7:
    if i == 2 or i == 3:
        continue
    if i >= 5:
        break
    print(i)
    i += 1