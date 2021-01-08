from django.shortcuts import render
from newsapi import NewsApiClient
from decouple import config

# from newsapi.newsapi_clinet import NewsApiClient


def index(request):
    API_KEY = config('API_KEY')
    newsapi = NewsApiClient(api_key=API_KEY)
    headLines = newsapi.get_top_headlines(sources='bbc-news')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)
    context = {"mylist": mylist}

    return render(request, "main/index.html", context)


# Create your views here.
