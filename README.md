# Codes correcteurs

Nous avons rédigé un article à propos des codes correcteurs et rédigé deux programmes en Python.

Vous pouvez retrouver le fichier `plan.tex` qui contient la répartition travaille, le fichier `article.bib` qui
contient les références et `article.tex` qui contient l'article.

Le projet a été réalisé par le groupe **G2S14** avec **Isabelle LIN**, **Filip SUDOL** et **Hocine HAMMOUCHE**.

## Les programmes

Il y a deux programmes graphiques en Python :

- `main.py` qui permet d'encoder un text avec le codage de Hamming et de le décoder.
- `game.py` qui affiche un matrix 4x4 qui correspond à un code de Hamming avec une erreur qu'il faut retrouver.

Vous pouvez retrouver les fichiers dans le dossier annexe et les instructions pour les utiliser ci-dessous.

## Utilisation

1. Installer `latex` et `bibtex` voir
   [ici](https://zestedesavoir.com/tutoriels/826/introduction-a-latex/1319_creer-vos-premiers-documents/5786_installation-et-premiers-pas/)
2. Télécharger le dépôt et générer le pdf

```shell
git clone 
cd md5-article
make article.pdf
```

### Utilisation des programmes

1. Installer Python 3
   voir [ici](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/1-premiers-pas/2-installation/)
2. Télécharger le dépôt et lancer les programmes

```shell
git clone 
cd md5-article
python3 annexe/main.py
# ou
python3 annexe/game.py
```
