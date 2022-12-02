# Library 

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import tkinter
from tkinter import *




################################################# Code #################################################
## Importation de la base BDD_train

data = pd.read_csv('ensemble_BDD_train.csv',sep = ";")
data
df=data

df = df.drop(1, axis=0)


# On stocke la données sur le fichier Excel

#Si problème, mettre le chemin exact du formulaire VBA
predi = pd.read_excel("Formulaire_Final_Automate.xlsm", decimal=",")

ypred = predi


### On recode les variables qualitatives en numérique grace a la fonction encodage 


def encodage(df):
    code = {"Alpes-Maritimes": 0,
            "Aude": 1,
            "Bouches-du-Rhone": 2,
            "Calvados": 3,
            "Charente-Maritime": 4,
            "Collectivite de Saint Barthelemy": 5,
            "Collectivite de Saint Martin": 6,
            "Corse": 7,
            "Corse-du-Sud": 8,
            "Cotes-d'Armor": 9,
            "Eure": 10,
            "Finistere": 11,
            "Gard": 12,
            "Gironde": 13,
            "Guadeloupe": 14,
            "Guyane": 15,
            "Haute-Corse": 16,
            "Herault": 17,
            "Ille-et-Vilaine": 18,
            "Landes": 19,
            "Loire-Atlantique": 20,
            "Manche": 21,
            "Martinique": 22,
            "Mayotte": 23,
            "Morbihan": 24,
            "Nord": 25,
            "Nouvelle-Caledonie": 26,
            "Pas-de-Calais": 27,
            "Polynesie": 28,
            "Pyrenees-Atlantiques": 29,
            "Pyrenees-Orientales": 30,
            "Reunion": 31,
            "Saint-Pierre-et-Miquelon": 32,
            "Seine-Maritime": 33,
            "Somme": 34,
            "Var": 35,
            "Vendee": 36,

            "Eaux territoriales": 0,
            "Plage et 300 metres": 1,
            "Port et acces": 2,
            "Responsabilite francaise": 3,
            "Autre": 0,

            "Clandestin": 1,
            "Commerce francais": 2,
            "Marin etranger": 3,
            "Pecheur francais": 4,
            "Plaisancier francais": 5,
            "Toutes categories": 6,


            "Aeronef": 1,
            "Commerce": 2,
            "Loisir nautique": 3,
            "Peche": 4,
            "Plaisance": 5,

            "apres-midi": 0,
            "dejeuner": 1,
            "matinee": 2,
            "nuit": 3,

            "Arcachon Eyrac": 0,
            "Barfleur": 1,
            "Boucau-Bayonne": 2,
            "Boulogne-sur-Mer": 3,
            "Brest": 4,
            "Calais": 5,
            "Cherbourg": 6,
            "Concarneau": 7,
            "Dielette": 8,
            "Dieppe": 9,
            "Dunkerque": 10,
            "Etretat": 11,
            "Fecamp": 12,
            "Granville": 13,
            "La Rochelle-Pallice": 14,
            "Le Havre": 15,
            "Le Touquet": 16,
            "Le Treport": 17,
            "Les Sables-d'Olonne": 18,
            "Ouistreham": 19,
            "Paimpol": 20,
            "Pointe de Grave": 21,
            "Portbail": 22,
            "Port-Navalo": 23,
            "Port-Tudy": 24,
            "Roscoff": 25,
            "Saint-Jean-de-Luz": 26,
            "Saint-Malo": 27,
            "Saint-Nazaire": 28,
            "Vieux-Boucau": 29,
            "Wissant": 30,

            }

    for col in df.select_dtypes('object').columns:
        df.loc[:, col] = df[col].map(code)
    return df


#On supprime les NA avec la fonction imputation 


def imputation(df):
    #df['is na'] = (df['Parainfluenza 3'].isna()) | (df['Leukocytes'].isna())
    #df = df.fillna(-999)
    df = df.dropna(axis=0)
    return  df

# On sépare notre dataframe en deux, les features(X) et la variable à prédire de l'autre ( Y ). 


def preprocessing(df):
    df = imputation(df)
    df = encodage(df)

    X = df.drop('mort', axis=1)
    y = df['mort']

    return X, y

####### Création de notre base d'entrainement et notre base test ######## 

X_train, y_train = preprocessing(df)

X_test, y_test = preprocessing(ypred)

####### Création du modèle random Forest appliqué à notre base d'entrainement #######

#On créé un Random Forest de 100 arbres
rf = RandomForestClassifier(n_estimators = 50, max_depth=9 ,min_samples_split=6 , criterion= 'gini')
#Et on lance le training sur notre dataset de train
rf.fit(X_train, y_train)



####### Précision du modèle ########

predictions = rf.predict(X_test)
predictions

proba = rf.predict_proba(X_test)
proba = proba[0,1]*100

####### On lance l'application via notre terminal 

proba = proba
predit = predictions

# Les différentes instructions en fonction des sorties de notre algorithme 
## Si la prédiction = 1 alors vous avez des risques de décéder 
## Si la prédiction est différente de 1 vous avez des chances d'être secourus. 

if predit==1:
    commentaire = "vous avez un risque de décéder"
else:
    commentaire = "vous avez des chances d'être secouru"

# Paramètre d'affichage de la fenêtre  

tuto = tkinter.Tk()
tuto.geometry("700x250")
tuto.title("Chance de survie")

x=95

# Les message affichés sur notre fenêtre et leur différentes positions 

l3 = Label(text="Notre application estime votre probabilité de décès à : ", font="Arial")
l3.place(x=10,y=100)

l3 = Label(text= str(proba) + " %", font="Arial")
l3.place(x=400,y=100)

l1 = Label(text=" En cas de problèmes, selon notre application :", font="Arial")
l1.place(x=10,y=50)

l2 = Label(text=commentaire, font="Arial")
l2.place(x=400,y=50)

#lOOP
tuto.mainloop()