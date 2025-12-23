# Comment héberger sa documentaton sur son Github ?

Ici nous allons comprendre comment faire pour héberger sa documentation pas à pas sur son GitHub

## Installer MkDocs

Pour installer MkDocs il faut d'abord avec Python et pip d'installer (Normalement Python installe pip de base)
[Lien d'installation de Python pour Windows](https://www.python.org/downloads/windows/)

Pour voir si Python est bien installé, taper dans l'invite de commande
```py
	python
```

Ensuite pour pip
```py
	pip --version
```
	

##Comment installer MkDocs

Pour installer MkDocs, il suffit de taper dans l'invite de commande

```py
	pip install MkDocs
```

##Créer son projet MKdocs

Pour créer son projet MkDocs, il faut taper la commande suivante
```py
	mkdocs new NomDuProjet
```

Attention il se peut que cela ne marche pas, dans ce cas il faudra taper avant chaque commande mkdocs ```python -m````

Exemple :
```py
	python -m mkdocs new NomDuProjet
```

Ensuite ne pas oublier de faire un cd, pour rentrer dans le dossier de notre projet

```py
	cd NomDuProjet
```

##Créer ses pages et configurer son yaml

Ici le but est de créer vos pages en markdown et ensuite de configurer le fichier yaml à la racine afin que votre site fonctionne.

[Lien vers la documentation Markdown](https://www.markdownguide.org/)

Dés que vous avez fini une de vos pages, ne pas oublier de l'ajouter dans votre fichier mkdocs.yml. Par exemple si j'ai créer le fichier toto.md, alors je devrai le rajouter dans ma configuration.

Exemple de ma configuration :
```
site_name: Ma documentation de la PrairieIA
site_url: https://monNomDutilisateur.github.io/NomDeMonRepot/
nav:
  - Accueil: index.md
  - Vérification : verification.md
  - Secunda: secunda.md
  - Tertia: tertia.md
theme:
  name: readthedocs
```

##Activier le déploiement sur GitHub

Une fois que vous avez fini votre documentation, vous devrez configurer votre GitHub afin qu'il déploie automatiquement votre site pour le mettre à disposition, puis à jour à chacun de vos push.
Pour cela il va falloir aller dans l'onglet "Actions" sur votre repot, puis ensuite vous allez cliquer sur "New workflow". Sur la nouvelle page, on va ajouter notre propre worklfow avec le lien "set up a workflow yourself".

Voici une configuration à modifier en fonction de votre projet 
```
	name: LeNomQueVousVoulezDonner

on:
  push:
    branches:
      - main

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      # 1️⃣ Récupérer le code
      - name: Checkout repository
        uses: actions/checkout@v4

      # 2️⃣ Installer Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      # 3️⃣ Installer MkDocs
      - name: Install dependencies
        run: |
          pip install mkdocs mkdocs-material
      # 4️⃣ Nettoyer l’ancien site pour éviter les artefacts multiples
      - name: Clean previous site
        working-directory: LeDossierDansLaquelleSeTrouveVotreDoc
        run: rm -rf site

      # 5️⃣ Construire le site MkDocs
      - name: Build MkDocs
        working-directory: LeDossierDansLaquelleSeTrouveVotreDoc
        run: mkdocs build

      # 6️⃣ Upload de l’artefact
      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: LeDossierDansLaquelleSeTrouveVotreDoc/site

      # 7️⃣ Déploiement vers GitHub Pages
      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
```

Une fois cela fait, on peut cliquer sur "Commit changes" et mettre les commentaires qu'on veut pour expliquer.
Maintenant en revenant à la racine de notre repot git, nous pourrons constater une petite icône qui nous dire "pending", "error" ou "success" pour nous dire à chaque fois si notre déploiement à bien fonctionner ou non.
Il ne nous restera plus qu'à aller sur le lien de notre site afin de pouvoir le regarder. (Normalement https://monNomDutilisateur.github.io/NomDeMonRepot/)

ATTENTION : Ne pas oublier de faire un Git pull avant de faire des modifications, car le déploiement à créer un fichier sur notre repot, on doit donc le récupérer.