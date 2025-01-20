from django.urls import path
from . import views


urlpatterns = [
    path(' ', views.liste_articles, name='liste_articles'),
]
