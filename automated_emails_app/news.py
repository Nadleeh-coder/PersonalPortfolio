import requests


class NewsFeed:
    """ Representing multiple news titles and links as a single string. """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "cfd652b1a8994d949725e9881aefa244"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def create_email(self):
        url = self._build_url()
        articles = self._get_articles(url)

        email_body = ""
        for article in articles:
            email_body += f"{article['title']}\n{article['url']}\n\n"

        return email_body

    @staticmethod
    def _get_articles(url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = (f"{self.base_url}"
               f"q={self.interest}&"
               f"searchIn=title&"
               f"from={self.from_date}&"
               f"to={self.to_date}&"
               f"language={self.language}&"
               f"apiKey={self.api_key}")

        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest="apple", from_date="2025-03-10", to_date="2025-03-11", language="en")
    print(news_feed.create_email())
