from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"

html=requests.get(url).content

soup =BeautifulSoup(html,"html.parser")

products=[]              
prices=[]               


for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'}).text
        price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'}).text
     
       
        products.append(names)
        prices.append(price)
        
file_name="ass.csv"        
df=pd.DataFrame({'Product Name':products,'Price':prices})
df.head(10)
df.to_csv(file_name)