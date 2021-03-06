"""INSport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from accueil.views import doc

urlpatterns = [
    url(r'^$',include('accueil.urls'),name='home'),
    url(r'^evenement/',include('evenement.urls'),name='evenement'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', include('logout.urls'),name='logout'),
    url(r'^swipe/', include('swipe.urls'),name='swipe'),
    url(r'^login/', include('login.urls'),name='login'),
    url(r'^tableaubord/', include('tableaubord.urls')),
	url(r'^profil/', include('profil.urls')),
    url(r'^init/',include('init.urls'),name='init'),
    url(r'^doc/',doc),

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
