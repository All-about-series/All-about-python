for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}") # n/x is a float type
            break

print("\n") 
# else clause of for loop
for n in range(2, 30):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x, end=', ')
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number', end=', ')