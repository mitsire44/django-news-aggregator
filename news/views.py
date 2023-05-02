from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News
from bs4 import BeautifulSoup
import requests

def index(request):
    headlines = News.objects.all()[::-1]
    context = {'news':headlines}
    return render(request, 'news/index.html', context)

def scrape(request):
    sauce = requests.get('https://www.theonion.com/').text
    soup = BeautifulSoup(sauce, 'lxml')

    for article in soup.find_all('article'):
        tit = article.h4.text
        url = article.a['href']
        new_headline = News()
        new_headline.title = tit
        new_headline.url = url
        new_headline.save()
    return redirect("../")



