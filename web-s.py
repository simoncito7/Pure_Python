#CoDIGO 1 - NO FUNCIONo

# from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
# import pandas as pd
# import sys
# import urllib.request

# datos = urllib.request.urlopen(‘https://www.openwebinars.net’).read().decode()


# !{sys.executable} -m pip install beayutifulsoup4

# from bs4 import BeautifulSoup
# soup =  BeautifulSoup(datos)
# tags = soup(‘a’)
# for tag in tags:
# 	print(tag.get(‘href’))



#CoDIGO 2 - NO FUNCIONo

# from scrapy.item import Field
# from scrapy.item import Item
# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from scrapy.contrib.loader import ItemLoader


# class Pregunta(Item):
# 	pregunta = Field()
# 	id = Field()

# class StackOver(Spider):
# 	name = "MiPrimerSpider"
# 	start_urls = ['https://stackoverflow.com/']
# 	def parse(self,response):
# 		sel = Selector(response)
# 		preguntas = sel.xpath('//div[@id = "question-mini-list"]/div')

# 		# iterar sobre todas las preguntas
# 		for i,elem in enumerate(preguntas):
# 			item = ItemLoader(Pregunta(),elem)
# 			item.add_xpath('pregunta', './/h3/a/text()')
# 			item.add_value('id',i)
# 			yield item.load_item()


#CoDIGO 3 - NO FUNCIONo

# from scrapy.item import Field
# from scrapy.item import Item
# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from scrapy.loader import ItemLoader

# class Pregunta(Item):
#     pregunta = Field()
#     id = Field()

# class StackOverflowSpider(Spider):
#     name = "MiPrimerSpider"
#     start_urls = ['http://stackoverflow.com/questions']
#     def parse(self, response):
#         sel = Selector(response)
#         preguntas = sel.xpath('//div[@id="questions"]/div') 
       
#         #Iterar sobre todas las preguntas
#         for i, elem in enumerate(preguntas):
#             item = ItemLoader(Pregunta(), elem)
#             item.add_xpath('pregunta', './/h3/a/text()')
#             item.add_value('id', i)

#             yield item.load_item()

# from scrapy.item import Field
# from scrapy.item import Item
# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from scrapy.loader import ItemLoader

# class Pregunta(Item):
#     pregunta = Field()
#     id = Field()

# class StackOverflowSpider(Spider):
#     name = "MiPrimerSpider"
#     start_urls = ['http://stackoverflow.com/']
#     def parse(self, response):
#         sel = Selector(response)
#         preguntas = sel.xpath('//div[@id="question-mini-list"]/div') 
#         for i, elem in enumerate(preguntas):
#             item = ItemLoader(Pregunta(), elem)
#             item.add_xpath('pregunta', './/h3/a/text()')
#             item.add_value('id', i)
#             yield item.load_item()


# CoDIGO'4 - USANDO LIBRERÍA BEAUTIFULSOUP

import urllib.request
datos = urllib.request.urlopen('http://www.openwebinars.net').read().decode()

import sys
!{sys.executable} -m pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup(datos)
tags = soup('a')
for tag in tags:
	print(tag.get('href'))


