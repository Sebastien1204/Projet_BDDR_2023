# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:45:43 2023

@author: Sébastien
"""

import pandas as pd
import json
import csv
import os
import psycopg2
import numpy
from psycopg2.extensions import register_adapter, AsIs

def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)

def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)

register_adapter(numpy.float64, addapt_numpy_float64)
register_adapter(numpy.int64, addapt_numpy_int64)

path = r"C:/Users/Sébastien/Desktop/data_final.csv"             #On va utiliser sans les doublons sur les titres.

with open(path , encoding="utf8") as file:                      #On commence par ouvrir le fichier et l'incrémenter dans une variable nommée data.
    reader = csv.reader(file)
    data = []
    for ligne in reader :
        data.append(ligne)
        
    df1 = pd.DataFrame(data , columns = data[0])
    df2 = df1.sort_values('title' , ignore_index = True)
    
    L = df2
    
def ressources(taille):                                                          #On crée une fonction auteur qui retournera une liste de listes avec, pour chaque liste, le titre de l'article, le prénom de l'auteur, son suffixe, son nom de famille, son email, son institution et son laboratoire.
    liste_auteurs = []
    liste_fichiers_pdf = []                                                 #Ces deux listes contiendront pour chaque article, le fichier pdf ou le fichier pmc associé.                                   
    liste_fichiers_pmc = []
    path_2 = r"C:/Users/Sébastien/Desktop/Projet BDDR 2/document_parses"
    liste_fichiers_pdf_2 = os.listdir(path_2 + '/pdf_json')                 #Ici, on récupère simplement la liste des fichiers pdf présents dans les données de base, on vérifiera par la suite si le fichier pdf référencé dans le fichier data_final existe et donc peut nous donner des informations.
    liste_fichiers_pmc_2 = os.listdir(path_2 + '/pmc_json')
    
    for k in range (1,len(L)):
        if (L['pdf'][k] != ""):
            if ';' in L['pdf'][k]:                                     #On regarde s'il y a plusieurs fichiers pdf de référencés.
                nb_info_pdf_0 = 0                                           #On initialise notre nombre d'informations à partir des fichiers pdf à 0.
                for i in range(len(L['pdf'][k].split(';'))):           #On boucle sur la totalité des fichiers pdf référencés pour chaque article.
                    nb_info_pdf = 0
                    with open('C:/Users/Sébastien/Desktop/Projet BDDR 2/' + L['pdf'][k].split(';')[i].strip() , encoding="utf8") as file:      #On ouvre le premier fichier pdf.
                        reader = json.load(file)
                        
                        if (len(reader["metadata"]["authors"]) > 0):                        #On calcule ensuite le nombre d'informations que nous donne chaque fichier pdf.
                        
                            for j in range(len(reader["metadata"]["authors"])):
                                if (reader["metadata"]["authors"][j]["first"] != ""):
                                    nb_info_pdf += 1
                                if (reader["metadata"]["authors"][j]["middle"] != ""):
                                    nb_info_pdf += 1
                                if (reader["metadata"]["authors"][j]["last"] != ""):
                                    nb_info_pdf += 1
                                if (reader["metadata"]["authors"][j]["email"] != "" and reader["metadata"]["authors"][j]["email"] != None):
                                    nb_info_pdf += 1
                                if (len(reader["metadata"]["authors"][j]["affiliation"]) >= 1 ):
                                    if (reader["metadata"]["authors"][j]["affiliation"]["institution"] != ""):
                                        nb_info_pdf += 1
                                    if (reader["metadata"]["authors"][j]["affiliation"]["laboratory"] != ""):
                                        nb_info_pdf += 1
                        else:
                            nb_info_pdf = 0                                             #Dans le cas où il n'y a pas d'auteurs dans ce fichier.
                                
                    if (nb_info_pdf >= nb_info_pdf_0):
                        nb_info_pdf_0 = nb_info_pdf                                     #Si le nombre d'info dans ce fichier est supérieur au max du nombre d'infos dans tous les fichiers pdf alors on le change.
                        if (i == 0):
                            liste_fichiers_pdf.append('C:/Users/Sébastien/Desktop/Projet BDDR 2/' + L['pdf'][k].split(';')[i].strip())     #On incrémente notre liste de fichiers pdf par ce même fichier.
                        elif (i >= 1):
                            liste_fichiers_pdf.pop()                                                                                            #Ici, on est dans le cas où on avait déjà incrémenté notre liste de fichiers pdf donc on retire la dernière valeur et on la remplace par la nouvelle qui donne plus d'infos.
                            liste_fichiers_pdf.append('C:/Users/Sébastien/Desktop/Projet BDDR 2/' + L['pdf'][k].split(';')[i].strip())
                       
            else :
                liste_fichiers_pdf.append('C:/Users/Sébastien/Desktop/Projet BDDR 2/' + L['pdf'][k].strip())       #Dans le cas où il n'y a qu'un seul fichier pdf de référencé pour cet article.
        else :
            liste_fichiers_pdf.append('')                                                                               #Dans le cas où la case de la colonne pdf est vide.
            
            
        if (L['pmc'][k] != ""):
            if ';' in L['pmc'][k]:
                for i in range(len(L['pmc'][k].split(';'))):
                    liste_fichiers_pmc.append('C:/Users/Sébastien/Desktop/Projet BDDR 2/' + L['pmc'][k].split(';')[i].strip())         #On a remarqué que les fichiers pmc étaient référencés de manière unique sur chaque article donc pas besoin de calculer le max d'infos sur ces fichiers.
            else :
                liste_fichiers_pmc.append('C:/Users/Sébastien/Desktop/Projet BDDR 2/' + L['pmc'][k].strip())
        else :
            liste_fichiers_pmc.append('')
                

    for k in range(taille):
            
        nb_info_pdf = 0
        nb_info_pmc = 0
            
        if (len(liste_fichiers_pdf[k].split('/')) == 8 and liste_fichiers_pdf[k].split('/')[7] in liste_fichiers_pdf_2):                #On vérifie que mon fichier pdf n'est pas un caractère vide en regardant la taille du split puis on vérifie qu'il existe bien dans nos fichiers pdf de base.
            with open(liste_fichiers_pdf[k] , encoding="utf8") as file:
                reader = json.load(file)
                    
                if (len(reader["metadata"]["authors"]) > 0):
                        
                    for j in range(len(reader["metadata"]["authors"])):
                        if (reader["metadata"]["authors"][j]["first"] != ""):
                            nb_info_pdf += 1
                        if (reader["metadata"]["authors"][j]["middle"] != ""):
                            nb_info_pdf += 1
                        if (reader["metadata"]["authors"][j]["last"] != ""):
                            nb_info_pdf += 1
                        if (reader["metadata"]["authors"][j]["email"] != "" and reader["metadata"]["authors"][j]["email"] != None):
                            nb_info_pdf += 1
                        if (len(reader["metadata"]["authors"][j]["affiliation"]) >= 1 ):
                            if (reader["metadata"]["authors"][j]["affiliation"]["institution"] != ""):
                                nb_info_pdf += 1
                            if (reader["metadata"]["authors"][j]["affiliation"]["laboratory"] != ""):
                                nb_info_pdf += 1                                                                                        #On calcule de nouveau le nombre d'infos données  par le fichier pdf de chaque article.
                    
            
        if (len(liste_fichiers_pmc[k].split('/')) == 8 and liste_fichiers_pmc[k].split('/')[7] in liste_fichiers_pmc_2):
            with open(liste_fichiers_pmc[k] , encoding="utf8") as file:
                reader = json.load(file)
                
                if (len(reader["metadata"]["authors"]) > 0):
                        
                    for j in range(len(reader["metadata"]["authors"])):
                        if (reader["metadata"]["authors"][j]["first"] != ""):
                            nb_info_pmc += 1
                        if (reader["metadata"]["authors"][j]["middle"] != ""):
                            nb_info_pmc += 1
                        if (reader["metadata"]["authors"][j]["last"] != ""):
                            nb_info_pmc += 1
                        if (reader["metadata"]["authors"][j]["email"] != "" and reader["metadata"]["authors"][j]["email"] != None):
                            nb_info_pmc += 1
                        if (len(reader["metadata"]["authors"][j]["affiliation"]) >= 1 ):
                            if (reader["metadata"]["authors"][j]["affiliation"]["institution"] != ""):
                                nb_info_pmc += 1
                            if (reader["metadata"]["authors"][j]["affiliation"]["laboratory"] != ""):
                                nb_info_pmc += 1                                                                                        #On calcule également le nombre d'infos données par le fichier pmc de chaque article.
                
        if (nb_info_pdf > nb_info_pmc):                                                                             #Dans le cas où le pdf donne plus d'infos que le pmc;
            with open(liste_fichiers_pdf[k] , encoding="utf8") as file :
                reader = json.load(file)
                if (len(reader["metadata"]["authors"]) > 0):                                                    
                    for j in range(len(reader["metadata"]["authors"])):                                             #On boucle sur chaque auteur d'un article.
                        liste_1_titre = []                                                                          #On  crée une liste qui va être incrémenté pour chaque auteur d'un article. 
                        liste_1_titre.append(L['title'][k+1])                                                       #La première case de la liste correspond au titre de l'article.
                        liste_1_titre.append(reader["metadata"]["authors"][j]["first"])                             #On récupère son prénom.
                        if (len(reader["metadata"]["authors"][j]["middle"]) >= 1):
                            liste_1_titre.append(''.join(reader["metadata"]["authors"][j]["middle"][0]))            #On récupère son suffixe s'il existe sinon on met un caractère vide.
                        else:
                            liste_1_titre.append('')
                        liste_1_titre.append(reader["metadata"]["authors"][j]["last"])                              #On récupère son nom de famille.
                        if (reader["metadata"]["authors"][j]["email"] == None):
                            liste_1_titre.append('')
                        else : 
                            liste_1_titre.append(reader["metadata"]["authors"][j]["email"])                         #On récupère son email.
                        if (reader["metadata"]["authors"][j]["affiliation"] != {}):
                            liste_1_titre.append(reader["metadata"]["authors"][j]["affiliation"]["institution"])    #On récupère son institution.
                            liste_1_titre.append(reader["metadata"]["authors"][j]["affiliation"]["laboratory"])     #On récupère son laboratoire.
                        else:
                            liste_1_titre.append('')
                            liste_1_titre.append('')
                        liste_1_titre.append(L['date'][k+1])
                        liste_1_titre.append(L['journal'][k+1])
                        liste_1_titre.append(L['url'][k+1])
                        if (L['thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['thematique'][k+1])
                        if (L['sous-thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['sous-thematique'][k+1])
                        liste_auteurs.append(liste_1_titre)                                                         #On incrémente notre liste finale par cette sous-liste qu'on vient de créer.
                            
                                
        elif (nb_info_pmc > nb_info_pdf):                                                                           #On effectue la même chose mais dans le cas où le nombre d'infos est plus important dans le fichier pmc.
            with open(liste_fichiers_pmc[k] , encoding="utf8") as file :
                reader = json.load(file)
                if (len(reader["metadata"]["authors"]) > 0):
                    for j in range(len(reader["metadata"]["authors"])):
                        liste_1_titre = []
                        liste_1_titre.append(L['title'][k+1])
                        liste_1_titre.append(reader["metadata"]["authors"][j]["first"])
                        if (len(reader["metadata"]["authors"][j]["middle"]) >= 1):
                            liste_1_titre.append(''.join(reader["metadata"]["authors"][j]["middle"][0]))
                        else:
                            liste_1_titre.append('')
                        liste_1_titre.append(reader["metadata"]["authors"][j]["last"])
                        if (reader["metadata"]["authors"][j]["email"] == None):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(reader["metadata"]["authors"][j]["email"])
                        if (reader["metadata"]["authors"][j]["affiliation"] != {}):
                            liste_1_titre.append(reader["metadata"]["authors"][j]["affiliation"]["institution"])
                            liste_1_titre.append(reader["metadata"]["authors"][j]["affiliation"]["laboratory"])
                        else:
                            liste_1_titre.append('')
                            liste_1_titre.append('')
                        liste_1_titre.append(L['date'][k+1])
                        liste_1_titre.append(L['journal'][k+1])
                        liste_1_titre.append(L['url'][k+1])
                        if (L['thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['thematique'][k+1])
                        if (L['sous-thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['sous-thematique'][k+1])
                        liste_auteurs.append(liste_1_titre)
          
        elif (nb_info_pmc == nb_info_pdf and nb_info_pmc != 0):                                                 #Dans le cas où les deux fichiers donnent le même nombre d'infos non nul.
            with open(liste_fichiers_pmc[k] , encoding="utf8") as file :
                reader = json.load(file)
                if (len(reader["metadata"]["authors"]) > 0):
                    for j in range(len(reader["metadata"]["authors"])):
                        liste_1_titre = []
                        liste_1_titre.append(L['title'][k+1])
                        liste_1_titre.append(reader["metadata"]["authors"][j]["first"])
                        if (len(reader["metadata"]["authors"][j]["middle"]) >= 1):
                            liste_1_titre.append(''.join(reader["metadata"]["authors"][j]["middle"][0]))
                        else:
                            liste_1_titre.append('')
                        liste_1_titre.append(reader["metadata"]["authors"][j]["last"])
                        if (reader["metadata"]["authors"][j]["email"] == None):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(reader["metadata"]["authors"][j]["email"])
                        if (reader["metadata"]["authors"][j]["affiliation"] != {}):
                            liste_1_titre.append(reader["metadata"]["authors"][j]["affiliation"]["institution"])
                            liste_1_titre.append(reader["metadata"]["authors"][j]["affiliation"]["laboratory"])
                        else:
                            liste_1_titre.append('')
                            liste_1_titre.append('')
                        liste_1_titre.append(L['date'][k+1])
                        liste_1_titre.append(L['journal'][k+1])
                        liste_1_titre.append(L['url'][k+1])
                        if (L['thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['thematique'][k+1])
                        if (L['sous-thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['sous-thematique'][k+1])
                        liste_auteurs.append(liste_1_titre)

                               
        else :                                                                                                          #Dans le cas où les deux fichiers donnent 0 info.
            if (liste_fichiers_pdf[k] == '' and liste_fichiers_pmc[k] == ''):
                if (L['authors'][k+1] != ""):
                    if (";" in L['authors'][k+1]):
                        for i in range(len(L['authors'][k+1].split(';'))):                                         #On va dans la colonne auteurs et à chaque auteur référencé on crée une liste.
                            if ("," in L['authors'][k+1].split(';')[i]):                                           #Dans le cas où le nom et le prénom sont séparés par une virgule.
                                liste_1_titre = []
                                liste_1_titre.append(L['title'][k+1])                                              #On récupère le titre de l'article.
                                if (len(L['authors'][k+1].split(';')[i].split(',')) >= 2):                         #Dans le cas où il y a au moins une virgule.
                                    liste_1_titre.append(L['authors'][k+1].split(';')[i].split(',')[1].strip())    #On récupère le prénom.
                                    liste_1_titre.append('')                                                            #Le suffixe est vide car pas présent.
                                    liste_1_titre.append(L['authors'][k+1].split(';')[i].split(',')[0].strip())    #On récupère le nom de famille.
                                elif (len(L['authors'][k+1].split(';')[i].split(',')) == 1):                       #Dans le cas où la virgule se trouve à la fin sans prénom
                                    liste_1_titre.append(L['authors'][k+1].split(';')[i].split(',')[0].strip())    #On récupère le nom.
                                    liste_1_titre.append('')                                                            #Le suffixe est vide.
                                    liste_1_titre.append('')                                                            #Le prénom est vide.
                                else :
                                    liste_1_titre.append('')
                                    liste_1_titre.append('')
                                    liste_1_titre.append('')
                                liste_1_titre.append('')
                                liste_1_titre.append('')
                                liste_1_titre.append('')
                                liste_1_titre.append(L['date'][k+1])
                                liste_1_titre.append(L['journal'][k+1])
                                liste_1_titre.append(L['url'][k+1])
                                if (L['thematique'][k+1]== 'Inconnu'):
                                    liste_1_titre.append('')
                                else:
                                    liste_1_titre.append(L['thematique'][k+1])
                                if (L['sous-thematique'][k+1]== 'Inconnu'):
                                    liste_1_titre.append('')
                                else:
                                    liste_1_titre.append(L['sous-thematique'][k+1])
                                liste_auteurs.append(liste_1_titre)
                        
                    elif ("," in L['authors'][k+1]):                                                                                                   #Dans le cas où il n' y a pas de point virgule, donc il n'y a qu'un seul auteur.
                        liste_1_titre = []
                        liste_1_titre.append(L['title'][k+1])
                        if (len(L['authors'][k+1].split(',')) >= 2):
                            liste_1_titre.append(L['authors'][k+1].split(',')[1].strip())
                            liste_1_titre.append('')
                            liste_1_titre.append(L['authors'][k+1].split(',')[0].strip())
                        elif (len(L['authors'][k+1].split(',')) == 1):
                            liste_1_titre.append(L['authors'][k+1].strip())
                            liste_1_titre.append('')
                            liste_1_titre.append('')
                        else :
                            liste_1_titre.append('')
                            liste_1_titre.append('')
                            liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append(L['date'][k+1])
                        liste_1_titre.append(L['journal'][k+1])
                        liste_1_titre.append(L['url'][k+1])
                        if (L['thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['thematique'][k+1])
                        if (L['sous-thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['sous-thematique'][k+1])
                        liste_auteurs.append(liste_1_titre)
                        
                    else :
                        liste_1_titre = []
                        liste_1_titre.append(L['title'][k+1])
                        liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append('')
                        liste_1_titre.append(L['date'][k+1])
                        liste_1_titre.append(L['journal'][k+1])
                        liste_1_titre.append(L['url'][k+1])
                        if (L['thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['thematique'][k+1])
                        if (L['sous-thematique'][k+1]== 'Inconnu'):
                            liste_1_titre.append('')
                        else:
                            liste_1_titre.append(L['sous-thematique'][k+1])
                        liste_auteurs.append(liste_1_titre)
                    
                else:                                                                                               #Dans le cas où la case de la colonne auteur est vide.
                    liste_1_titre = []
                    liste_1_titre.append(L['title'][k+1])                                                      #On récupère quand même le titre sans pouvoir récupérer d'autre information.
                    liste_1_titre.append('')
                    liste_1_titre.append('')
                    liste_1_titre.append('')
                    liste_1_titre.append('')
                    liste_1_titre.append('')
                    liste_1_titre.append('')
                    liste_1_titre.append(L['date'][k+1])
                    liste_1_titre.append(L['journal'][k+1])
                    liste_1_titre.append(L['url'][k+1])
                    if (L['thematique'][k+1]== 'Inconnu'):
                        liste_1_titre.append('')
                    else:
                        liste_1_titre.append(L['thematique'][k+1])
                    if (L['sous-thematique'][k+1]== 'Inconnu'):
                        liste_1_titre.append('')
                    else:
                        liste_1_titre.append(L['sous-thematique'][k+1])
                    liste_auteurs.append(liste_1_titre)

    return liste_auteurs


taille_des_donnees = len(data)-1                                                                          #La taille de nos données correspond à celle de data - 1 car on ne s'intéresse pas à la première ligne qui celle du nom des colonnes.
A = ressources(taille_des_donnees) 

compteur_titre = 1

conn = psycopg2.connect(
    dbname = "sebnoel",
    user = "postgres",
    password = "sebnoel",
    host = "localhost", 
    port = '5432')

cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Auteur2 CASCADE;
            CREATE TABLE Auteur2 ( Auteur_id INT PRIMARY KEY, Article_id INT, Titre VARCHAR(10485760), Nom VARCHAR(10485760), Prenom VARCHAR(10485760), Mail VARCHAR(10485760), Institution VARCHAR(10485760), Laboratoire VARCHAR(10485760) ) ;""")
                      

cur.execute("""DROP TABLE IF EXISTS Article2 CASCADE;
            CREATE TABLE Article2 ( Article_id INT, Auteur VARCHAR(10485760), Titre VARCHAR(10485760), Date VARCHAR(10485760), Journal VARCHAR(10485760), Url VARCHAR(10485760), Thematique VARCHAR(10485760), Sous_thematique VARCHAR(10485760), Institution VARCHAR(10485760), Laboratoire VARCHAR(10485760)) ;""")
            
for i in range (len(A)):
    if (A[i][1] != ""):
        if (i < len(A)-1):
            if(A[i][0] == A[i+1][0]):
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],A[i][3],(A[i][1]+" "+A[i][2]).strip(),A[i][4],A[i][5],A[i][6]))
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
            else :
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],A[i][3],(A[i][1]+" "+A[i][2]).strip(),A[i][4],A[i][5],A[i][6]))
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
                
                compteur_titre += 1
        else :
            if (A[i][0] == A[i-1][0]):
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],A[i][3],(A[i][1]+" "+A[i][2]).strip(),A[i][4],A[i][5],A[i][6]))
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
            else:
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],A[i][3],(A[i][1]+" "+A[i][2]).strip(),A[i][4],A[i][5],A[i][6]))
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
                
                compteur_titre += 1
    else:
        if (i < len(A)-1):
            if(A[i][0] == A[i+1][0]):
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],'','','','',''))
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
            else :
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],'','','','',''))
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
                
                compteur_titre += 1
        else :
            if (A[i][0] == A[i-1][0]):
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],'','','','',''))
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
            else :
                cur.execute("""INSERT INTO Auteur2 
                            (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (i+1,compteur_titre,A[i][0],'','','','','')) 
                
                cur.execute("""INSERT INTO Article2
                            (Article_id, Auteur, Titre, Date, Journal, Url, Thematique, Sous_thematique, Institution, Laboratoire)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """,
                            (compteur_titre,A[i][3]+" "+A[i][1],A[i][0],A[i][7],A[i][8],A[i][9],A[i][10],A[i][11],A[i][5], A[i][6]))
                
                compteur_titre += 1

cur.execute("DROP TABLE IF EXISTS Auteur CASCADE;")
cur.execute("CREATE TABLE Auteur AS SELECT * FROM Auteur2 ORDER BY nom ASC, prenom ASC, article_id ASC;")

df = pd.read_sql('SELECT * FROM Auteur', conn)

compteur_auteur = 1

cur.execute("TRUNCATE TABLE Auteur;")


for i in range(len(df)):
    if (i < len(df)-1):
        if (df['nom'][i]+" "+df['prenom'][i] == df['nom'][i+1]+" "+df['prenom'][i+1]):
            cur.execute("""INSERT INTO Auteur 
                        (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                        VALUES
                        (%s,%s,%s,%s,%s,%s,%s,%s)
                        """,
                        (compteur_auteur,df['article_id'][i],df['titre'][i],df['nom'][i],df['prenom'][i],df['mail'][i],df['institution'][i],df['laboratoire'][i]))
        else :
            cur.execute("""INSERT INTO Auteur 
                        (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                        VALUES
                        (%s,%s,%s,%s,%s,%s,%s,%s)
                        """,
                        (compteur_auteur,df['article_id'][i],df['titre'][i],df['nom'][i],df['prenom'][i],df['mail'][i],df['institution'][i],df['laboratoire'][i]))
            compteur_auteur += 1
    else:
        if (df['nom'][i-1]+" "+df['prenom'][i-1] == df['nom'][i]+" "+df['prenom'][i]):
            cur.execute("""INSERT INTO Auteur 
                        (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                        VALUES
                        (%s,%s,%s,%s,%s,%s,%s,%s)
                        """,
                        (compteur_auteur,df['article_id'][i],df['titre'][i],df['nom'][i],df['prenom'][i],df['mail'][i],df['institution'][i],df['laboratoire'][i]))
        else :
            cur.execute("""INSERT INTO Auteur 
                        (Auteur_id, Article_id, Titre, Nom, Prenom, Mail, Institution, Laboratoire)
                        VALUES
                        (%s,%s,%s,%s,%s,%s,%s,%s)
                        """,
                        (compteur_auteur,df['article_id'][i],df['titre'][i],df['nom'][i],df['prenom'][i],df['mail'][i],df['institution'][i],df['laboratoire'][i]))
            compteur_auteur += 1


cur.execute("DROP TABLE IF EXISTS Auteur2 CASCADE;")

cur.execute("DROP TABLE IF EXISTS Article CASCADE;")
cur.execute("CREATE TABLE Article AS SELECT * FROM Article2 ORDER BY titre ASC;")

cur.execute("DROP TABLE IF EXISTS Article2 CASCADE;")

cur.execute("DELETE FROM Auteur WHERE titre='';")
cur.execute("DELETE FROM Article WHERE titre='';")

cur.close()
conn.commit()
conn.close()