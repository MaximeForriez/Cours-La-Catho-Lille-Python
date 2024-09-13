# Séance n°6

## L'objet `os`

[Documentation officielle](https://docs.python.org/3/library/os.html)

`os` possède plusieurs méthodes importantes.

- `os.getcwd()` renvoie le répertoire courant.

- `os.chdir("` chemin du répertoire `")` change le répertoire courant.

- `os.listdir()` liste les dossiers et les fichiers du répertoire courant.

- `os.walk('.')` renvoie le contenu du répertoire courant.

- `os.mkdir('.', mode=0o755)` permet de créer un répertoire. L'option `mode=0o755` ne peut être utilisée qu'avec les systèmes d'exploitation `MAC/OS` et `Linux`.

- `os.makedirs("` chemin du répertoire `")` crée un répertoire et sa hiérarchie.

- `os.rename("` ancien nom `","` nouveau nom `)` renomme un fichier dans le répertoire courant.

- `os.removedirs('` chemin du répertoire `')` renomme les dossiers.

- `os.path.exists('` chemin du répertoire `')` vérifie l'existence d'un chemin.

- `os.path.realpath('` chemin du répertoire `')`  vérifie si le chemin est canonique.

- `os.path.join('` répertoire `, ` fichier.py `')` adapte le séparateur des chemins en fonction du système d'exploitation.

`	base = 'c:\\Users\\Max'`

`	filename = 'test.py'`

`	os.path.join(base, filename)`

- `os.path.split('` chemin `')` extrait le chemin du nom du fichier avec pour résultat un tuple. L'indice `0` renvoie l'adresse du répertoire et l'indice `1` renvoie le nom du fichier.

- `os.path.samefile('` chemin 1 `', '` chemin 2 `')` vérifie si deux chemins sont identiques. La méthode renvoie est booléen.

- `os.path.isdir('` chemin `')` vérifie s'il s'agit d'un dossier.

- `os.path.isfile('` fichier `')` vérifie s'il s'agit d'un fichier

- `os.path.islink('` lien `')` vérifie s'il s'agit d'un lien symbolique (ou raccourci).

- `os.path.stat('` fichier `')` renvoie les statistiques d'un fichier.

## L'objet `shutil`

- [Documentation officielle](https://docs.python.org/3/library/shutil.html)

- [Documentation officielle](https://python-simple.com/python-modules-fichiers/shutil.php)

- [Documentation non officielle en français](https://python-simple.com/python-modules-fichiers/shutil.php)
