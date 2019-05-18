import os
from NewsPy import NewsApi

# use your own api key from newsapi.org
news = NewsApi(os.environ.get("NEWS_API_KEY"))

my_news = news.get_everything(q="tech")

status = my_news["status"]
count = my_news["totalResults"]
articles = my_news["articles"]

print(articles[0])
