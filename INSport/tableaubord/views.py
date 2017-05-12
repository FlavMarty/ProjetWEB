from django.shortcuts import render,redirect
from tableaubord.models import Evenement,Utilisateur, Sport
from datetime import datetime
from .forms import UtilisateurForm,UserForm, createEventForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
#page d'exemple pour afficher des événements --------------
def tableaubord(request):
	exuser=request.user
	exemple=Evenement( nbPlaces=5 , description="C'est un exemple",createur=exuser, sports=Sport.objects.get(id=5),dateheure=datetime(2005,7,15,12,00))
	exemple.save()
	print(exemple.nbPlaces)
	evenements=Evenement.objects.all()
	return render(request,'tableaubord.html',{'evenements':evenements})


#Création compte : ---------------------------------------

def sign1(request):
	form = UserForm(request.POST or None)
	if form.is_valid() :
		new_user = User.objects.create_user(**form.cleaned_data)
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)  # nous connectons l'utilisateur
			return redirect('init')
	return render(request, 'sign1.html',locals())



#Création evenement : ---------------------------------------

def createEvent(request):
	form=createEventForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request, 'createEvent.html',locals())


