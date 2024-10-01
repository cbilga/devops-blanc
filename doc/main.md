# Help on module src.main in src:

# NAME
## src.main - Ce module permet de rechercher des mots dans un dictionnaire, en utilisant des caractères génériques (wildcards).

# DESCRIPTION
 **Fonctionnement général:**
 
 1. **Chargement du dictionnaire:** Le module charge un dictionnaire de mots depuis un fichier texte.
 2. **Recherche de mots:** L'utilisateur saisit un mot à rechercher, qui peut contenir des caractères génériques (représentés par le caractère '?').
 3. **Affichage des résultats:** Le module affiche tous les mots du dictionnaire qui correspondent au motif de recherche.
 
 **Exemple d'utilisation:**
 
## Pour rechercher tous les mots de 4 lettres commençant par 'C' et se terminant par 'T', vous pouvez saisir le motif "C??T".
 
 **Note:** Les mots du dictionnaire sont automatiquement convertis en majuscules pour les recherches.
 
 **Modules utilisés:**
 
 * `re`: Module pour l'utilisation d'expressions régulières, permettant la recherche de motifs avec des caractères génériques.
 
 **Limitations:**
 
 * Les caractères génériques ne peuvent représenter qu'une seule lettre.
 * Le dictionnaire est chargé en mémoire, ce qui peut limiter la taille des dictionnaires utilisables.

# FUNCTIONS
## create_dictionary()
### Crée un dictionnaire indexé par le nombre de lettres, en majuscules et sans doublons.
 
### Returns:
 dict: Un dictionnaire où les clés sont des nombres représentant la longueur des mots,
 et les valeurs sont des ensembles de mots de cette longueur.
 
## find_words(dictionary, pattern)
### Trouve les mots correspondant au pattern dans le dictionnaire.
 
### Args:
 dictionary (dict): Le dictionnaire de mots.
 pattern (str): Le pattern de recherche avec des wildcards (?).
 
### Returns:
 list: Une liste de mots correspondant au pattern.
 
## run()
### Point d'entrée principal de l'application.
 
### Il permet de :
 
 * Charger le dictionnaire de mots.
 * Effectuer des recherches de mots avec des wildcards.
 * Afficher les résultats à l'utilisateur.

# FILE
 /home/runner/work/devops-blanc/devops-blanc/src/main.py


