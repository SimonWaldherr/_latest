from scraper.scrape import scrape

urls = [
    'http://abcnews.go.com/',
    'http://www.cnn.com/',
    'http://www.nbcnews.com/',
    'http://www.huffingtonpost.com/',
    'http://www.cbsnews.com/',
    'http://www.usatoday.com/',
    'http://www.nytimes.com/',
    'http://www.foxnews.com/',
    'http://www.dailymail.co.uk/ushome/index.html',
    'http://www.washingtonpost.com/',
    'http://bleacherreport.com/',
    'http://www.businessinsider.com/',
    'http://www.bbc.com/',
    'http://www.theguardian.com/us',
    'http://www.msn.com/en-us/news',
    'http://www.npr.org/',
    'http://www.nydailynews.com/',
    'http://www.latimes.com/',
    'http://nypost.com/',
    'http://time.com/',
    'http://mashable.com/',
    'http://www.telegraph.co.uk/',
    'http://www.usnews.com/',
    'http://www.vice.com/en_us',
    'http://www.mirror.co.uk/news/',
    'http://www.independent.co.uk/',
    'http://techcrunch.com/',
]

"""
Scrape the news articles
"""
scrape(urls, 'latest')
