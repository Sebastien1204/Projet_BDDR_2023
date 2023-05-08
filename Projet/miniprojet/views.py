from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, When
from miniprojet.models import thematique, sous_thematique, auteur, article, journaux, dates, laboratoires, institutions
from datetime import datetime, timedelta
from io import BytesIO
import matplotlib.pyplot as plt



def index(request):
    return render (request,'affichage_accueil.html')

def index2(request):
    a = thematique.objects.all()
    return render(request,'affichage_thematique.html',{'thematique':a})

def index3(request):
    a = sous_thematique.objects.all()
    return render(request,'affichage_sous_thematique.html',{'sous_thematique':a})

def index4(request):
    return render(request,'recherche_thematique.html')
    
def index5(request):
    all_thematique = thematique.objects.all()
    thematique_qs = all_thematique
    for i in dict(request.GET):
        if i == 'thematique_id':
            thematique_id = request.GET.get('thematique_id')
            if thematique_id != "":
                thematique_qs = thematique_qs.filter(Q(thematique_id=thematique_id))
        if i == 'nom':
            nom = request.GET.get('nom')
            if nom != "":
                thematique_qs = thematique_qs.filter(Q(nom=nom))
    return render(request,'resultat_recherche_thematique.html',{
        'all_thematique' : all_thematique,
        'thematique_qs' : thematique_qs
    }) 

def index6(request):
    return render(request,'recherche_sous_thematique.html')
    
def index7(request):
    all_sous_thematique = sous_thematique.objects.all()
    sous_thematique_qs = all_sous_thematique
    for i in dict(request.GET):
        if i == 'sous_thematique_id':
            sous_thematique_id = request.GET.get('sous_thematique_id')
            if sous_thematique_id != "":
                sous_thematique_qs = sous_thematique_qs.filter(Q(sous_thematique_id=sous_thematique_id))
        if i == 'thematique_id':
            thematique_id = request.GET.get('thematique_id')
            if thematique_id != "":
                sous_thematique_qs = sous_thematique_qs.filter(Q(thematique_id=thematique_id))
        if i == 'nom':
            nom = request.GET.get('nom')
            if nom != "":
                sous_thematique_qs = sous_thematique_qs.filter(Q(nom=nom))
    return render(request,'resultat_recherche_sous_thematique.html',{
        'all_sous_thematique' : all_sous_thematique,
        'sous_thematique_qs' : sous_thematique_qs
    })

def index8(request):
    return render(request,'accueil_recherche_article.html')

def index9(request):
    a = article.objects.all()[1000000:1000020]
    return render(request,'accueil_article.html',{'article':a})

def index10(request):
    return render(request,'choix_thematique_article.html')

def index11(request):
    return render(request,'choix_sous_thematique_article.html')

def index12(request):
    all_sous_thematique = sous_thematique.objects.all()
    sous_thematique_qs = all_sous_thematique
    for i in dict(request.GET):
        if i == 'thematique_id':
            thematique_id = request.GET.get('thematique_id')
            if thematique_id != "":
                sous_thematique_qs = sous_thematique_qs.filter(Q(thematique_id=thematique_id))
    return render(request,'resultat_recherche_article_thematique.html',{
        'all_sous_thematique' : all_sous_thematique,
        'sous_thematique_qs' : sous_thematique_qs
    })

def index13(request):
    all_sous_thematique = sous_thematique.objects.all()
    sous_thematique_qs = all_sous_thematique
    for i in dict(request.GET):
        if i == 'sous_thematique_id':
            sous_thematique_id = request.GET.get('sous_thematique_id')
            if sous_thematique_id != "":
                sous_thematique_qs = sous_thematique_qs.filter(Q(sous_thematique_id=sous_thematique_id))
    return render(request,'resultat_recherche_article_sous_thematique.html',{
        'all_sous_thematique' : all_sous_thematique,
        'sous_thematique_qs' : sous_thematique_qs
    })

def index14(request):
    return render(request,'choix_tableau_article.html')

def index15(request):
    return render(request,'entree_dates_histogramme.html')

def index16(request):
    return render(request,'choix_semaine_histogramme.html')

def index17(request):
    return render(request,'choix_mois_histogramme.html')

def index18(request):
    return render(request,'choix_annee_histogramme.html')

def index19(request):
    return render(request,'accueil_auteur.html')

def index20(request):
    a = auteur.objects.all()[1000000:1000020]
    return render(request,'accueil_auteur.html',{'auteur':a})

def index21(request):
    return render(request,'recherche_auteur.html')

def index22(request):
    all_auteur = auteur.objects.all()
    auteur_qs = all_auteur
    for i in dict(request.GET):
        if i == 'nom':
            nom = request.GET.get('nom')
            if nom != "":
                auteur_qs = auteur_qs.filter(Q(nom=nom))
        if i == 'prenom':
            prenom = request.GET.get('prenom')
            if prenom != "":
                auteur_qs = auteur_qs.filter(Q(prenom=prenom))
        if i == 'titre':
            titre = request.GET.get('titre')
            if titre != "":
                auteur_qs = auteur_qs.filter(Q(titre=titre))
    return render(request,'resultat_recherche_auteur.html',{
        'all_auteur' : all_auteur,
        'auteur_qs' : auteur_qs
    })

def index23(request):
    return render(request,'choix_auteur_article.html')

def index24(request):
    return render(request,'choix_date_article.html')

def index25(request):
    return render(request,'choix_journal_article.html')

def index26(request):
    return render(request,'choix_institution_article.html')

def index27(request):
    return render(request,'choix_laboratoire_article.html')

def index28(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'thematique':
            thematique = request.GET.get('thematique')
            if thematique != "":
                article_qs = article_qs.filter(Q(thematique=thematique))
    return render(request,'resultat_recherche_article_thematique.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index29(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'sous_thematique':
            sous_thematique = request.GET.get('sous_thematique')
            if sous_thematique != "":
                article_qs = article_qs.filter(Q(sous_thematique=sous_thematique))
    return render(request,'resultat_recherche_article_sous_thematique.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index30(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'auteur':
            auteur = request.GET.get('auteur')
            if auteur != "":
                article_qs = article_qs.filter(Q(auteur=auteur))
    return render(request,'resultat_recherche_article_auteur.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index31(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'date':
            date = request.GET.get('date')
            if date != "":
                article_qs = article_qs.filter(Q(date=date))
    return render(request,'resultat_recherche_article_date.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index32(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'journal':
            journal = request.GET.get('journal')
            if journal != "":
                article_qs = article_qs.filter(Q(journal=journal))
    return render(request,'resultat_recherche_article_journal.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index33(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'institution':
            institution = request.GET.get('institution')
            if institution != "":
                article_qs = article_qs.filter(Q(institution=institution))
    return render(request,'resultat_recherche_article_institution.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index34(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'laboratoire':
            laboratoire = request.GET.get('laboratoire')
            if laboratoire != "":
                article_qs = article_qs.filter(Q(laboratoire=laboratoire))
    return render(request,'resultat_recherche_article_laboratoire.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index35(request):
    return render(request,'choix_titre_article.html')

def index36(request):
    all_article = article.objects.all()
    article_qs = all_article
    for i in dict(request.GET):
        if i == 'titre':
            titre = request.GET.get('titre')
            if titre != "":
                article_qs = article_qs.filter(Q(titre=titre))
    return render(request,'resultat_recherche_article_titre.html',{
        'all_article' : all_article,
        'article_qs' : article_qs
    })

def index37(request):
    a = journaux.objects.all()[:25]
    return render(request,'accueil_journaux.html',{'journaux' : a})

def index38(request):
    return render(request,'accueil_recherche_journaux.html')

def index39(request):
    return render(request,'choix_recherche_journal.html')

def index40(request):
    all_journaux = journaux.objects.all()
    journaux_qs = all_journaux
    for i in dict(request.GET):
        if i == 'journal':
            journal = request.GET.get('journal')
            if journal != "":
                journaux_qs = journaux_qs.filter(Q(journal=journal))
    return render(request,'resultat_recherche_journal.html',{
        'all_journaux' : all_journaux,
        'journaux_qs' : journaux_qs
    })

def index41(request):
    return render(request,'choix_histogramme_journal.html')

def index42(request):
    a = laboratoires.objects.all()[:25]
    return render(request,'accueil_laboratoires.html',{'laboratoires' : a})

def index43(request):
    return render(request,'accueil_recherche_laboratoires.html')

def index44(request):
    return render(request,'choix_recherche_laboratoire.html')

def index45(request):
    all_laboratoires = laboratoires.objects.all()
    laboratoires_qs = all_laboratoires
    for i in dict(request.GET):
        if i == 'laboratoire':
            laboratoire = request.GET.get('laboratoire')
            if laboratoire != "":
                laboratoires_qs = laboratoires_qs.filter(Q(laboratoire=laboratoire))
    return render(request,'resultat_recherche_laboratoire.html',{
        'all_laboratoires' : all_laboratoires,
        'laboratoires_qs' : laboratoires_qs
    })

def index46(request):
    return render(request,'choix_histogramme_laboratoire.html')

def index47(request):
    a = institutions.objects.all()[:25]
    return render(request,'accueil_institutions.html',{'institutions' : a})

def index48(request):
    return render(request,'accueil_recherche_institutions.html')

def index49(request):
    return render(request,'choix_recherche_institution.html')

def index50(request):
    all_institutions = institutions.objects.all()
    institutions_qs = all_institutions
    for i in dict(request.GET):
        if i == 'institution':
            institution = request.GET.get('institution')
            if institution != "":
                institutions_qs = institutions_qs.filter(Q(institution=institution))
    return render(request,'resultat_recherche_institution.html',{
        'all_institutions' : all_institutions,
        'institutions_qs' : institutions_qs
    })

def index51(request):
    return render(request,'choix_histogramme_institution.html')

def index52(request):
    return render(request, 'choix_histogramme_journal.html')

def index53(request):
    return render(request, 'choix_recherche_auteur.html')

def index54(request):
    return render(request, 'choix_nom_auteur.html')

def index55(request):
    return render(request, 'choix_prenom_auteur.html')

def index56(request):
    return render(request, 'choix_titre_auteur.html')

def index57(request):
    all_auteur = auteur.objects.all()
    auteur_qs = all_auteur
    for i in dict(request.GET):
        if i == 'nom':
            nom = request.GET.get('nom')
            if nom != "":
                auteur_qs = auteur_qs.filter(Q(nom=nom))
    return render(request,'resultat_recherche_auteur_nom.html',{
        'all_auteur' : all_auteur,
        'auteur_qs' : auteur_qs
    })

def index58(request):
    all_auteur = auteur.objects.all()
    auteur_qs = all_auteur
    for i in dict(request.GET):
        if i == 'prenom':
            prenom = request.GET.get('prenom')
            if prenom != "":
                auteur_qs = auteur_qs.filter(Q(prenom=prenom))
    return render(request,'resultat_recherche_auteur_prenom.html',{
        'all_auteur' : all_auteur,
        'auteur_qs' : auteur_qs
    })

def index59(request):
    all_auteur = auteur.objects.all()
    auteur_qs = all_auteur
    for i in dict(request.GET):
        if i == 'titre':
            titre = request.GET.get('titre')
            if titre != "":
                auteur_qs = auteur_qs.filter(Q(titre=titre))
    return render(request,'resultat_recherche_auteur_titre.html',{
        'all_auteur' : all_auteur,
        'auteur_qs' : auteur_qs
    })

def index60(request):
    return render(request,'entree_dates_histogramme.html')

def index61(request):
    all_dates = dates.objects.all()
    dates_qs = all_dates
    for i in dict (request.GET):
        if i == 'date_debut':
            date_debut = request.GET.get('date_debut')
            date_fin = request.GET.get('date_fin')

    format1 = "%Y-%m-%d"
    format2 = "%Y-%m"
    format3 = "%Y"

    if (len(date_debut) > 7):
        date_1 = datetime.strptime(date_debut, format1)
    elif(len(date_debut) <= 7 and len(date_debut) > 4):
        date_1 = datetime.strptime(date_debut, format2)
    else :
        date_1 = datetime.strptime(date_debut, format3)

    if (len(date_fin) > 7):
        date_2 = datetime.strptime(date_fin, format1)
    elif(len(date_fin) <= 7 and len(date_fin) > 4):
        date_2 = datetime.strptime(date_fin, format2)
    else :
        date_2 = datetime.strptime(date_fin, format3)    
    
    intervalle = (date_2 - date_1).days + 1
    
    liste_dates_intervalle = []
    
    for i in range(intervalle):
        liste_dates_intervalle.append(datetime.strftime(date_1 + timedelta(i), format1))

    dates_qs = dates_qs.filter(Q(Q(date__in=liste_dates_intervalle)))

    dates_qs = dates_qs.order_by('date')

    liste_dates_dans_base_de_donnees = []

    for i in range(dates.objects.count()):
        liste_dates_dans_base_de_donnees.append(dates.objects.values_list('date')[i][0])

    liste_quantites_intervalle = []

    for i in range(len(liste_dates_intervalle)):
        if(liste_dates_intervalle[i] in liste_dates_dans_base_de_donnees):
            liste_quantites_intervalle.append(dates_qs.get(date=liste_dates_intervalle[i]).quantite)
        else:
            liste_quantites_intervalle.append(0)

    a = plt.plot(liste_dates_intervalle,liste_quantites_intervalle)
    plt.xlabel('Dates')
    plt.ylabel("Nombre d'articles")
    plt.title("Histogramme d'articles par date")
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type='image/png')

def index62(request):
    all_dates = dates.objects.all()
    dates_qs = all_dates
    for i in dict (request.GET):
        if i == 'date_debut':
            date_debut = request.GET.get('date_debut')
            date_fin = request.GET.get('date_fin')

    format1 = "%Y-%m-%d"
    format2 = "%Y-%m"
    format3 = "%Y"

    if (len(date_debut) > 7):
        date_1 = datetime.strptime(date_debut, format1)
    elif(len(date_debut) <= 7 and len(date_debut) > 4):
        date_1 = datetime.strptime(date_debut, format2)
    else :
        date_1 = datetime.strptime(date_debut, format3)

    if (len(date_fin) > 7):
        date_2 = datetime.strptime(date_fin, format1)
    elif(len(date_fin) <= 7 and len(date_fin) > 4):
        date_2 = datetime.strptime(date_fin, format2)
    else :
        date_2 = datetime.strptime(date_fin, format3)
    
    intervalle = (date_2 - date_1).days + 1
    
    liste_dates_intervalle = []
    
    for i in range(intervalle):
        liste_dates_intervalle.append(datetime.strftime(date_1 + timedelta(i), format1))

    dates_qs = dates_qs.filter(Q(Q(date__in=liste_dates_intervalle)))

    dates_qs = dates_qs.order_by('date')

    return render(request,'resultat_date_tableau.html',{
        'all_dates' : all_dates,
        'dates_qs' : dates_qs
    })

def index63(request):
    return render(request,'choix_type_resultat_dates.html')

def index64(request):
    return render(request,'entree_dates_tableau.html')
