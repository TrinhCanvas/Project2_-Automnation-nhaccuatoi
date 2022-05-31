import string
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By




class Base:
	def __init__(self):
		options = Options()
		options.add_argument('--start-maximized')
		self.driver = webdriver.Chrome(options=options)

	# self.time_wait = 15

	def go_page(self, url):
		self.driver.get(url)

	def get_element(self, action):
		"""
		Hàm lấy elemnt
		:param action: String - Check lấy element theo kiểu nào
		:return:
		"""
		if action == "wait":
			wait = WebDriverWait(self.driver, 15)
			element = wait.until(EC.presence_of_element_located())
		else:
			self.driver.find_element()

	def click_element(self, element):
		element.click()

	def sendkeys_element(self, element):
		element.send_keys()


class Web(Base):
	def __init__(self):
		super(Web, self).__init__()

	def go_page(self, url):
		self.driver.get(url)

	def get_element(self, action):
		"""
		Hàm lấy elemnt
		:param action: String - Check lấy element theo kiểu nào
		:return:
		"""
		if action == "wait":
			wait = WebDriverWait(self.driver, 15)
			element = wait.until(EC.presence_of_element_located())
		else:
			self.driver.find_element()

	def click_element(self, element):
		element.click()

	def sendkeys_element(self, element):
		element.send_keys()

user = ''
	def TenTaiKhoan(self):
		global user
		wait = WebDriverWait(driver, 15)
		element4 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='username']")))
		element4.click()

		for idx in range(8):
			x = random.choices(string.ascii_lowercase)
			user += x[0]
		element4.send_keys(user)


