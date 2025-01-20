from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Article, ArticleCategory
from .forms import ArticleForm, CategoryForm

# Create your views here.
class ListeArticlesView(ListView):
    model = Article # Specify the model to use
    template_name = 'blog/liste_articles.html' # Specify the template
    context_object_name = 'articles' # The name to use in the template

    # def get_queryset(self):
    #     articles = Article.objects.all().order_by('-titre')
    #     return articles

    def get_queryset(self):
        # Recover the "q" parameter in the URL
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(titre__icontains=query)
        return Article.objects.all()

class CreerArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/creer_article.html'
    success_url = reverse_lazy('liste_articles') # Redirection after creation

class CreerCategoryView(CreateView):
    model = ArticleCategory
    form_class = CategoryForm
    template_name = 'blog/creer_category.html'
    success_url = reverse_lazy('liste_articles') # Redirection after creation