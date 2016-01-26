from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),

	# <127.0.0.1:8000> est la page d'accueil du site <odn974site> 
    url(r'', include('blog.urls')),
    
    

]
