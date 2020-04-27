import requests
# from BeautifulSoup import BeautifulSoup4
from bs4 import BeautifulSoup
import pandas as pd

urls=[]

result=requests.get("https://www.whitehouse.gov/briefings-statements/")

print(result.status_code)

print(result.headers)

src=result.content

soup=BeautifulSoup(src)

links=soup.find_all("a")
# print(links)
for h2_tags in soup.find_all("h2"):
    atag=h2_tags.find("a")
    print (atag)
    urls.append(atag.attrs['href'])
#print (urls)
tag=soup.b
for link in soup.find_all('a'):
    print(link.get('href'))
    print(tag.attrs)

