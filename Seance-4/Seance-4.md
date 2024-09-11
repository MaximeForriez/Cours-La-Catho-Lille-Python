# Séance n°4

## Les tuples

Un **tuple** est une séquence immuable, c'est-à-dire une liste en lecture seule.

### Création

`tuple = ()`

ou

`tuple = (45,0)`

ou

`tuple = 45,`

ou

`tuple = (4,6)`

### Lire les données

On lit les données grâce aux indices du tuple.

`print(tuple[0])`

## Les dictionnaires

Un **dictionnaire** est une liste avec des clés.

### Créer un dictionnaire

`dictionnaire = {}`

ou

`dictionnaire = {1:145, "prenom":"Maxime"}`

Ici `1` et `"prenom"` sont des clés, tandis que `145` et `"Maxime"` sont des valeurs associées aux clés.

### Lire un élement

On peut appeler l'élément par sa clé.

`print(dictionnaire[1])`

ou

`print(dictionnaire)`

ou

`print(dictionnaire["prenom"])`

ou

`print(dictionnaire)`

### Parcourir un dictionnaire

Parcourir par les clés :

`for cle in dictionnaire.keys():`

`	print(cle)`

Parcourir par les valeurs :

`for valeur in dictionnaire.values():`

`	print(valeur)`

Parcourir par les clés et les valeurs :
	
`for cle, valeur in dictionnaire.items():`

`	print(cle, " ", valeur)`

### Modifier une valeur

Il suffit d'utiliser la clé comme si c'était un indice.

`dictionnaire["prenom"]="Sophie"`

`print(dictionnaire["prenom"])`

### Copier un dictionnaire

Tout comme les listes, on ne peut pas copier directement par une simple affectation un dictionnaire.

`dictionnaire2 = dictionnaire.copy()`

`dictionnaire2["prenom"]="Maxime"`

`print(dictionnaire2)`

> [!IMPORTANT]
> Les dictionnaires possèdant plein de méthodes : `pop`, *etc*.

## Astuce pour les tuples et les dictionnaires

On peut créer un tuple avec les paramètres d'une fonction en appelant. Il suffit de placer `*` devant l'argument de la fonction.

`def fonction(*tuple):`

`	return tuple`

`print(fonction(1, 2, 3))`

On peut créer un dictionnaire avec les paramètres d'une fonction en appelant. Il suffit de placer `**` devant l'argument de la fonction.

`def fonction2(**dictionnaire):`

`	return dictionnaire`

`print(fonction2(prenom="Max" , nom="Forriez"))`

## L'objet `PIL.Image`






