#coding:utf8

#Exemple d'affichage (sortie)
print("Bonjour tout le monde !")

#Syntaxe de base
#-Chaîne de caractères : '', "", """, '''
#-Commentaires #

#Variable
#-Déclaration et affectation
nom = "Forriez"
print(nom)
#-Déclaration et affectation d'une constante
PI = 3.1416
print(PI)
#-Réaffectation
nom = "Toto"
print(nom)
#-Réaffectation avec la même variable
nb = 1
nb = nb + 1
print(nb)

#Entrée-Sortie + Exemple de concaténation
age = input("Quel est votre âge ? ")
age = int(age)
print("Tu as {} ans.".format(age))

#Opérateurs
#-Opérateur d'affectation  =
#-Opérateurs arithmétiques
print(1 + 1)
print(4 - 6)
print(3 * 5)
print(3 / 5)
print(5 % 2)

print(3 ** 2)
#-Opérateurs d'affectation
var = 1
var += 1
print(var)
var = 4
var -= 6
print(var)
var = 3 
var *= 5
print(var)
var = 3 
var /= 5
print(var)
var = 5
var %= 2
print(var)
#-Opérateurs de comparaison
# == != < > <= >=

#-Opérateurs logiques
# and / or / in / not in / 

#Condition
age = 15
AGE_LEGAL = 18
if age < AGE_LEGAL:
#if 0 < age < AGE_LEGAL:
#if age >= 0 and age < AGE_LEGAL:
	print("Accès refusé")
#elif :
else:
	print("Accès autorisé")

AGE_MAXIMUM = 130
if age <= 0:
	print("Votre âge ne peut pas être négatif. Vous avez écrit n'importe quoi !")
elif age >= AGE_MAXIMUM:
	print("Soit vous êtes un vénérable ancien ! Soit vous avez écrit n'importe !")
elif 0 < age < AGE_LEGAL:
	print("Accès refusé")
else:
	print("Accès autorisé")	

#Boucles
compteur = 0
while compteur < 5:
	print(compteur)
	compteur += 1


for element in "A", "B", "C":
	print(element)

for element in range(1, 10, 1):
	if element == 5:
		continue;
#		break;
	print(element)

#Fonctions
#-Fonctions natives comme print(), input(), int(), float(), str(), bool(), etc.
#-Fonctions créées -> une fonction = une tâche
def direBonjour(nom):
	print("Bonjour {}".format(nom))

prenom = input("Quel est votre prénom ? ")
prenom = str(prenom)

#Appel de la fonction
direBonjour(prenom)

def direBonjour2(nom = "Maxime"):
	print("Bonjour {}".format(nom))

prenom = input("Quel est votre prénom ? ")
direBonjour2()

def direBonjour3(nom = "Maxime"):
	return "Bonjour {}".format(nom)

prenom = input("Quel est votre prénom ? ")
print(direBonjour3(str(prenom)))

def calculerSomme(nombre1, nombre2):
	return nombre1 + nombre2

print(calculerSomme(1, 2))

#Modularité dans Python
#-Module Python = une bibliothèque (library)

import math
print(math.sqrt(2))

#-Un module est un fichier *.py
#1 Créer et écrire dans un fichier toto.py
def test():
	print("Bonjour ! Test réussi !")

#2 Dans main.py, taper :
from toto import test
test()
