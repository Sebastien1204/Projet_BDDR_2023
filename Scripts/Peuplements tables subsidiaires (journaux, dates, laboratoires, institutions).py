# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:44:59 2023

@author: Sébastien
"""

import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname = "sebnoel",
    user = "postgres",
    password = "sebnoel",
    host = "localhost", 
    port = '5432')

cur = conn.cursor()

journaux = pd.read_sql('SELECT * FROM Article', conn)
journaux.drop_duplicates(subset=['titre'],inplace=True)

journaux = journaux['journal'].value_counts()
journaux = journaux.to_frame()

cur.execute("""DROP TABLE IF EXISTS Journaux CASCADE;
            CREATE TABLE Journaux ( Journal_id INT PRIMARY KEY, Journal VARCHAR(10485760), Quantite INT ) ;""")
            
for i in range(len(journaux)):
    cur.execute("""INSERT INTO Journaux 
                (Journal_id, Journal, Quantite)
                VALUES
                (%s,%s,%s)
                """,
                (i+1,journaux.index[i],journaux['journal'][i]))
    
    
dates = pd.read_sql('SELECT * FROM Article', conn)
dates.drop_duplicates(subset=['titre'],inplace=True)

dates = dates['date'].value_counts()
dates = dates.to_frame()

cur.execute("""DROP TABLE IF EXISTS Dates CASCADE;
            CREATE TABLE Dates ( Date_id INT PRIMARY KEY, Date VARCHAR(10485760), Quantite INT ) ;""")
            
for i in range(len(dates)):
    cur.execute("""INSERT INTO Dates 
                (Date_id, Date, Quantite)
                VALUES
                (%s,%s,%s)
                """,
                (i+1,dates.index[i],dates['date'][i]))
    
laboratoires = pd.read_sql('SELECT * FROM Article', conn)
laboratoires.drop_duplicates(subset=['titre'],inplace=True)

laboratoires = laboratoires['laboratoire'].value_counts()
laboratoires = laboratoires.to_frame()

cur.execute("""DROP TABLE IF EXISTS Laboratoires CASCADE;
            CREATE TABLE Laboratoires ( Laboratoire_id INT PRIMARY KEY, Laboratoire VARCHAR(10485760), Quantite INT ) ;""")
            
for i in range(len(laboratoires)):
    cur.execute("""INSERT INTO Laboratoires 
                (Laboratoire_id, Laboratoire, Quantite)
                VALUES
                (%s,%s,%s)
                """,
                (i+1,laboratoires.index[i],laboratoires['laboratoire'][i]))
    
institutions = pd.read_sql('SELECT * FROM Article', conn)
institutions.drop_duplicates(subset=['titre'],inplace=True)

institutions = institutions['institution'].value_counts()
institutions = institutions.to_frame()

cur.execute("""DROP TABLE IF EXISTS Institutions CASCADE;
            CREATE TABLE Institutions ( Institution_id INT PRIMARY KEY, Institution VARCHAR(10485760), Quantite INT ) ;""")
            
for i in range(len(institutions)):
    cur.execute("""INSERT INTO Institutions 
                (Institution_id, Institution, Quantite)
                VALUES
                (%s,%s,%s)
                """,
                (i+1,institutions.index[i],institutions['institution'][i]))

cur.close()
conn.commit()
conn.close()