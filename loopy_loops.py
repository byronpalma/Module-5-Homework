# tuples dealing with pokemon
if __name__ == "__main__": 

    pokemon = ('pikachu', 'charmander', 'bulbasuar')
    print(pokemon[0])

    print(f'starter1: {pokemon[0]}')
    print(f'starter2: {pokemon[1]}')
    print(f'starter3: {pokemon[2]}')

# tuple dealing with my name
name = ('byron')
my_tuple = tuple(name)
print(my_tuple)   
print(f'"i" is in my tuple: {3 in my_tuple}')

# # loops dealing with tuple
for i in range(2, 11):
    print (i)

numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10')

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

string = 'This is a simple string'
for letter in string:
    print(letter)
