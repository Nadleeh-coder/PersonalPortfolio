import datetime
import pandas
import yagmail
# import smtplib
# import socks

from news import NewsFeed

df = pandas.read_excel("files/people.xlsx")
today = datetime.datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
# socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, "https://genproxy.corp.amdocs.com", 8080)
# socks.wrapmodule(smtplib)
for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row["interest"], from_date=yesterday, to_date=today)
    email = yagmail.SMTP("nadleeh.esports@gmail.com", "imqlzlrugrrmwjql")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today.\n {news_feed.create_email()}\nEarle")
