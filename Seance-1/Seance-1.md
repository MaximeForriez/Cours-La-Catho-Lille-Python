# Séance n°1

Pourquoi apprendre Python ? Pour beaucoup, Python sera l'Excel de demain, c'est-à-dire il sera plus judicieux d'opérer des traitements avec Python qu'Excel. C'est normal, la société évolue, et Excel est inapproprié pour opérer un traitement automatique performant, surtout lorsque la masse et les sources de données sont très importantes, or nous  sommes dans un monde de données massives. Le tableur n'est plus le meilleur outil pour tenir un tableau de bord par exemple.

##Documentation

Cette série de T.D. ne peut que vous donner un bref aperçu du langage de programmation `Python`. Vous allez apprendre les rudiments de la version 3[^1]. L'objectif est d'en acquérir les bases. Tout au long des séances, vous serez confrontés à des problèmes. Typiquement, un code qui ne marche pas, il faudra apprendre à résoudre par vous-mêmes les problèmes. Pour ce, la [documentation officielle](https://docs.python.org/3/) du langage doit devenir votre meilleure amie. De nombreuses documentations sont en français, mais, pour toutes les nouvelles technologies, il faut savoir lire l'anglais technique.

Par ailleurs, les tutoriels sur Youtube sont très nombreux en français.

- [Formation vidéo - Cours](https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC)

- [Formation vidéo - Tutoriels](https://www.youtube.com/watch?v=a5HGF_ELI1E&list=PLrSOXFDHBtfFMB2Qeuej6efzZRvjRdXo8)

- [Formation vidéo - Exercices](https://www.youtube.com/watch?v=HVN4qv6Dxdk&list=PLrSOXFDHBtfEiSgOG1FM4oq-yS24iV4s1)

- *etc*.

##Syntaxe de base

Tout programme informatique offre la possibilité à l'utilisateur de commenter son code. Au cours de votre apprentissage, n'hésitez pas à utiliser cette fonctionnalité pour ajouter **vos** éléments de compréhension.

`# Ceci est un commentaire en Python`

##Algorithmique

Le mot « algorithmie » vient du nom du mathématicien persan, Muhammad ibn Musa al-Khuwarizmi dit Al Khuwarizmi (IX<sup>e</sup> siècle), latinisé en Algoritmi.

Un algorithme est une **recette**. Il s'agit d'une suite d'instructions qui, lorsqu'elles sont exécutées correctement, aboutissent au résultat attendu. C'est un énoncé en langage clair, bien défini et ordonné.

Plus précisément, un algorithme décrit une **méthode de résolution** de problèmes courants, le plus souvent par le calcul.

L'algorithmique[^2] est l'ensemble des éléments informatiques permettant d'écrire un programme. Apprendre l'algorithmique, c'est apprendre à programmer dans les règles de l'art. L'algorithmique doit permettre le développement de mécanisme de pensée par l'apprentissage permettant d'optimiser les traitements que le développeur doit programmer au niveau :

- de la vitesse de calcul ;

- de l'occupation de la mémoire ;

- de la quantité de lignes de programmation ;

- *etc*.

Il est possible d'apprendre le code informatique sans aucun langage de programmation. On parle alors de **langage de description d'algorithmes** (L.D.A.). Dans ce cadre, un **pseudo-code** fait référence à une syntaxe ressemblant à un code. Voici les éléments **presque** universels que l'on retrouve dans tout langage de programmation :

- les variables ;

- les opérateurs ;

- les instructions ;

- les conditions ;

- les boucles ;

- les boucles conditionnelles ;

- les fonctions et les procédures ;

- les objets[^3].

##Premier programme

1. Aller sur le site [replit](https://replit.com/)

2. Créer votre compte

3. Paramétrer le langage voulu, ici `Python`

4. Cliquer sur `Create REPL`

L'écran de travail se divise en trois zones :

1. à gauche, la navigation dans les dossiers et les fichiers de votre projet ;

2. au centre, la zone de création des programmes sous la forme d'onglets. Tout projet `Python` doit au minimum avoir un projet `main.py`. Vous pouvez créer de nouveaux fichiers en cliquant sur `+` et `New file`. Faites attention de bien mettre l'extension `.py` au nom de votre fichier.

3. à droite, la console. Vous avez deux choix possibles : soit l'onglet `Console` dans lequel vous exécutez votre programme avec le bouton vert `Run`, soit en `Shell` qui correspond à un terminal dans lequel vous devez taper la commande `python main.py` pour exécuter votre programme.

Le plus simple pour commencer est de créer une sortie.

`#Exemple d'affichage (sortie)
print("Bonjour tout le monde !")`

`print(...)` est la fonction permettant d'écrire un retour sur la console d'exécution. Les `"` permettent de créer une zone de texte (`String`, chaîne de caractères en informatique).

Tester le code pour voir si vous avez compris.

\[!TIP] Les chaînes de caractères peuvent s'écrire de quatre manières différentes : `''`, `""`, `'''`, et `"""`. Les guillemets simples ou doubles permettent d'écrire un texte sur une seule ligne, tandis que les guillements triples simples ou doubles permettent d'écrire du texte sur plusieurs lignes.

##Les variables






##Les opérateurs


##Les conditions


##Les boucles conditionnelles


##Les boucles


##Les fonctions






[^1]: Les versions 2 et 3 sont incompatibles, même dans la syntaxe de base. Dit autrement, si la [version 4](https://answerpython.com/why-python-4-may-never-arrive/) annoncée venait à être publiée, il faudra s'attendre à la même incompatibilité.

[^2]: On peut également dire algorithmie. Les deux existent en français.

[^3]: Bien que `Python` soit un langage orienté objet, ce concept informatique ne sera pas abordé pleinement dans ces séances.
