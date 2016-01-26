from django.conf.urls import url
from . import views

urlpatterns = [
    
    # la pae d'accueil du blog liste des post
    url(r'^$', views.post_list, name='post_list'),
]
