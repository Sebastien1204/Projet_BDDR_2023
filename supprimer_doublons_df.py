# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:58:46 2023

@author: Sébastien
"""

import pandas as pd
import csv,time,os

def data_sans_doublons_titre():
    
    df = pd.read_csv('C:/Users/Sébastien/Desktop/Projet BDDR 2/Kaggle/metadata.csv',low_memory=False)
    
    df.drop_duplicates(subset='doi',inplace=True)
    
    df.to_csv('C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv',index=False)
    
"""def titre():
    
    liste_titre2 = df['title'].tolist()
    
    liste_titre = []
    texte = "Titres : "
    temps = time.time()
    path = r"C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv"
    
    with open (path , encoding = "utf8") as file:
        reader = csv.reader(file)
        L = []
        for ligne in reader :
            L.append(ligne)
                
        indice_titre = 0
        while(L[0][indice_titre] != 'title'):
            indice_titre += 1
            
        for k in range (1,len(L)):
            liste_titre.append(L[k][indice_titre])
            
    return (texte,len(liste_titre),time.time()-temps)

def lien():
    liste_lien = []
    texte = "Liens url : "
    temps = time.time()
    path = r"C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv"
    
    with open (path , encoding = "utf8") as file:
        reader = csv.reader(file)
        L = []
        for ligne in reader :
            L.append(ligne)
                
        indice_lien = 0
        while(L[0][indice_lien] != 'url'):
            indice_lien += 1
            
        for k in range (1,len(L)):
            liste_lien.append(L[k][indice_lien])
            
    return (texte,len(liste_lien),time.time()-temps)"""

def date():
    liste_date = []
    texte = "Dates : " 
    temps = time.time()
    path = r"C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv"
    
    with open (path , encoding = "utf8") as file:
        reader = csv.reader(file)
        L = []
        for ligne in reader :
            L.append(ligne)
                
        indice_date = 0
        while(L[0][indice_date] != 'publish_time'):
            indice_date += 1
            
        for k in range (1,len(L)):
            liste_date.append(L[k][indice_date])
            
    compteur = pd.Series(liste_date).value_counts()      
    return len(compteur)

"""def journal():
    liste_journaux = []
    texte = "Journaux : "
    temps = time.time()
    path = r"C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv"
    
    with open (path , encoding = "utf8") as file:
        reader = csv.reader(file)
        L = []
        for ligne in reader :
            L.append(ligne)
                
        indice_journal = 0
        while(L[0][indice_journal] != 'journal'):
            indice_journal += 1
            
        for k in range (1,len(L)):
            liste_journaux.append(L[k][indice_journal])
            
    return (texte,len(liste_journaux),time.time()-temps)

def supprimer_data_sans_doublons_titre():
    file = r"C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv"
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("Fichier supprimé !")
    else:
        print("Fichier introuvable !")"""

data_sans_doublons_titre()
print(date())
"""print(titre())
print(lien())
print(date())
print(journal())
supprimer_data_sans_doublons_titre()"""