from django.shortcuts import render
from .models import Article, Tag

def blog_list(request):
    # load all blog articles from database
    articles = Article.objects.filter().order_by('-created_on')
    ctx = {
        'articles': articles,
    }
    return render(request, 'blog/list.html', ctx)