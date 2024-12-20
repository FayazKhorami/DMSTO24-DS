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




import random

print("Välkommen till Sten, Sax, Påse-spelet!")
print("Regler: Sten slår sax, sax slår påse, påse slår sten.")
print("Först till 3 poäng vinner spelet!\n")


dina_poäng = 0
datorns_poäng = 0


while dina_poäng < 3 and datorns_poäng < 3:
    x = input("Välj sten, sax eller påse: ").lower()
    val = random.choice(['sten', 'sax', 'påse'])


    if x not in ['sten', 'sax', 'påse']:
        print("Ogiltigt val! Välj mellan 'sten', 'sax' eller 'påse'.")
        continue


    print(f"Datorn valde {val}.")


    if x == val:
        print("Det blev oavgjort! Ingen får poäng.")
    elif (x == 'sten' and val == 'sax') or (x == 'sax' and val == 'påse') or (x == 'påse' and val == 'sten'):
        print("Grattis! Du vann denna gång.")
        dina_poäng += 1
    else:
        print("Tyvärr, datorn vann denna gången.")
        datorns_poäng += 1


    print(f"Ställning: Du {dina_poäng} - {datorns_poäng} Datorn\n")


if dina_poäng == 3:
    print("Hurra! Du vann hela spelet! 🏆")
else:
    print("Datorn vann spelet. Bättre lycka nästa gång! 🤖")
    
    
"""


import random

print("💥 Välkommen till Sten, Sax, Påse-spelet! 💥")
print("Regler: Sten slår sax, sax slår påse, påse slår sten.")
print("Först till 3 poäng vinner spelet!\n")

dina_poäng = 0
datorns_poäng = 0
dina_val = [] 

while dina_poäng < 3 and datorns_poäng < 3:
    x = input("Välj sten, sax eller påse: ").lower()

    if x not in ['sten', 'sax', 'påse']:
        print("🚫 Ogiltigt val! Välj mellan 'sten', 'sax' eller 'påse'.")
        continue


    if dina_val:
        senaste_val = dina_val[-1]
        if senaste_val == 'sten':
            val = 'påse'  
        elif senaste_val == 'sax':
            val = 'sten'
        else:
            val = 'sax'
    else:
        val = random.choice(['sten', 'sax', 'påse'])  

    print(f"Datorn tänker... 🤔")
    print(f"Datorn valde {val}.")


    if x == val:
        print("😐 Det blev oavgjort! Ingen får poäng.")
    elif (x == 'sten' and val == 'sax') or (x == 'sax' and val == 'påse') or (x == 'påse' and val == 'sten'):
        print("🎉 Grattis! Du vann denna gång.")
        dina_poäng += 1
    else:
        print("😢 Tyvärr, datorn vann denna gången.")
        datorns_poäng += 1


    dina_val.append(x)

    print(f"🔢 Ställning: Du {dina_poäng} - {datorns_poäng} Datorn\n")


if dina_poäng == 3:
    print("🏆 Hurra! Du vann hela spelet! Bra kämpat!")
else:
    print("🤖 Datorn vann spelet. Den var för smart! Försök igen nästa gång!")
