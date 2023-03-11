import bs4
import requests

url="https://github.com/pricing"
data= requests.get(url)
soup= bs4.BeautifulSoup(data.text , "html.parser")
#print(soup.prettify())
for link in soup.find_all('img'):
    #links=link.get("src")
    #print(links)
    links=link.get('href')
    if links[:3]=="../"and links!="#":
        print("https://github.com/pricing" +links[2:len(links)])
    elif links[0]=="/"and links!="#":
        print("https://github.com/pricing"+ links)