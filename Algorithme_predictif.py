import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


#Importation de la base de donnees
data = pd.read_csv('C:/Users/win/Documents/M2 SEP/S1/Cousin/ensemble_BDD_train.csv',sep = ";")
data
df=data


# Recodage des quali
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


#Drop des lignes NA's
def imputation(df):
    #df['is na'] = (df['Parainfluenza 3'].isna()) | (df['Leukocytes'].isna())
    #df = df.fillna(-999)
    df = df.dropna(axis=0)
    return  df



# Création de X, Y
def preprocessing(df):
    df = imputation(df)
    df = encodage(df)

    X = df.drop('mort', axis=1)
    y = df['mort']

    print(y.value_counts())

    return X, y



X_train, y_train = preprocessing(df)

X_test, y_test = preprocessing(ypred)

predictions = rf.predict(X_test)
predictions

proba = rf.predict_proba(X_test)
proba