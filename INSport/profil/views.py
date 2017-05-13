from .forms import UserForm, AdherenceForm, SportForm
from tableaubord.models import Utilisateur, Sport, Adherence, Participation
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def Utilisateur(request):
	utilisateur=request.user.profile
	sports=Sport.objects.all()

	form = UserForm(request.POST,request.FILES, instance=utilisateur)
	# Ne marche pas si on ne met pas instance = utilisateur car le champ id serait vide vu qu'on exclu user du formulaire!
	if form.is_valid():
		form.save()
	else:
		form=UserForm(instance=utilisateur)
		form.merge_from_initial()

	#list_exp = AdherenceForm(request.POST, instance=utilisateur)  
	list_exp= sports
	sports = request.POST.getlist('choix')
	print("reter")
	Adherence.objects.filter(adherent_id=request.user.id).delete()
	for sport in sports:
			ad=Adherence(adherent=request.user,sport=Sport.objects.get(pk=sport))
			ad.save()

	form3 = SportForm(request.POST)  
	if form3.is_valid():
		form3.save()  


	return render(request, 'Utilisateur.html', locals())


def profil(request):
	return render(request, 'profil.html')


#@login_required
def monProfil(request):
	if request.user.is_authenticated():
		utilisateur=request.user.profile
		sports=Sport.objects.all()
		adherences=Adherence.objects.all()
		return render(request, 'monProfil.html',locals())
	return redirect('/login')


