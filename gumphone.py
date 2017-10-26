
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from xlsxlib import Excel
import time
import re
import os
from xlsxlib import Excel

class Gumscp():

	def __init__(self):
		# Launch PhantomJS or Chromium
		self.driver = webdriver.PhantomJS("path_to_chromium or path_to_phantom_JS")

		return

	def get_code(self, link):

		self.driver.get(link)

		html = self.driver.page_source

		soup = BeautifulSoup(html) #specify parser or it will auto-select for you

		return soup

	def quit(self):
		self.driver.quit()	
		return	

	def get_all_ads_per_page(self, soup):
		print ("Let's scrape!")
		link_list = []
		url_match = re.compile(r'https://www.gumtree.com/p/(.*)')

		for a in soup.find_all('a', href=True):
			url = a['href']
			url = 'https://www.gumtree.com' + url
			if url_match.match(url):				
					link_list.append(url)

			link_list = list(set(link_list))

		link_list = sorted(link_list)
		print ("Number of links: "+ str(len(link_list)))
		#print(link_list)

		return link_list	

	def reveal_and_scrape(self, link):

		self.driver.get(link)
		# Reveal the phone number
		self.driver.find_element_by_link_text('Reveal').click()
		# Waiting 1 sec for the phone to reveal
		time.sleep(1)
		# Get the phone number
		x = self.driver.find_element_by_class_name('grid-container')

		# Chopping the text to get the phone number and the name
		head, sep, tail = x.text.partition('Contact details')
		head2, sep2, tail2 = tail.partition('Reveal')
		phone = head2.strip()

		head3, sep3,tail3 = head.partition('Full screen gallery')
		head4, sep4, tail4 = tail3.partition('Posting')
		name = head4.strip()
		#phone = self.driver.find_element_by_class_name("space-mvxs").text

		return name, phone

	def scrape(self, link, page_number):

		l_name = []
		l_phone = []
		print('Scraping... '+str(link)+str(page_number)+'?seller_type=private')
		soup = self.get_code(link+str(page_number)+'?seller_type=private')
		link_list = self.get_all_ads_per_page(soup)

		for linkd in link_list:
			try:
				name, phone = self.reveal_and_scrape(linkd)
				print(name)
				print(phone)
				l_name.append(name)
				l_phone.append(phone)
			except:
				pass

		p_list = {'name':l_name, 'phone':l_phone}
		return p_list

	def scrape_l(self, link, number_of_page):

		l_name = []
		l_phone = []

		for i in range(1, number_of_page+1):

			soup = self.get_code(link+str(i))
			link_list = self.get_all_ads_per_page(soup)

			for linkd in link_list:
				try:
					name, phone = self.reveal_and_scrape(linkd)
					print(name)
					print(phone)
					l_name.append(name)
					l_phone.append(phone)
				except:
					pass

		p_list = {'name':l_name, 'phone':l_phone}
		return p_list

	def result(self, p_list):
		
		print('Printing')
		result = Excel()
		result.open_workbook('result')
		row_to_write = 1

		for i in range(0, len(p_list['name'])):
			result.write_cell(row_to_write, 1, p_list['name'][i])
			result.write_cell(row_to_write, 2, p_list['phone'][i])
			row_to_write = row_to_write+1

		result.save_workbook()
		return

