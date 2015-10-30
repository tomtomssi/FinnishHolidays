from bs4 import BeautifulSoup as Soup
import urllib.request

myFile = open("dates.txt", 'w')
myFile.truncate()

urlStrs = [
    "http://www.webcal.fi/fi-FI/pyhat.php?y=2015",
    "http://www.webcal.fi/fi-FI/pyhat.php?y=2016",
    "http://www.webcal.fi/fi-FI/pyhat.php?y=2017",
    "http://www.webcal.fi/fi-FI/pyhat.php?y=2018",
    "http://www.webcal.fi/fi-FI/pyhat.php?y=2019",
    "http://www.webcal.fi/fi-FI/pyhat.php?y=2020"
]

for urlStr in urlStrs:
    soup = Soup(urllib.request.urlopen(urlStr), "html.parser")
    for tr in soup.findAll("tr")[1:]:
        for td in tr.findAll("td")[3]:
            myFile.write(td.replace('.', '-') + '\n')
