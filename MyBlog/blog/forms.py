from django import forms
from .models import Article, ArticleCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ArticleCategory
        fields = ['name']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'category']