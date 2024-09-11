# Séance n°3

## Les listes en Python

Il n'existe pas de tableau en `Python`.

#Listes
### Création d'une liste

`liste1 = list`

ou

`liste2 =[]`

ou

`liste3 = [1, 3, 15]`

ou

`liste4 = [0]*10`

ou

`liste5 = range(20)`

`print(liste1)`

`print(liste2)`

`print(liste3)`

`print(liste4)`

`print(liste5)`

### Afficher un élément 

> [!IMPORTANT]
> Les indices commencent à zéro, et pas un.

`print(liste5[0])`

`print(liste5[15])`

`print(liste5[-1])`

`print(liste5[:2])`

`print(liste5[3:])`

`print(liste5[9:12])`

### Parcourir une liste

`i = 0`

`while i < len(liste5):`

`	print(liste5[i])`

`	i += 1`

`for element in liste3:`

`	print(element)`

### Modifier un élément

`print(liste3[1])`

`liste3[1] = 100000`

`print(liste3[1])`

`liste3[1] = 3`

### Les méthodes des listes

Les listes sont des objets qui disposent de plein de méthodes. Par exemple,

`liste3.append(100)`

`for element in liste3:`

`    print(element)`

mais encore `insert`, `pop`, `remove`, `index`, `sort`, `reverse`, `count`, `clear`, `extend`, *etc*.
	
### Copier une liste

Si vous effectuez les commandes suivantes :

`liste6 = liste3`

`print(liste6)`

`liste3.append(9)`

`print(liste6)`

`print(liste3)`

vous voyez qu'elle ne marche pas. Vous avez créé une référence entre les variables `liste3` et `liste6`.

Pour copier une liste, il ne faut pas créer une nouvelle liste, mais un **clone**.

`import copy`

`liste6 = copy.deepcopy(liste3)`

`print(liste6)`

`liste6.append(7)`

`print(liste6)`

`print(liste3)`

`for objet in enumerate(liste6):`

`	print(objet)`

Avec cette technique, vous avez copié la liste.

## L'objet `turtle`
























## La condition `if __name__ == "__main__":`

Cette condition permet de tester un module. Elle doit être obligatoirement à la fin d'un fichier `Python`. L'objectif est de vérifier si les fonctions fonctionnent en dehors du fichier principal.
