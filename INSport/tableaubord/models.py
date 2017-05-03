#ici la base de donnée générale, utilisée par toutes les vues

from django.db import models

#Create your models here
class Utilisateur(models.Model):
    nom= models.CharField(max_length=15)
    prenom= models.CharField(max_length=15)
    #dateNaissance= models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    sexe= models.CharField(max_length=6,
                           choices=(
                                    ('M', 'Male'),
                                    ('F', 'Female'),
                                )
                           )
    tel= models.CharField(max_length=12)#voir pour changer avec des forms (pour ne pas pouvoir mettre de num absurde)
    mail= models.CharField(max_length=50)
    #photoProfil= models.ImageField(upload_to="photosProfil/")  #cf settings.py, on a défini comme racine de mediapath deploment/media

class Sport(models.Model):
    #photoSport=  models.ImageField(upload_to="photosSport/")
    nom= models.CharField(max_length=20)

class Evenement(models.Model):
    sports=models.ManyToManyField(Sport) #ManyToManyField permet relation plusieurs a plusieurs (ce qu'on veut ici, un evenement peut avoir +sieurs sport et un sport peut etre affilié a +sieurs evts)
    #date=models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    heure=  models.TimeField(auto_now=True, auto_now_add=False)
    createur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nbPlaces= models.IntegerField()
    description= models.CharField(max_length=250)
    #photoEvt=models.ImageField(upload_to="photosEvt/")

class Adherence(models.Model):
    adherent=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    sport=models.ForeignKey(Sport, on_delete=models.CASCADE)

class Participation:
    participant=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    evenement= models.ForeignKey(Evenement, on_delete=models.CASCADE)