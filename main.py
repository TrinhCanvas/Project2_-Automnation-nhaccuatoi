import random
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

driver.get("https://www.nhaccuatui.com/")

wait = WebDriverWait(driver, 15)

user = ''


def tinh_tong(a, b):
	return a + b


def DangkyTK():
	# Click vào nút đăng ký trên giao diện
	wait = WebDriverWait(driver, 15)
	element1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@title='Đăng ký']")))
	driver.find_element()
	element1.click()
	time.sleep(3)

	# Bắt đầu hoàn thành thông tin đăng ký
	#######Ten đăng nhập
	element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=('ifRegisterQuick')]")))
	driver.switch_to.frame(element2)
	# element2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
	element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='username']")))

	global user
	for idx in range(8):
		x = random.choices(string.ascii_lowercase)
		user += x[0]
	element2.send_keys(user)
	time.sleep(2)

	########Mật khẩu
	element3 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@name='password']")))
	element3.send_keys("lovisong")
	time.sleep(2)
	# xác nhận mật khẩu
	element4 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='password_comfirm']")))
	element4.click()
	element4.send_keys("lovisong")
	time.sleep(2)

	######## Email
	element5 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[(@id='email')]")))
	user1 = ''
	y = "@gmail.com"
	for idx in range(8):
		x = random.choices(string.ascii_lowercase)
		user1 += x[0]
	gmail = user1 + y
	element5.send_keys(gmail)
	time.sleep(3)

	#######Tôi không phải người máy
	wait = WebDriverWait(driver, 15)
	element6 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@title='reCAPTCHA']")))
	driver.switch_to.frame(element6)
	element61 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='recaptcha-anchor']/div[1]")))
	element61.click()


def DangNhap():
	wait = WebDriverWait(driver, 15)
	element1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnShowBoxLogin']")))
	element1.click()
	time.sleep(3)
	# Nhập username và passwword
	# element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=('ifRegisterQuick')]")))
	# driver.switch_to.frame(element2)
	element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='uname']")))
	element2.send_keys("hoathuytinh1999")

	element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
	element2.send_keys("12345678")
	time.sleep(3)
	# click vào nút đăng nhập
	element3 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='btn btn_login_submit']")))
	element3.click()
	time.sleep(3)


# Chọn 1 bài hát thể loại nhạc trẻ ở mục bài hát


def NgheNhac():
	# Chọn 1 bài hát thể loại nhạc trẻ ở mục bài hát
	element4 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='menuTop']/li[3]")))
	element4.click()
	time.sleep(5)
	# chọn 1 bài hát để bắt đầu nghe
	element5 = wait.until(EC.presence_of_element_located(
		(By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div/ul/li[1]/div/div[3]/a[1]")))
	element5.click()
	time.sleep(2)
	element6 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='autoplayLabelnctPlayer']")))
	element6.click()
	time.sleep(5)


# Chọn vào mục Tuyển Tập -> Buồn -> bật 1 bài nhạc
# 	ac =ActionChains(driver)
# 	Move1 = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@title='Tuyển Tập']")))
# 	Move2 = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='menuTop']/li[5]/ul/li[2]/ul/li[2]/a")))
# 	ac.move_to_element(Move1).move_to_element(Move2).click()
# 	ac.perform()
# 	time.sleep(3)
# 	EMusic = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='list_album tag']/ul/li[3]")))
# 	EMusic.click()

# Click vào mục bài hát xong thì chuyển chuyển sang tab mới và mở 1 bài sau đó tắt và trở về mở 1 bài mới

def Clicktotab():
	"""
	Hàm mở thêm 1 tab
	:return: 1 tab gg- khi click vào 1 đối tượng sẽ mở link ra tab mới
	"""
	wait = WebDriverWait(driver, 15)
	element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='menuTop']/li[5]/a")))
	action = ActionChains(driver)

	action.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
	time.sleep(3)

	driver.switch_to.window(driver.window_handles[1])
	element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='list_album tag']/ul/li[12]")))
	element2.click()
	# Tua đến vị trí của bài hát
	# 	element3 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='timeSliderHolderflashPlayer']")))
	element3 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='timeSliderflashPlayer']")))
	action.drag_and_drop_by_offset(element3, 200, 100)
	element3.click()
	time.sleep(10)
	driver.close()


def Dangxuat():
	ac = ActionChains(driver)
	move_1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".userprofile-card-item")))
	move_2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user_control > ul > li:nth-child(5) > a")))
	ac.move_to_element(move_1).move_to_element(move_2).click()
	ac.perform()


if __name__ == '__main__':
	# DangNhap()
	# NgheNhac()
	# Dangxuat()
	# time.sleep(10)
	Clicktotab()
	# Dangxuat()
	time.sleep(3)
# driver.quit()
