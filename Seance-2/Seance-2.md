# Séance n°2

## Le concept d'objet

Un objet traite un type de données particulier. Tout objet possède :

- des attributs ou des propriétés ;

- des méthodes.

Les propriétés désignent les variables propres à l'objet. Les méthodes renvoient aux fonctions propres de cet objet. Dans le cours précédent, on avait vu l'objet `math`. Il permet de comprendre simplement ce qu'est un objet.

L'objet `math` possède des constantes `pi` et `e` par exemple. On les appelle en tapant :

`math.pi`

`math.e`

c'est-à-dire le nom de l'objet et l'attribut appelé.

L'objet `math` possède des fonctions mathématiques :

- `math.pow(` nombre`,` puissance `)` : nombre à la puissance demandée ;

- `math.sqrt(` nombre `)` : racine carrée du nombre ;

- `math.cbrt(` nombre `)` : racine cubique du nombre ;

- `math.log(` nombre`,` base `)` : logarithme du nombre de base demandée ;

- `math.log2(` nombre `)` : logarithme de base 2 du nombre ;

- `math.log10(` nombre `)` : logarithme de base 10 du nombre ;

- `math.exp(` nombre `)` : exponentielle du nombre ;

- `math.cos(` nombre `)` : cosinus du nombre ;

- `math.sin(` nombre `)` : sinus du nombre ;

- `math.tan(` nombre `)` : tangente du nombre ;

- `math.acos(` nombre `)` : arc cosinus du nombre ;

- `math.asin(` nombre `)` : arc sinus du nombre ;

- `math.atan(` nombre `)` : arc tangente du nombre ;

- `math.floor(` nombre `)` : arrondir à l'entier inférieur ;

- `math.ceil(` nombre `)` : arrondir à l'entier supérieur ; 

- `math.factorial(` nombre `)` : factorielle du nombre ;

- *etc*.

> [!WARNING]
> Les nombres complexes ont leur propre module `cmath`.

La particularité de l'objet `math` est qu'il n'est pas nécessaire d'instancier un objet pour l'utiliser, à la différence de l'objet `string`.

## L'aide sur Python

Pour avoir de l'aide sur un objet connu, on tape

`help(` nom de l'objet `)`

## Les chaînes de caractères

La chaîne de caractères en `Python` est un objet. L'objet est instancié en affectant une variable.

`nom = "forriez"`

Vous venez de créer un objet `string`. On utilise par conséquent des méthodes pour transformer cet objet.

- `nom.upper()` met en tous les caractères en majuscule.

- `nom.lower()` met en tous les caractères en minuscule.

- `nom.capitalize()` met la première lettre de chaque mot en majuscule.

- `nom.strip()` efface les espaces blancs avant le premier mot et après le dernier mot.

- `nom.replace(` ancien(s) caractère(s)`,` nouveau(x) caractère(s)`,` occurrences `)`

- `nom.swapcase()` transforme toutes les majuscules en minuscules, et *vice versa*.

- `nom.split("` séparateur `")` transforme la chaîne en liste grâce au séparateur.

- `nom.isdigit()` teste si la chaîne est un entier.

- `nom.isalpha()` teste si la chaîne ne contient que des lettres.

- `nom[` indice `]` affiche le caractère de l'indice avec une valeur allant de 0 à l'infini.

- *etc*.

On peut obtenir la longueur d' une chaîne de caractères avec :

`len(nom)`

On peut concaténer les chaînes de caractères de deux façons :

1. "J'ai {} ans.".format(41)

2. "J'ai " + str(41) + " ans."

La concaténation avec `+` n'a que des variables de type `str`, à la différence de la méthode `.format(...)`.

## Le module PyPDF

La documentation est :

- [https://pypi.org/project/pypdf/](https://pypi.org/project/pypdf/) ;

- [la documentation PyPDF](https://pypdf.readthedocs.io/en/stable/) ;

- [la documentation PyPDF en français](https://products.documentprocessing.com/fr/merger/python/pypdf/).

`import pypdf`

Les fonctions et les méthodes principales sont :

- `reader = pypdf.PdfReader("example.pdf")` pour instancier un objet P.D.F. L'objet contient le fichier si on est dans le même dossier, ou le chemin absolu ou relatif du fichier ;

- `number_of_pages = len(reader.pages)` pour avoir le nombre de pages du document.;

- `page = reader.pages[0]` pour lire la première page du P.D.F. ;

- `text = page.extract_text()` pour extraire les éléments textuels de la page P.D.F. ;

- `meta = reader.metadata` pour lire les métadonnées de la page P.D.F. :

	+ `meta.author` ;

	+ `meta.producer` ;

	+ `meta.subject` ;

	+ `meta.title`.

- `writer = pypdf.PdfWriter()` pour écrire des éléments dans le P.D.F. ;

- `writer.write("` nom du fichier `")` pour enregistrer les éléments écrits ;

- `writer.close()` pour fermer les modifications. Cette commande doit être mise chaque fois qu'un `pypdf.PdfWriter()` est créé ;

- `writer.add_page(` nouvellePage `)` pour ajouter une page ;

- `writer.add_metadata(` données en format J.S.O.N. `)` pour ajouter des métadonnées ; 

- `page2 = new_elements.add_blank_page(` largeur`,` hauteur`)` pour ajouter une page blanche ;

- `page2.merge_transformed_page(reader.pages[` numéro de page` ], pypdf.Transformation().translate(` nombre `),` nombre de pages `)` pour ajuster le contenu de la page.
