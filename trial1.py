# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:50:56 2024

@author: Lynn MACLYNN
"""

print('hello, it is my first code in anaconda')

f = lambda x: x**3 - 2
a = 3
print("l'image de {} à travers la fonction f est {}".format(a,f(a)))


def signe(a):
    if (a<0):
        print(a, ' est négatif')
    elif (a>0):
        print(a, ' est positif')
    else :
        print(a, ' est nul')


for i in range(10):
    print(i)
    
for i in range(5,10,2):
    print(i)
for i in range (10,-10,-1):
    signe(i)
    
#=============================================================================
# STRUCTURES DES DONNEES
#==============================================================================

#les listes

villes = ['yaounde', 'dschang', 'bafoussam']
autres = [villes, 'foto']
nombres = [5, 8, 7, 65, 23, 41]
liste = []

#les tuples

villes = ('yaounde', 'bafoussam', 'dschang')
nombre = (1, 3, -5, 7)
tuple1 = ()

# slicing
print(villes[0:2])
print(nombres[1:5])
print(villes[::-1])

#les dictionnaires

bedroom  = {
    'habits' : 50,
    'lit' : 1,
    'portes' : 2,
    'sacs' : 10,
    'tables' : 2,
    'livres' : 30,
    }

food = {
        'pommes' : 20,
        'avocats' : 2,
        'bananes' : 10,
        }

# les lists comprehension

liste = []
for i in range(10):
    liste.append(i*i)
print(liste)

liste1 = [i*i for i in range(10)]
print(liste1)
