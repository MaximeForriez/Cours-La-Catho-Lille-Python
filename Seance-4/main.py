#coding:utf8
import PIL.Image

#Les tuples
#-Tuple = séquence immuable

#-Création
tuple = ()
tuple = (45,0)
tuple = 45,
tuple = (4,6)

#-Lire les données
print(tuple[0])

#Les dictionnaires
#-Liste avec des clés

#-Création
dictionnaire = {}
dictionnaire = {1:145, "prenom":"Maxime"}

#1 et "prenom" sont des clés, tandis que 145 et "Maxime" sont des valeurs associées aux clés.

#-Lire un élement
print(dictionnaire[1])
print(dictionnaire)
print(dictionnaire["prenom"])
print(dictionnaire)

#-Parcourir un dictionnaire
for cle in dictionnaire.keys():
	print(cle)

for valeur in dictionnaire.values():
	print(valeur)
	
for cle, valeur in dictionnaire.items():
	print(cle, " ", valeur)

#-Modifier une valeur
dictionnaire["prenom"]="Sophie"
print(dictionnaire["prenom"])

#-Les dictionnaires sont des objets possédant plein de méthodes : pop, 

#-Copier un dictionnaire
dictionnaire2 = dictionnaire.copy()
dictionnaire2["prenom"]="Maxime"
print(dictionnaire2)

#-Astuce pour les tuples et les dictionnaires
def fonction(*tuple):
  return tuple

print(fonction(1, 2, 3))

def fonction2(**dictionnaire):
  return dictionnaire

print(fonction2(prenom="Max" , nom="Forriez"))

#PIL.Image










