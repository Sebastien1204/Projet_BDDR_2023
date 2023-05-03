# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:20:26 2023

@author: Sébastien
"""

import pandas as pd
import os
import psycopg2

conn = psycopg2.connect(
    dbname = "sebnoel",
    user = "postgres",
    password = "sebnoel",
    host = "localhost", 
    port = '5432')

cur = conn.cursor()

data_journaux = pd.read_sql('SELECT * FROM Journaux', conn)

if os.path.exists("C:/Users/Sébastien/Desktop/journaux.txt"):
    os.remove("C:/Users/Sébastien/Desktop/journaux.txt")

journaux = open("C:/Users/Sébastien/Desktop/journaux.txt","a",encoding="utf-8")

for i in range(1,len(data_journaux)):
    if (i == len(data_journaux)-1):
        if ("'" in data_journaux['journal'][i]):
            nouveau_texte = ""
            for j in range(len(data_journaux['journal'][i].split("'"))):
                nouveau_texte = nouveau_texte + data_journaux['journal'][i].split("'")[j] + " "
            journaux.write(f"['nouveau_texte',{data_journaux['quantite'][i]}]")    
        else:
            journaux.write(f"['{data_journaux['journal'][i]}',{data_journaux['quantite'][i]}]")
    else:
        if ("'" in data_journaux['journal'][i]):
            nouveau_texte = ""
            for j in range(len(data_journaux['journal'][i].split("'"))):
                nouveau_texte = nouveau_texte + data_journaux['journal'][i].split("'")[j] + " "
            journaux.write(f"['nouveau_texte',{data_journaux['quantite'][i]}],")  
            journaux.write(f"\n")
        else:
            journaux.write(f"['{data_journaux['journal'][i]}',{data_journaux['quantite'][i]}],")
            journaux.write(f"\n")
        
journaux.close()

data_laboratoires = pd.read_sql('SELECT * FROM Laboratoires', conn)

if os.path.exists("C:/Users/Sébastien/Desktop/laboratoires.txt"):
    os.remove("C:/Users/Sébastien/Desktop/laboratoires.txt")

laboratoires = open("C:/Users/Sébastien/Desktop/laboratoires.txt","a",encoding="utf-8")

for i in range(1,len(data_laboratoires)):
    if (i == len(data_laboratoires)-1):
        if ("'" in data_laboratoires['laboratoire'][i]):
            nouveau_texte = ""
            for j in range(len(data_laboratoires['laboratoire'][i].split("'"))):
                nouveau_texte = nouveau_texte + data_laboratoires['laboratoire'][i].split("'")[j] + " "
            laboratoires.write(f"['nouveau_texte',{data_laboratoires['quantite'][i]}]")    
        else:
            laboratoires.write(f"['{data_laboratoires['laboratoire'][i]}',{data_laboratoires['quantite'][i]}]")
    else:
        if ("'" in data_laboratoires['laboratoire'][i]):
            nouveau_texte = ""
            for j in range(len(data_laboratoires['laboratoire'][i].split("'"))):
                nouveau_texte = nouveau_texte + data_laboratoires['laboratoire'][i].split("'")[j] + " "
            laboratoires.write(f"['nouveau_texte',{data_laboratoires['quantite'][i]}],")  
            laboratoires.write(f"\n")
        else:
            laboratoires.write(f"['{data_laboratoires['laboratoire'][i]}',{data_laboratoires['quantite'][i]}],")
            laboratoires.write(f"\n")
        
laboratoires.close()

data_institutions = pd.read_sql('SELECT * FROM Institutions', conn)

if os.path.exists("C:/Users/Sébastien/Desktop/institutions.txt"):
    os.remove("C:/Users/Sébastien/Desktop/institutions.txt")

institutions = open("C:/Users/Sébastien/Desktop/institutions.txt","a",encoding="utf-8")

for i in range(1,len(data_institutions)):
    if (i == len(data_institutions)-1):
        if ("'" in data_institutions['institution'][i]):
            nouveau_texte = ""
            for j in range(len(data_institutions['institution'][i].split("'"))):
                nouveau_texte = nouveau_texte + data_institutions['institution'][i].split("'")[j] + " "
            institutions.write(f"['nouveau_texte',{data_institutions['quantite'][i]}]")    
        else:
            institutions.write(f"['{data_institutions['institution'][i]}',{data_institutions['quantite'][i]}]")
    else:
        if ("'" in data_institutions['institution'][i]):
            nouveau_texte = ""
            for j in range(len(data_institutions['institution'][i].split("'"))):
                nouveau_texte = nouveau_texte + data_institutions['institution'][i].split("'")[j] + " "
            institutions.write(f"['nouveau_texte',{data_institutions['quantite'][i]}],")  
            institutions.write(f"\n")
        else:
            institutions.write(f"['{data_institutions['institution'][i]}',{data_institutions['quantite'][i]}],")
            institutions.write(f"\n")
        
institutions.close()

cur.close()
conn.commit()
conn.close()