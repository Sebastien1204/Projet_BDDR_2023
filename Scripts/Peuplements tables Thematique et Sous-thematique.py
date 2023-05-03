# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:49:49 2023

@author: Sébastien
"""

import os
import psycopg2
from password import *
import pandas as pd
import csv
import time

class Ressource():
    
    def __init__(self):
        self.path = r"C:/Users/Sébastien/Desktop/Projet BDDR 2/Kaggle/target_tables"
        self.thematique = []
        self.sous_thematique = []
        self.liste_titre = []
        self.liste_date = []
        self.liste_lien = []
        self.liste_auteurs = []
        
    def verification(self,nom_sous_thematique):
        for i in range(len(self.sous_thematique)):
            for j in range(len(self.sous_thematique[i])):
                if nom_sous_thematique == self.sous_thematique[i][j]:
                    return False
        return True
    
    def extract(self,repo,j=None,path=None):
        if path :
            a = path
        else :
            a = self.path
        b = "/" + str(repo)
        path_2 = a + b
        Ressource.tri(self,path_2,j)
        
    def tri(self,path=None,j=None):
        if path :
            new_path = path
        else :
            new_path = self.path
        if path :
            list_files = os.listdir(new_path)
            self.sous_thematique.append([])
            for i in range(len(list_files)):
                element = list_files[i]
                if not "." in element :
                    Ressource.extract(self,element,j,new_path)
                elif element != "":
                    if element[-5] == "_":
                        if Ressource.verification(self, element[:-5]) == True:
                            self.sous_thematique[j].append(element[:-5])
                    else :
                        if Ressource.verification(self,element[:-4]) == True:
                            self.sous_thematique[j].append(element[:-4])
        
            j += 1
        else:
            list_files = os.listdir(new_path)[1:]
            for i in range(len(list_files)):
                element = list_files[i]
                if not "." in element:
                    if element[0] in "12345678":
                        new_element = element.replace("_"," ")
                        self.thematique.append(new_element[2:].title())
                        Ressource.extract(self,element,i,new_path)
                    else:
                        new_element = element.replace("_"," ")
                        self.thematique.append(new_element.title())
                        Ressource.extract(self,element,i,new_path)     
                        
    def data_sans_doublons_titre(self):
        df = pd.read_csv('C:/Users/Sébastien/Desktop/Projet BDDR 2/Kaggle/metadata.csv',low_memory=False)
        df.drop_duplicates(subset='doi',inplace=True)
        df.to_csv('C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv',index=False)
                        
                        
    def titre(self):
        self.path = r"C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv"
        with open (self.path , encoding = "utf8") as file:
            reader = csv.reader(file)
            L = []
            for ligne in reader :
                L.append(ligne)
                
            indice_colonne = 0
            while(L[0][indice_colonne] != 'title'):
                indice_colonne += 1
            
            for k in range (1,len(L)):
                self.liste_titre.append(L[k][indice_colonne])
        
        self.path = r"C:/Users/Sébastien/Desktop/Projet BDDR 2/Kaggle/target_tables"
        liste_dossiers = os.listdir(self.path)
        for i in range(1,len(liste_dossiers)):
            liste_dossiers_2 = os.listdir(self.path + '/' + str(liste_dossiers[i]))
            for j in range(len(liste_dossiers_2)):  
                if(liste_dossiers_2[j][-1] == "v"):
                    with open(self.path + '/' + str(liste_dossiers[i]) + '/' + str(liste_dossiers_2[j]) , encoding = "utf8") as file:
                        reader = csv.reader(file)
                        L = []
                        for ligne in reader :
                            L.append(ligne)
                        indice_colonne = 0
                        while(L[0][indice_colonne] != 'Study'):
                            indice_colonne += 1
                        for k in range (1,len(L)):
                            self.liste_titre.append(L[k][indice_colonne])
                        
        self.liste_titre = list(set(self.liste_titre))
                        
        return len(self.liste_titre)
    
    def date(self):
        compteur = 0
        self.path = r"C:/Users/Sébastien/Desktop/data_sans_doublons_titre.csv"
        liste_titres_traversés = []
        with open (self.path , encoding = "utf8") as file:
            reader = csv.reader(file)
            L = []
            for ligne in reader :
                L.append(ligne)
                
            indice_colonne = 0
            while(L[0][indice_colonne] != 'publish_time'):
                indice_colonne += 1
            
            indice_titre = 0
            while(L[0][indice_titre] != 'title'):
                indice_titre += 1
            
            for k in range (1,len(L)):
                if (L[k][indice_titre] in self.liste_titre and L[k][indice_titre] not in liste_titres_traversés):
                    liste_titres_traversés.append(L[k][indice_colonne])
                    compteur += 1
                    print(compteur)
                    self.liste_date.append(L[k][indice_colonne])
        
        self.path = r"C:/Users/Sébastien/Desktop/Projet BDDR 2/Kaggle/target_tables"
        liste_dossiers = os.listdir(self.path)
        for i in range(1,len(liste_dossiers)):
            liste_dossiers_2 = os.listdir(self.path + '/' + str(liste_dossiers[i]))
            for j in range(len(liste_dossiers_2)):  
                if(liste_dossiers_2[j][-1] == "v"):
                    
                    with open(self.path + '/' + str(liste_dossiers[i]) + '/' + str(liste_dossiers_2[j]) , encoding = "utf8") as file:
                        reader = csv.reader(file)
                        
                        L = []
                        for ligne in reader :
                            L.append(ligne)
                            
                        indice_colonne = 0
                        while(L[0][indice_colonne] != 'Date' and L[0][indice_colonne] != 'Date Published'):
                            indice_colonne += 1
                            
                        indice_titre = 0
                        while(L[0][indice_titre] != 'title'):
                            indice_titre += 1
                            
                        for k in range (1,len(L)):
                            if (L[k][indice_titre] in self.liste_titre and L[k][indice_titre] not in liste_titres_traversés):
                                liste_titres_traversés.append(L[k][indice_colonne])
                                compteur += 1 
                                print(compteur)
                                self.liste_date.append(L[k][indice_colonne])
                        
        return len(self.liste_date)
            
    def creer(self):
        file = open("monfichier.txt", "w")
        for i in range(len(self.thematique)):
            file.write(f"{self.thematique[i]}\n \n")
            for j in range(len(self.sous_thematique[i])):
                file.write(f"{self.sous_thematique[i][j]}\n")
            file.write(f"\n")
        file.close()         
        
R = Ressource()
R.tri()
R.data_sans_doublons_titre()
print(R.titre())
#print(R.date())
#R.creer()

compteur_de_la_sous_thematique = 0

conn = psycopg2.connect(
    dbname = "sebnoel",
    user = "postgres",
    password = "sebnoel",
    host = "localhost", 
    port = '5432')

cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Thematique CASCADE;
            CREATE TABLE Thematique ( Thematique_id INT PRIMARY KEY, Nom VARCHAR(100) );""")
            
for i in range (len(R.thematique)):
    cur.execute("""INSERT INTO Thematique 
                (Thematique_id, Nom)
                VALUES
                (%s,%s)
                """,
                (i+1,R.thematique[i]))
    
cur.execute("""DROP TABLE IF EXISTS Sous_Thematique CASCADE;
            CREATE TABLE Sous_Thematique ( Sous_Thematique_id INT PRIMARY KEY, Thematique_id INT REFERENCES Thematique (Thematique_id), Nom VARCHAR(100) );""")  
            
for i in range (len(R.thematique)):
    for j in range (len(R.sous_thematique[i])):
        compteur_de_la_sous_thematique += 1
        cur.execute("""INSERT INTO Sous_Thematique 
                    (Sous_Thematique_id, Thematique_id, Nom)
                    VALUES
                    (%s,%s,%s)
                    """,
                    (compteur_de_la_sous_thematique,i+1,R.sous_thematique[i][j]))

cur.execute("SELECT * FROM Thematique;")
cur.execute("SELECT * FROM Sous_Thematique;")

df = pd.read_sql('SELECT * FROM Thematique', conn)
print(df)

df = pd.read_sql('SELECT * FROM Sous_Thematique', conn)
print(df)


cur.close()
conn.commit()
conn.close()
print("La connexion PostgreSQL est fermée.")