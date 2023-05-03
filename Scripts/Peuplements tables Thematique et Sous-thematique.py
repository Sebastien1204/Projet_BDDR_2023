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
                      
        
R = Ressource()
R.tri()

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
        
cur.close()
conn.commit()
conn.close()
print("La connexion PostgreSQL est fermée.")
