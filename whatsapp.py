import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep

class TestingWhatsappWeb(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:/Users/Esteban Henao/Downloads/chromedriver.exe')
		driver = self.driver
		driver.get('https://web.whatsapp.com/')
		driver.maximize_window()

	def test_talk(self):
		driver = self.driver

		WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))

		search_field = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
		search_field.click()
		search_field.clear
		search_field.send_keys('3206098483')
		sleep(1)

		select_contact = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[2]')
		select_contact.click()
		sleep(1)

		WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')))
		text_field = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
		text_field.click()
		text_field.clear
		text_field.send_keys('Hola, esta es una prueba automatizada de un bot chateando por medio de WhatsApp Web')
		sleep(2)

		enter_button = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]')
		enter_button.click()
		sleep(2)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()