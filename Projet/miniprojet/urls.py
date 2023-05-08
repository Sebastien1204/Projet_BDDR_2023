from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thematique', views.index2, name='index2'),
    path('sous_thematique', views.index3, name='index3'),
    path('recherche_thematique', views.index4, name='index4'),
    path('resultat_recherche_thematique', views.index5, name='index5'),
    path('recherche_sous_thematique', views.index6, name='index6'),
    path('resultat_recherche_sous_thematique', views.index7, name='index7'),
    path('accueil_recherche_article',views.index8, name='index8'),
    path('accueil_article',views.index9,name='index9'),
    path('choix_thematique_article',views.index10,name='index10'),
    path('choix_sous_thematique_article',views.index11,name='index11'),
    path('choix_auteur_article',views.index23,name='index23'),
    path('choix_date_article',views.index24,name='index24'),
    path('choix_journal_article',views.index25,name='index25'),
    path('choix_institution_article',views.index26,name='index26'),
    path('choix_laboratoire_article',views.index27,name='index27'),
    path('resultat_recherche_article_thematique', views.index28, name='index28'),
    path('resultat_recherche_article_sous_thematique', views.index29, name='index29'),
    path('resultat_recherche_article_auteur', views.index30, name='index30'),
    path('resultat_recherche_article_date', views.index31, name='index31'),
    path('resultat_recherche_article_journal', views.index32, name='index32'),
    path('resultat_recherche_article_institution', views.index33, name='index33'),
    path('resultat_recherche_article_laboratoire', views.index34, name='index34'),
    path('choix_histogramme_article',views.index14,name='index14'),
    path('choix_date_histogramme',views.index15,name='index15'),
    path('choix_semaine_histogramme',views.index16,name='index16'),
    path('choix_mois_histogramme',views.index17,name='index17'),
    path('choix_annee_histogramme',views.index18,name='index18'),
    path('accueil_auteur',views.index20,name="index20"),
    path('recherche_auteur',views.index21,name="index21"),
    path('resultat_recherche_auteur',views.index22,name="index22"),
    path('choix_titre_article',views.index35,name='index35'),
    path('resultat_recherche_article_titre',views.index36,name='index36'),
    path('accueil_journaux',views.index37,name="index37"),
    path('accueil_recherche_journaux',views.index38,name="index38"),
    path('choix_recherche_journal',views.index39,name="index39"),
    path('resultat_recherche_journal',views.index40,name="index40"),
    path('choix_histogramme_journal',views.index52,name="index52"),
    path('accueil_laboratoires',views.index42,name="index42"),
    path('accueil_recherche_laboratoires',views.index43,name="index43"),
    path('choix_recherche_laboratoire',views.index44,name="index44"),
    path('resultat_recherche_laboratoire',views.index45,name="index45"),
    path('choix_histogramme_laboratoire',views.index46,name="index46"),
    path('accueil_institutions',views.index47,name="index47"),
    path('accueil_recherche_institutions',views.index48,name="index48"),
    path('choix_recherche_institution',views.index49,name="index49"),
    path('resultat_recherche_institution',views.index50,name="index50"),
    path('choix_histogramme_institution',views.index51,name="index51"),
    path('choix_recherche_auteur',views.index53,name="index53"),
    path('choix_nom_auteur',views.index54,name="index54"),
    path('choix_prenom_auteur',views.index55,name="index55"),
    path('choix_titre_auteur',views.index56,name="index56"),
    path('resultat_recherche_auteur_nom',views.index57,name="index57"),
    path('resultat_recherche_auteur_prenom',views.index58,name="index58"),
    path('resultat_recherche_auteur_titre',views.index59,name="index59"),
    path('entree_dates_histogramme',views.index60,name="index60"),
    path('resultat_date_histogramme',views.index61,name='index61'),
    path('resultat_date_tableau',views.index62,name="index62"),
    path('choix_type_resultat_dates',views.index63,name="index63"),
    path('entree_dates_tableau',views.index64,name="index64")
]