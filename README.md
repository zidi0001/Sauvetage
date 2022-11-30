# Sauvetage


# Configuration de l'application
## Etape 1 : configurer l'interpreteur Python via Pycharm 
  Nous vous invitons à configurer l'interpreteur de votre éditeur de texte (Pycharm) en selectionnant un executeur Python. Nous vous conseillons l'éditeur au sein de votre environnement virtuel Python.
  
## Etape 2 : configurer le formulaire VBA en lui indiquant le chemin du fichier python et l'emplacement de l'éxecuteur Python
  Ouvrez le formulaire VBA. Ensuite, rendez vous dans l'onglet Développeur et cliquez sur "Visual Basic". Sur la gauche de votre fenêtre, nous vous invitons à cliquer sur "mon_formulaire" situé dans le dossier feuilles.
  
  ![image](https://user-images.githubusercontent.com/116751113/204825569-b6461964-6967-4f03-93dd-01812303b6ef.png)

  Ensuite, cliquez sur le bouton "Prediction".
  Déroulez le code jusqu'à la commande Shell.

Vous devez remplacer les 2 lignes suivantes avec le chemin de l'éxecuteur de votre Python et le chemin de votre script Python.

PythonExePath = """C:\Users\win\Documents\M2 SEP\S1\Cousin\Pre_Pycharm\venv\Scripts\python.exe"""
PythonScriptPath = """C:\Users\win\Documents\M2 SEP\S1\Cousin\Pre_Pycharm\ensemble.py"""


Vous pouvez, normalement, utiliser notre application :)
