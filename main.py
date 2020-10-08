from scraper.scrape import scrape

urls = [
    "https://abcnews.go.com/Health",
    "https://edition.cnn.com/health",
    "https://www.nbcnews.com/health",
    "https://www.dailymail.co.uk/health/index.html",
    "https://www.cbsnews.com/health/",
    "https://www.nytimes.com/section/health",
    "https://www.elitedaily.com/health-wellness-month",
    "https://www.bbc.co.uk/news/health",
    "https://www.cnet.com/health/",
    "https://www.msn.com/en-gb/health"
]

"""
Scrape the news articles
"""
scrape(urls, 'health')