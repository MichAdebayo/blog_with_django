from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Article, ArticleCategory
from .forms import ArticleForm, CategoryForm, ArticleFilterForm


class ListeArticlesView(FormView, ListView):
    """View to list and filter articles."""
    model = Article # Specify the model to use
    template_name = 'blog/liste_articles.html' # Specify the template
    context_object_name = 'articles' # The name to use in the template
    form_class = ArticleFilterForm

    def get_queryset(self):
        """Returns a filtered queryset of articles based on form input.
        
        This method filters articles by title, category, and publication date if provided in the GET request.

        Returns:
            QuerySet: A queryset of Article objects filtered according to the form data.
        """
        queryset =  super().get_queryset()
        
        form = ArticleFilterForm(self.request.GET)

        if form.is_valid():
            search_title = form.cleaned_data.get('titre')
            search_category = form.cleaned_data.get('category')
            search_date = form.cleaned_data.get('date_publication')

            filtered_article_set = {}
        
            if search_title:
                filtered_article_set['titre__icontains'] = search_title
            if search_category:
                filtered_article_set['category'] = search_category
            if search_date:
                filtered_article_set['date_publication'] = search_date

            queryset = queryset.filter(**filtered_article_set)

        return queryset


class CreerArticleView(CreateView):
    """View to create a new article."""
    model = Article
    form_class = ArticleForm
    template_name = 'blog/creer_article.html'
    success_url = reverse_lazy('liste_articles') # Redirection after creation

class CreerCategoryView(CreateView):
    """View to create a new article category."""
    model = ArticleCategory
    form_class = CategoryForm
    template_name = 'blog/creer_category.html'
    success_url = reverse_lazy('liste_articles') # Redirection after creation
