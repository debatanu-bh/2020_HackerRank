from selenium import webdriver
# from BeautifulSoup import BeautifulSoup4
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"C:\Users\debatanu\PycharmProjects\2020\driver\chromedriver")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
# driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

driver.get("https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_9_na_na_na&as-pos=0&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=6c2ee700-3d2c-4edc-a925-de7163f35d61&as-searchtext=redminote")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
    df = pd.DataFrame ( {'Product Name': products, 'Price': prices,'RATING':ratings} )
    df.to_csv ( 'MobileProducts.csv', index=False, encoding='utf-8' )
