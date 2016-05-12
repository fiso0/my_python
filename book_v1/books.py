book_urls=["http://product.dangdang.com/23203528.html",#哲学的故事 33.6
           "http://product.dangdang.com/22634348.html",#Head First Python 34
           "http://product.dangdang.com/23611453.html"]#大问题：简明哲学导论 39

import requests
from bs4 import BeautifulSoup
import re


def parseBook(url,book):
	'''解析当当商品页面内的标题（书名）和价格'''
	response=requests.get(url).text
	soup = BeautifulSoup(response, "lxml")

	title=soup.select_one('.name_info > h1').get('title')

	price_str=soup.select_one('.price_qiang .price_d').getText()
	pattern=re.compile("\d+\.?\d*")
	price=pattern.search(price_str).group(0)

	book.append({'title':title,'price':price})

book=[]
for url in book_urls:
	parseBook(url,book)
print(book)

