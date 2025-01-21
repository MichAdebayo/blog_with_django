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

class ArticleFilterForm(forms.Form):
    
    titre =  forms.CharField(label="Search by Word", max_length=100, widget=forms.TextInput(attrs={"size" : 17}), required=False)
    category = forms.ModelChoiceField(label="Search by category", queryset=ArticleCategory.objects.all(), required=False) 
    date_publication = forms.DateField(required=False, label="Publication date", widget=forms.DateInput(attrs={'type': 'date'}),
    ) 
