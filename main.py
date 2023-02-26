import feedparser
from transformers import pipeline
from bs4 import BeautifulSoup
import requests
summarizer = pipeline("summarization")
feed = feedparser.parse("https://www.pythonforbeginners.com/feed/")
link = feed.entries[0].link # get the link of the first entry
response = requests.get(link) # get the HTML content of the link
soup = BeautifulSoup(response.text, "html.parser") # parse the HTML with beautifulsoup
article = soup.find("div", class_="entry-content").get_text() # find and get the text of the article content
summary = summarizer(article, max_length=60, min_length=40)
print(summary[0]["summary_text"])

