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

    for  i in range(6):
        city_news = \
            {
    #           'author' : r['articles'][0]['author'],
               'title': r['articles'][i]['title'],
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

def category(request,tag):
    url = "https://newsapi.org/v2/everything?q={}&apiKey=f9454a944cd14fdea4fb920d5a5378af"
    category=tag
    category_data = []
    a=category




    c = requests.get(url.format(category)).json()
    print(c)

    for  i in range(6):
        category_news = \
            {

    #           'author' : r['articles'][0]['author'],
    #            'title': r['articles'][0]['title'],
                'description' : c['articles'][i]['description'],
                # 'image' : c['articles'][i]['urlToImage'],
                    'url' : c['articles'][i]['url']
            }
        category_data.append(category_news)
    #
    context = {
                'category':a,
                'category_data' : category_data
              }


    return render(request,'category.html',context)





def about(request):
    return render(request,'about.html')



