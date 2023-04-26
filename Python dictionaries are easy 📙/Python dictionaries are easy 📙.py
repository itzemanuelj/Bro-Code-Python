## Python dictionaries are easy 📙

## a dict  is a collectionof key value pairs

capitals = {
    'USA': 'Washington DC',
    'India': 'New Dheli',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

##print(dir(capitals))
##print(help(capitals))

print(capitals.get('USA'))
print(capitals.get('Japan')) ## returns none

if capitals.get('Russia'):
    print('That capital exists')
else:
    print('that country does not exist')

capitals.update({'Germany': 'Berlin'})
print(capitals)

capitals.update({'USA': 'Detroit'})

capitals.pop('China')

capitals.popItem() ##pops last item

capitals.clear() ## clears the dict

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(f'{key}: {value}')


