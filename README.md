# NewsPy
Python wrapper Library for https://newsapi.org/

```python
from NewsPy import NewsApi

# use your own api key from newsapi.org
news = NewsApi("YOUR-API-KEY")

my_news = news.get_everything(q="tech")

status = my_news["status"]
count = my_news["totalResults"]
articles = my_news["articles"]

print(articles)
```