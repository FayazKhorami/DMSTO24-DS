reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

#2 bertätter var den ska börja på 
#3 bertätter hur många steg den ska ta för att skriva den andra i lista
every_third_item = reallyLongList[2::3]

print (every_third_item)

reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

#här ska den börja 0 efter vi har inte berättad för datorn vilken posion ska den börja på, så den bestämmer direkt börja på 0 
# i det fallet 1 är start och den ska hoppa skriva den 4. så det blir 1 5 9 osv
every_forth_number = reallyLongList[::4]

print (every_forth_number)


reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

every_third_item = reallyLongList[2::3]

for i, item in enumerate(every_third_item, start=1):
    print(f"{i}. {item}")
