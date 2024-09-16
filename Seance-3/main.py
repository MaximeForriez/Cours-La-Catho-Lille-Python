#coding:utf8
import turtle
import module

#Listes
#-Création d'une liste
liste1 = list
liste2 =[]
liste3 = [1, 3, 15]
liste4 = [0]*10
liste5 = range(20)
print(liste1)
print(liste2)
print(liste3)
print(liste4)
print(liste5)

#-Afficher un élément 
print(liste5[0])
print(liste5[15])
print(liste5[-1])
print(liste5[:2])
print(liste5[3:])
print(liste5[9:12])

#-Parcourir une liste
i = 0
while i < len(liste5):
	print(liste5[i])
	i += 1

for element in liste3:
	print(element)

#-Modifier un élément
print(liste3[1])
liste3[1] = 100000
print(liste3[1])
liste3[1] = 3

#-Les listes sont des objets qui disposent de plein de méthodes
liste3.append(100)
for element in liste3:
    print(element)

# insert, pop, remove, index, sort, reverse, count, clear, extend, etc.
	
#-Copier une liste
#--L'erreur courante
liste6 = liste3
print(liste6)
liste3.append(9)
print(liste6)
print(liste3)

#--La solution
import copy
liste6 = copy.deepcopy(liste3)
print(liste6)
liste6.append(7)
print(liste6)
print(liste3)

for objet in enumerate(liste6):
	print(objet)

#Test du module créé et de la condition de fin de fichier
	
module.module()
module.module2()

#turtle
















