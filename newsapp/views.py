from django.shortcuts import render
import requests
API_KEY = 'd17d1dc9c63b4644b36048b370d5fea1'


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request, 'base.html', context)


def index(request):
    return render(request, 'main.html')
# Create your views here.
