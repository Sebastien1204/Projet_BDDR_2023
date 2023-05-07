from django.db import models
from django.contrib import admin
from sqlalchemy import ForeignKey
from django.template.defaultfilters import urlize

class thematique(models.Model):
    thematique_id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length = 100)
    class Meta : 
        managed = False
        db_table = 'thematique'

class sous_thematique(models.Model):
    sous_thematique_id = models.AutoField(primary_key = True)
    thematique_id = models.IntegerField()
    nom = models.CharField(max_length = 100)
    class Meta :
        managed = False
        db_table = 'sous_thematique'

class auteur(models.Model):
    auteur_id = models.AutoField(primary_key = True)
    article_id = models.IntegerField()
    titre = models.CharField(max_length = 10485760)
    nom = models.CharField(max_length = 10485760)
    prenom = models.CharField(max_length = 10485760)
    mail = models.CharField(max_length = 10485760)
    institution = models.CharField(max_length = 10485760)
    laboratoire = models.CharField(max_length = 10485760)
    class Meta :
        managed = False
        db_table = 'auteur'

class article(models.Model):
    article_id = models.IntegerField(primary_key = True)
    auteur = models.CharField(max_length = 10485760)
    titre = models.CharField(max_length = 10485760)
    date = models.CharField(max_length = 10485760)
    journal = models.CharField(max_length = 10485760)
    url = models.CharField(max_length = 10485760)
    thematique = models.CharField(max_length = 10485760)
    sous_thematique = models.CharField(max_length = 10485760)
    institution = models.CharField(max_length = 10485760)
    laboratoire = models.CharField(max_length = 10485760)

    def lien_url(self):
        return urlize(self.url)
    
    class Meta :
        managed = False
        db_table = 'article'

class journaux(models.Model):
    journal_id = models.IntegerField(primary_key = True)
    journal = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'journaux'

class dates(models.Model):
    date_id = models.IntegerField(primary_key = True)
    date = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'dates'

class laboratoires(models.Model):
    laboratoire_id = models.IntegerField(primary_key = True)
    laboratoire = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'laboratoires'

class institutions(models.Model):
    institution_id = models.IntegerField(primary_key = True)
    institution = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'institutions'