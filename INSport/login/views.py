from django.contrib.auth import authenticate, login
from .forms import ConnexionForm
from django.shortcuts import render,redirect

def connexion(request):
	error = False

	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user) 
				return redirect('/')# nous connectons l'utilisateur
		else: # sinon une erreur sera affichée
		        error = True
	else:
		form = ConnexionForm()

	return render(request, 'connexion.html', locals())
