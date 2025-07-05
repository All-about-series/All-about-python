print("\'Don\"t,\' they said")
print('\'Don\"t,\' they said')
print('\"Don\'t,\" they said')
print('\"Don\"t,\" they said')

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name', '\n')  # note the r makes the string a raw string literal

# using """ or ''' for multi-line string literals, EOL(End Of Line) is automatically included in the string, but its possible to prevent it by usnig \ at the end of the line 
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# '+' and '*' operator for string concatenation and repetition
print(3 * 'un' + 'ium') #unununium
# Since ** has higher precedence than -, -3**2 will be interpreted as -(3**2) and thus result in -9. To avoid this and get 9, you can use (-3)**2.

print('Py' 'thon') # 'Python'
text = ('Put several strings within parentheses'
        
        'to have them joined together.')
print(text)

print(text + 'COPY')

word = 'Python'
print(word[0], word[-1], sep='isto') # Piston 

#slicing
print(word[2:5]) # tho
print(word[2:]+ word[:-2]) # thonPyth

print(word[:2] + 'Mara' + word[2:]) # PyMarathon

## Strings are immutable sequences of Unicode characters 
# word[0] = 'My' # immutable, so not allowed
# word[2:] = 'hi' # not allowed

# Create new word instead 
word = 'My' + word[2:] # Mython

# print(word[66]) # string index out of range
print(word[:66]) # out of range slice indexes are handled gracefully

