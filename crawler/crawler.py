# CRAWLER
import urllib.request as req

# catch ptt src code
url = "https://www.ptt.cc/bbs/movie/index.html"
# establish Request obj, plus "Request Headers" information
request = req.Request(url, headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)

# analyze src code, fetch the title of the article
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
ptt_title = root.title.string
print(ptt_title)
article_titles = root.find_all("div", class_ = "title") # find all tags "div" including class="title" 
for title in article_titles:
    if title.a != None:      # if tag "a" is not deleted, print it out
        print(title.a.string)

