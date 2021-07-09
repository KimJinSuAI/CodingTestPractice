from bs4 import BeautifulSoup
import requests 
import json 
import pandas as pd # 국내 ETF 전체 리스트 
url = 'https://finance.naver.com/sise/sise_market_sum.nhn' 
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"html.parser")
for tag in soup.select("div[class=box_type_l] > table[class=type_2] tr td a[class=tltle]"):
    response2 = requests.get("https://finance.naver.com/item/main.nhn?"+tag["href"][-6:])
    html2 = response2.text
    soup2 = BeautifulSoup(html2,"html.parser")
    # print(tag.text + str(tag))
    print(soup2.select("body > div[id=wrap] > div[class=new_totalinfo]"))       #동적크롤링..
    



# json_data = json.loads(a) 
# df_etf_list = pd.json_normalize(json_data['result']['etfItemList'])
# print(a.text)