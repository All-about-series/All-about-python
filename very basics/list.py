squares = [1, 4, 9, 16, 25]
print(squares[-3:])
concat_sq= squares + [36, 49, 64, 81, 100] + squares # new copy not reference passing
print(concat_sq)

# Unlike strings, lists are muatable
squares[0] = 0
print(squares)
print(concat_sq)

squares.append(123)
squares.append(4**3)
print(squares)
print(concat_sq)
print(id(squares[0]) == id(concat_sq[0])) # False as reference are changed

## Reference passing
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object

rgba.append("Alph")
print('Alph' in rgb) # True
print(rgb)

# All slice operations does a shallow copy
correct_rgba = rgba[:] # shallow copy
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)
print(id(correct_rgba) == id(rgba))
correct_rgba[1:3] = ["Violet", "Indigo"]
print(correct_rgba)
correct_rgba[1:3] = []
print(correct_rgba)
correct_rgba[:] = []
print(correct_rgba) # empty list
print(len(correct_rgba))





