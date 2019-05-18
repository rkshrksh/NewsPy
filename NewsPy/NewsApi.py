import requests


class NewsApi:
    API_KEY = None
    API_URL = "https://newsapi.org/v2/"

    def __init__(self, API_KEY):
        assert API_KEY is not None, "Please provide api key"
        self.API_KEY = API_KEY

    def _get_news(self, url):
        response = requests.get(url)
        return response.json()

    def get_top_headlines(self, sources=None, q=None, language=None, country=None,
                          category=None, pageSize=20, page=1):
        assert not(sources is None and category is None and country is None and q is None and language is None), "Required parameters are missing. Please set any of the following parameters and try again: sources, q, language, country, category."

        assert not (sources is not None and (country is not None or category is not None)
                    ), "Can't Mix Sources param with Country and Category"

        url = f"{self.API_URL}top-headlines?apiKey={self.API_KEY}"

        if sources is not None:
            url = f"{url}&sources={sources}"

        if q is not None:
            url = f"{url}&q={q}"

        if language is not None:
            url = f"{url}&language={language}"

        if country is not None:
            url = f"{url}&country={country}"

        if category is not None:
            url = f"{url}&category={category}"

        if pageSize is not None:
            url = f"{url}&pageSize={pageSize}"

        if page is not None:
            url = f"{url}&page={page}"

        return self._get_news(url)

    def get_everything(self, q=None, sources=None, domains=None, excludeDomains=None,
                       from_date=None, to_date=None, language=None, sortBy="publishedAt",
                       pageSize=20, page=1):
        assert not (sources is None and q is None and domains is None), "Required parameters are missing. Please set any of the following parameters and try again: sources, q or domains."

        url = f"{self.API_URL}everything?apiKey={self.API_KEY}"

        if sources is not None:
            url = f"{url}&sources={sources}"

        if q is not None:
            url = f"{url}&q={q}"

        if language is not None:
            url = f"{url}&language={language}"

        if domains is not None:
            url = f"{url}&domains={domains}"

        if excludeDomains is not None:
            url = f"{url}&excludeDomains={excludeDomains}"

        if from_date is not None:
            url = f"{url}&from={from_date}"

        if to_date is not None:
            url = f"{url}&to={to_date}"

        if sortBy is not None:
            url = f"{url}&sortBy={sortBy}"

        if pageSize is not None:
            url = f"{url}&pageSize={pageSize}"

        if page is not None:
            url = f"{url}&page={page}"

        return self._get_news(url)
