# Ubicando por ID
# Use this when you know id attribute of an element.
# ---------------- ESTE PROGRAMA, USANDO FIREFOX, NAVEGA AL BUSCADOR DE GOOGLE Y BUSCA LA PALABRA "TECHBEAMERS"-----------------------


from selenium import webdriver  						# importación de módulo webdriver de Selenium
import time												# importa la librería time
from selenium.webdriver.common.keys import Keys 		# importa el módulo Keys de selenium.webdriver.common.keys

driver = webdriver.Chrome(executable_path="./chromedriver.exe")							# Creación del driver de chrome()
driver.get("http://google.com")							# Navega a la página google.com			
driver.maximize_window()								# Este método permite maximizar ventana
time.sleep(5)											# "duerme" la ejecución del programa
inputElement = driver.find_element_by_name("q")			# 
inputElement.send_keys("Techbeamers")					# Ingresa "Techbeamers" en el buscador
inputElement.submit()									# Envía la petición (equivale a decir que hace clic en "buscar")

time.sleep(5)
# elem = driver.find_element_by_link_text("Python Tutorial")
elem = driver.find_element_by_partial_link_text("Python")
elem.click()
# time.sleep(20)

# driver.close()											# cierra el driver


# /html/body/div[7]/div[3]/div[8]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]


# import time
# from selenium import webdriver						# selenium.webdriver module provides all the WebDriver implementations.
# from selenium.webdriver.common.keys import Keys 	# The Keys class provides keys in the keyboard like RETURN, F1, ALT, etc.
# from selenium.webdriver.common.by import By 
# driver = webdriver.Firefox()						# Instance of Firefox webdriver is created

# driver.get("https://docs.python.org/3/howto/regex.html") 				# the driver.get() method will navigate to a page given by the URL.
# time.sleep(10)

# # assert "PSF" in driver.title

# a = driver.find_element(By.CLASS_NAME, 'CLASS_NAME= "related"')

# driver.find_elements(By.XPATH, 'CLASS_NAME')

# # WebDriver offers a number of ways to find elements using one of the "find_elements_by_*" methods

# elem = driver.find_elements_by_name("Python")			# este método permite buscar un elemento por su nombre

# #luego enviamos "keys" (letras). Es similar a ingresar letras por teclado.

# elem.clear()		# antes de cargar, se limpia la variable elem mediante el método clear()
# elem.send_keys("pycon")			# keys ingresadas
# elem.send_keys(Keys.RETURN)		# 

# assert "No results found." not in driver.page_source		# Para asegurar que algunos resultados son encontrados, hacer una aserción

# driver.close()


#--------------------------------------------------------------------------------------------------------------#


# import requests
# from bs4 import BeautifulSoup
 
# def count_words(url, the_word):
#     r = requests.get(url, allow_redirects=False)
#     soup = BeautifulSoup(r.content, 'lxml')
#     words = soup.find(text=lambda text: text and the_word in text)
#     print(words)
#     return len(words)
 
 
# def main():
#     url = 'https://python-forum.io/Thread-How-to-find-a-specific-word-in-a-webpage-and-How-to-count-it'
#     word = 'code'
#     count = count_words(url, word)
#     print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
 
# if __name__ == '__main__':
#     main()


# ---------------------------------------------------------------------------------------------------------------#


# import requests
# from bs4 import BeautifulSoup, SoupStrainer
# import re
# from collections import Counter

# pattern1 = re.compile(r"\bshall\b",re.IGNORECASE)
# pattern2 = re.compile(r"\bmust\b",re.IGNORECASE)


########################################Sections##########################
# def levelthree(item2_url):
#  r = requests.get(item2_url)
#  for sectionlinks in     BeautifulSoup((r.content),"html.parser",parse_only=SoupStrainer('a')):
#   if sectionlinks.has_attr('href'):
#    if 'section' in sectionlinks['href']:
#          href = "http://law.justia.com" + sectionlinks.get('href')
#          href = "\n" + str(href)
#          print (href)



########################################Chapters##########################
# def leveltwo(item_url):
#     r = requests.get(item_url)
#     for sublinks in BeautifulSoup((r.content), "html.parser", parse_only=SoupStrainer('a')):
#         if sublinks.has_attr('href'):
#             if 'chapt' in sublinks['href']:
#                 chapterlinks = "http://law.justia.com" + sublinks.get('href')
#                 chapterlinks = "\n" + str(chapterlinks)
#                 print (chapterlinks)


# ######################################Titles###############################
# def levelone(url):
#     r = requests.get(url)
#     for links in BeautifulSoup((r.content), "html.parser", parse_only=SoupStrainer('a')):
#         if links.has_attr('href'):
#             if 'title-43' in links['href']:
#                 titlelinks = "http://law.justia.com" + links.get('href')
#                 titlelinks = "\n" + str(titlelinks)
#                 leveltwo(titlelinks)
#                 print (titlelinks)


# ###########################################################################
# base_url = "http://law.justia.com/codes/georgia/2015/"
# levelone(base_url)



# import re
# import requests

# def wordOnTheWebFifa():
#     page = requests.get("https://twitter.com/explore").text
#     listita=re.findall("covid2019", page)


#     print(listita)

#     print(len(listita))

#     print(page.find("covid2019"))

# wordOnTheWebFifa()

# Python3 program for a word frequency 
# counter after crawling a web-page 
# import requests 
# from bs4 import BeautifulSoup 
# import operator 
# from collections import Counter 

# '''Function defining the web-crawler/core 
# spider, which will fetch information from 
# a given website, and push the contents to 
# the second function clean_wordlist()'''
# def start(url): 

# 	# empty list to store the contents of 
# 	# the website fetched from our web-crawler 
# 	wordlist = [] 
# 	source_code = requests.get(url).text 

# 	# BeautifulSoup object which will 
# 	# ping the requested url for data 
# 	soup = BeautifulSoup(source_code, 'html.parser') 

# 	# Text in given web-page is stored under 
# 	# the <div> tags with class <entry-content> 
# 	for each_text in soup.findAll('div', {'class':'entry-content'}): 
# 		content = each_text.text 

# 		# use split() to break the sentence into 
# 		# words and convert them into lowercase 
# 		words = content.lower().split() 
		
# 		for each_word in words: 
# 			wordlist.append(each_word) 
# 		clean_wordlist(wordlist) 

# # Function removes any unwanted symbols 
# def clean_wordlist(wordlist): 
	
# 	clean_list =[] 
# 	for word in wordlist: 
# 		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		
# 		for i in range (0, len(symbols)): 
# 			word = word.replace(symbols[i], '') 
			
# 		if len(word) > 0: 
# 			clean_list.append(word) 
# 	create_dictionary(clean_list) 

# # Creates a dictionary conatining each word's 
# # count and top_20 ocuuring words 
# def create_dictionary(clean_list): 
# 	word_count = {} 
	
# 	for word in clean_list: 
# 		if word in word_count: 
# 			word_count[word] += 1
# 		else: 
# 			word_count[word] = 1
			
# 	''' To get count of each word in 
# 		the crawled page --> 
		
# 	# operator.itemgetter() takes one 
# 	# parameter either 1(denotes keys) 
# 	# or 0 (denotes corresponding values) 
	
# 	for key, value in sorted(word_count.items(), 
# 					key = operator.itemgetter(1)): 
# 		print ("% s : % s " % (key, value)) 
		
# 	<-- '''

	
# 	c = Counter(word_count) 
	
# 	# returns the most occurring elements 
# 	top = c.most_common(10) 
# 	print(top) 

# # Driver code 
# if __name__ == '__main__': 
# 	start("https://www.geeksforgeeks.org/programming-language-choose/") 
