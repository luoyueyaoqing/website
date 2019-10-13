from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def base(request):
    articles = Article.objects.all()
    return render(request, 'base.html', {'articles': articles})




