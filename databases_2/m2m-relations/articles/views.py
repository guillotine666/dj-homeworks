from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related(
        Prefetch('scopes', queryset=ArticleScope.objects.order_by(
            '-is_main').select_related('topic')))
    context = {'object_list': articles}

    return render(request, template, context)
