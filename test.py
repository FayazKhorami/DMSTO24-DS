
"""
print("Hello, World!")

namn = "Anna"

age = 25

print(f"Hej, {namn}! Du är {age} år gammal.")

x = 10

y = 20 

z = x + y

print (f'Summan av x och y är: {z}')

x = 10

y = 9

print(x + y)

x = '123'

y = 2

z = int(x)

print (z * y)

a = 7 + 3

b = 5 // 2 

c = 5 % 2 

d = 5 ** 2
 
print(a, b, c, d)

x = 10

y = 3

a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
f = x % y
g = x ** y

print (a , b, c, d, e, f, g)

pi = 3.14

print (int(pi))

y = 5

print (float(y))

x = input ('ange ett tal: ')

y = input ('ange ett tal: ')

summa = int(x) + int(y)

print (f'Summan är: {summa}')

"""


x = input('Välj sten, sax eller påse: ').lower()

import random
val = random.choice(['sten', 'sax', 'påse'])

if x == val:
    print(f"Det blev oavgjort! Både du och datorn valde {val}.")
elif (x == 'sten' and val == 'sax') or (x == 'sax' and val == 'påse') or (x == 'påse' and val == 'sten'):
    print(f"Grattis! Du valde {x} och datorn valde {val}. Du vann!")
elif (x == 'sten' and val == 'påse') or (x == 'sax' and val == 'sten') or (x == 'påse' and val == 'sax'):
    print(f"Tyvärr, du förlorade. Du valde {x} och datorn valde {val}.")
else:
    print("Ogiltigt val! Välj mellan 'sten', 'sax' eller 'påse'.")

"""


text = "Data Science"

print("Första tecknet:", text[0])

print("Sista tecknet:", text[-1])

print("De första fem tecknen:", text[:6])

"""