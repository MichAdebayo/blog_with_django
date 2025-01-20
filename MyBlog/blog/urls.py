from django.urls import path
from .views import ListeArticlesView, CreerArticleView, CreerCategoryView


urlpatterns = [
    path('', ListeArticlesView.as_view(), name='liste_articles'),
    path('nouveau/', CreerArticleView.as_view(), name='creer_article'),
    path('nouveau_cat/', CreerCategoryView.as_view(), name='creer_category'),
]
