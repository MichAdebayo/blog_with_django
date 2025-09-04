from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
    """Model representing a category of articles."""
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Article(models.Model):
    """Model representing a blog article."""
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titre
