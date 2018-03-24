import random
#from random import randrange
clovek = input('Zadej kámen, nůžky nebo papír: ')


#cislo = randrange (3)
# jak projit pc1 a číslo, hlásí, že pc1 není definováno


seznam = ['kámen', 'nůžky', 'papír']

pc1 = random.choise(seznam)

"""
if cislo == 0:
    pc1 = ("kámen")
elif cislo == 1:
    pc1 = ("nůžky")
else:
    pc1 = ("papír")
"""

if clovek == 'kámen':
    if pc1 =='kámen':
        print("Kámen a kámen, plichta!")
    elif pc1 == 'nůžky':
        print("Kámen tupí nůžky, vyhrála/a jsi!")
    elif pc1 == 'papír':
        print("Papír balí kámen, prohrál/a jsi!")
elif clovek == 'nůžky':
    if pc1 == 'kámen':
        print("Kámen tupí nůžky, prohrál/a jsi!")
    elif pc1 == 'nůžky':
        print ("Nůžky a nůžky, plichta!")
    elif pc1 == 'papír':
        print ("Nůžky stříhaj papír, vyhrál/a jsi!")
elif clovek == 'papír':
    if pc1 == 'kámen':
        print ("Papír balí kámen, vyhrál/a jsi!")
    elif pc1 == 'nůžky':
        print("Nůžky stříhaj papír, prohrál/a jsi!")
    elif pc1 == 'papír':
        print("Papír a papír, plichta!")
else:
    print ("Můžeš zadat pouze kámen, nůžky nebo papír!")
