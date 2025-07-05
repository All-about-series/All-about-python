## Fibonacci sequence example
a,b = 0,1
while a < 10:
    print(a, end=',' if a < 9 else '\n')
    a, b = b, a + b # RHS is evaluated before assignment, RHS is evaluated from left to right

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items(): # users.items() for original reference
    if status == 'inactive':
        del users[user] # deleting from original collection
        # del users.copy()[user] # delete from the copy 
print(users)

# Range
list_from_range0 = list(range(-2, -20, 3)) # [] (since step is positive but we have to go backwards, imagine the numberline)
list_from_range1 = list(range(-2, -20, -3))
print(list_from_range1)
print(sum(range(1, 10))) # 45, sum of numbers from 1 to 9

# Enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1))) # index starts from 1
