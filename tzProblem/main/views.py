from django.shortcuts import render, redirect

from main.forms import ArticleForm
from main.models import Article
from django.utils import timezone


# Create your views here.
def main(request):
    if request.method=='GET':
        articles = Article.objects.all()

        for article in articles:
            print('In view (8 hrs short): ', article.pubDateTime)
            print('In view, fix date time: ', timezone.localtime(article.pubDateTime))

        return render(request, 'main/base.html', {'articles':articles,
                                                  'articleForm':ArticleForm(instance=articles.first())})
    
    #POST
    articleForm = ArticleForm(request.POST)
    articleForm.save()
    
    return redirect('main:main')