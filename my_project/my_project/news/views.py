from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
@login_required
# Create your views here.
def news(request):
    url = 'https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=f9454a944cd14fdea4fb920d5a5378af'

    news_data=[]
    r = requests.get(url).json()
    print(r)

    for  i in range(5):
        city_news = \
            {
    #           'author' : r['articles'][0]['author'],
    #            'title': r['articles'][0]['title'],
                'description' : r['articles'][i]['description'],
                'image' : r['articles'][i]['urlToImage'],
                   'url' : r['articles'][i]['url']
            }
        news_data.append(city_news)
    #
    context = {

                'news_data' : news_data
              }


    return render(request,'news.html',context)

