# CRAWLER
import urllib.request as req
import bs4

# catch ptt src code
def getData(url):
    # establish Request obj, plus "Request Headers" information
    request = req.Request(url, headers = {
        "cookie" : "over18=1",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    #print(data)

    # analyze src code, fetch the title of the article
    root = bs4.BeautifulSoup(data, "html.parser")
    article_titles = root.find_all("div", class_ = "title") # find all tags "div" including class="title" 
    for title in article_titles:
        if title.a != None:      # if tag "a" is not deleted, print it out
            print(title.a.string)
    # catch the next page link
    #nxtLink = root.find_all("a", class_ = "btn wide") # check format
    #print(nxtLink)                                    # check format
    nxtLink = root.find("a", string = "‹ 上頁")
    return nxtLink["href"]

# catch full-page article titles
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
# catch 5 pages titles
while count < 5:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1
