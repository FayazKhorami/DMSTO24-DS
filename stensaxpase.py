"""""

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

x =                                          5

y =                                             10
