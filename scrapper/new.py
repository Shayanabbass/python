from urllib import request
URL="https://olympus.realpython.org/poseidon"
html=request.urlopen(URL).read().decode("CP1252")
  
webpageashtml=html
#print(webpageashtml)
htmllist=html.split("\n")
#print(htmllist)
for links in htmllist:
    href=links.find("<img")
    if href!=-1:
        print("https://olympus.realpython.org"+links[links.find('"')+1:links.rfind('"')])
      

        
        



