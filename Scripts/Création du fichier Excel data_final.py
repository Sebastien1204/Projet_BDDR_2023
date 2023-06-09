#!/bin/env python3

import os
import psycopg2
from password import *
import pandas as pd
import csv



class Ressource():

    
    def __init__(self):
        self.path = os.getcwd()     #Permet de récupérer le chemin du fichier 
        self.thematique = []        
        self.sous_thematique = []
        self.titre =[]
        self.liste_doi = []


    def verification(self,nom_sous_thematique):         # Cette fonction vérifie les sous_thématiques ( éviter les doublons )
        for i in range(len(self.sous_thematique)):
            for j in range(len(self.sous_thematique[i])):
                if nom_sous_thematique == self.sous_thematique[i][j]:
                    return False
        return True
                


    def extract(self,repo,j = None ,path = None):       #Cette fonction permet de rentrer dans les dossiers et ressortir toutes les sous-thématiques
        if path : 
            a = path
        else:
            a = self.path + '/CORD-19/Kaggle/target_tables'
        b = "/" + str(repo)
        path_2 = a + b
        Ressource.tri(self,path_2,j)                    #On rappelle la fonction tri qui permet de mettre les sous-thématiques dans 


    def tri(self,path = None, j= None):                 #Cette fonction va nous permettre de trier les thématiques et sous-thématiques
        if path:                                           # On va vérifier si on est dans le dossier courant ( Dans ce cas là on utilise le path de self.path )
            new_path = path                                
        else:                                              # Dans le cas où path = None, on remplit les thématiques, dans le cas contraire, on remplit les sous-thématiques 
            new_path = self.path +'/CORD-19/Kaggle/target_tables'

        if path:                                           # 1er cas : path != None, 
            list_files = os.listdir(new_path)              # On récupère la liste des éléments du dossier ( le nom des sous-thématiques)
            self.sous_thematique.append([])                # On ajoute une nouvelle liste de self.sous_thematique
            for i in range(len(list_files)):               
                element = list_files[i]
                if not "." in element :                    # Dans le dernier dossier, on a deux dossiers à traiter, donc on extrait à nouveau les éléments des deux dossiers ( un dossier ne contenant pas de "." dans son nom )
                    Ressource.extract(self,element,j,new_path) 
                    
                elif element != "":
                    self.sous_thematique[j].append(element)
            j+=1
        else:
            list_files = os.listdir(new_path)[1:]          # On ne prend pas en compte le premier dossier ( inutile pour le programme )
            for i in range(len(list_files)):
                element = list_files[i]
                if not "." in element:
                    if element[0] in "12345678":           # On souhaite enlever les numéros qui sont au début
                        #new_element = element.replace("_", " ")     # On remplace les "_" par " "
                        self.thematique.append(element)    # Afin d'etre propre, on enleve le premier espace et on le met en majuscule
                        Ressource.extract(self,element, i)          # On extrait les sous-thématiques
                    else:
                        #new_element = element.replace("_", " ")     
                        self.thematique.append(element)
                        Ressource.extract(self,element, i)


    def recup(self):                                #Cette fonction va lister les titres des articles qui sont dans nos sous-thématiques
        for i in range(len(self.thematique)-1):     #On va dans nos thématiques
            for j in range(len(self.sous_thematique[i])):       #On va dans nos sous-thématiques et on va regarder tous les fichier csv                     
                with open(self.path + "/CORD-19/Kaggle/target_tables" + '/' + str(self.thematique[i])+'/' +str(self.sous_thematique[i][j]), newline='',encoding = "utf8") as csvfile:
                    reader = csv.reader(csvfile)                    #On lit les fichiers csv associés aux sous-thématiques
                    L = []
                    for ligne in reader:
                        L.append(ligne)
                    l = 0
                    while(L[0][l]!= 'Study'):       #On a vu que le titre était dans la colonnes Study, donc on cherche la colonne Study dans l'ensemble des fichier
                        l+=1
                    p = 0
                    while(L[0][p] != 'Study Link'):       #On a vu que le titre était dans la colonnes Study, donc on cherche la colonne Study dans l'ensemble des fichier
                        p+=1
                    for k in range(1,len(L)):       #On ajoute les titres dans la liste
                        self.titre.append([self.thematique[i],self.sous_thematique[i][j],L[k][l],L[k][p]])
        return self.titre
                        

            
    def lien(self):       #permet de récupérer une liste contenant l'ensemble des doi de metadata.csv ( ceux qui n'ont pas de doublons )
        with open (self.path + '/data_sans_doublons_titre.csv', encoding = "utf8") as file:
            reader = csv.reader(file)
            L = []
            for ligne in reader :
                L.append(ligne)
            indice_doi = 0
            while(L[0][indice_doi] != 'doi'):
                indice_doi += 1
            
            for k in range (1,len(L)):
                self.liste_doi.append(L[k][indice_doi])



    def compar(self):   #Compare les doi sur metadata et les thematiques
        for i in range(len(self.titre)):
            if "doi.org" in self.titre[i][3]:
                seq = self.titre[i][3].split("/")
                j = 0
                while not "10." in seq[j] :
                    j += 1
                s = "/".join(seq[j:])
            if s in self.liste_doi:
                self.titre[i].append(s)
            else:
                self.titre[i].append("")


    def ajoute(self):    #Ce programme nous permet d'ajouter les colonnes remplies Thématiques et Sous-Thématiques
        df = pd.read_csv(self.path + '/data_sans_doublons_titre.csv', low_memory = False)
        Theme =[]
        Sous_Theme = []
        M = []
        print(len(self.titre))
        for i in range(len(self.titre)):            #Ici, nous créons la liste avec les thématiques/sous-thématiques et doi associé
            if self.titre[i][4] != "":
                M.append(self.titre[i])
        print(len(M))
        for i in range(len(df['doi'])):
            k = 0                                   
            for j in range(len(M)):
                if df['doi'][i] == M[j][4]:       
                    Theme.append(M[j][0])           # On ajoute la thématique correspondant
                    Sous_Theme.append(M[j][1])      # On ajoute également la sous-thématiques 
                    del M[j]                        #Afin que notre programme tourne plus vite (et comme nous n'avons pas de doublons) on supprime de l'élément utilisé dans la liste avec les thématiques
                    k = 1
                    break   
            if k == 0:                              #Ici si k = 0, l'article ne contient pas de thématique et sous-thématique.
                Theme.append("Inconnu")
                Sous_Theme.append("Inconnu")
        
        df1 = pd.DataFrame([row  for row in Theme],columns = ["thematique"])
        df2 = pd.DataFrame([row for row in Sous_Theme],columns = ["sous-thematique"])
        data = pd.concat([df1,df2,df],axis = 1)
        data_final = data.drop(["who_covidence_id","cord_uid","sha","pmcid","pubmed_id","license","abstract","authors","mag_id","arxiv_id","s2_id"], axis=1)
        data_final.to_csv(self.path + '/data_final.csv',index=False)  

        
        
fichiers = os.listdir(os.getcwd())        

if not 'data_sans_doublons_titre.csv' in fichiers: # On verifie si notre fichier data sans doublons est déjà créé
    
    df = pd.read_csv(os.getcwd()  + '/CORD-19/metadata.csv',low_memory = False)    #creation du fichier data_sans_doublons_titre.csv qui nous sera metadata.csv mais sans doublons
    
    df.drop_duplicates(subset='doi',inplace=True,ignore_index = True)
    
    df.to_csv(os.getcwd()  + '/data_sans_doublons_titre.csv',index=False)  



R = Ressource()
print("Etape 1")
R.tri()
print("Etape 2")
R.recup()
print("Etape 3")
R.lien()
print("Etape 4")
R.compar()
print("Etape 5")
R.ajoute()
