import feedparser
from transformers import pipeline
from bs4 import BeautifulSoup
summarizer = pipeline("summarization")
feed = feedparser.parse("https://azure.microsoft.com/fr-fr/blog/feed/")
articles = feed.entries
souped = []

for article in articles:
    souped.append({
        "title": article.title,
        "content": BeautifulSoup(article.content[0].value, "html.parser").get_text()
    })
tokenizer = pipeline("summarization", max_length=512, truncation=True)
for article in souped:
    # check if the article has text
    if article:
        try:
            summary = tokenizer(article["content"], max_length=60, min_length=40)
            print("========================")
            print("->", article["title"])
            print(summary[0]["summary_text"])
        except IndexError:
            # catch the exception and continue
            print("Could not generate summary for this article.")
            continue


