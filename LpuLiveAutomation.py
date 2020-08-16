'''
1. Go the https://lpulive.lpu.in/login [Done]
2. Login with UMS ID and Password [Done]
3. click on the 1st group [Done]
4. Find the span element with the word Today [Done]
5. Download files and images if any [Done]
6. Create a folder name with same name as group name 
7. And Paste those files in respective folders
8. Switch to the next Group [Done]
9. Perform same task
10. Happy Coding !
'''
from time import sleep
import os
import rename

try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from selenium.webdriver.chrome.options import Options
	print('Pass: Requirement Satisfied')
except Exception as e:
	print("Fail: Something Occurred")
	sleep(5)
	quit()

#Enter Day
print("Enter day in format:")
print("1. For single day (eg, Today)")
print("2. For multiple days (eg, Today Thursday, space seperated)\n")
dayList = input("Provide Day/Days : ").split()

try:
	options = Options()
	curDir = os.getcwd()
	downloadDir = "Downloads"
	if os.path.exists(downloadDir)==False:
		os.mkdir(downloadDir)
	options.add_argument("--disable-notifications")
	options.add_experimental_option("prefs", {"download.default_directory": str(curDir)+"\\"+downloadDir})
	driver = webdriver.Chrome('./chromedriver', options=options)
	# driver.maximize_window()
	driver.get('https://lpulive.lpu.in/login')
	print('Pass: Browser Opened')
except Exception as e:
	print("Fail: Chrome Driver Error")
	sleep(5)
	quit()

def login():
	try:
		user_field = driver.find_element_by_xpath('//*[@id="inputEmail"]')
		user_field.send_keys('11903306')
		pass_field = driver.find_element_by_xpath('//*[@id="inputPassword"]')
		pass_field.send_keys('9419Roshank@')
		pass_field.send_keys(Keys.RETURN)
		print('Pass: Login Successfull')
	except Exception as e:
		print('Fail: Login Failed')
		sleep(5)
		driver.quit()
		quit()

gName = "Other"
def downloadMaterials(path):
	dwnBtnPath = '/html/body/app-root/app-layout/div/div/div/div[2]/app-chat/app-gallery-carousel/div/div[1]/div[2]/a'
	closeBtnPath = '/html/body/app-root/app-layout/div/div/div/div[2]/app-chat/app-gallery-carousel/div/div[1]/div[2]/span'
	
	print(gName)
	for i in range(2, 100):
		textpath = path + '/div['+str(i)+']'
		try:
			linkPath = textpath + '/div/div/div[2]/div[1]/div/a'
			link = driver.find_element_by_xpath(linkPath)
			link.click()
			print("Link Found")
			sleep(0.5)
			continue
		except Exception as e:
			a = 0
		try:
			imgPath = textpath + '/div/div/div[2]/div[1]/div[1]/div/img'
			images = driver.find_element_by_xpath(imgPath)
			print('Image Found')
			images.click()
			sleep(0.5)
			try:
				WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, dwnBtnPath))).click()
				sleep(0.5)
				driver.find_element_by_xpath(closeBtnPath).click()
				continue
			except Exception as e:
				print('Fail: Image Error', e)
				continue
		except Exception as e:
			print("Simple Text")
		try:
			text = driver.find_element_by_xpath(textpath)
		except Exception as e:
			print("Download Completed")
			sleep(2)
			rename.renameFiles(gName)
			return


def searchForMaterials():
	global dayList
	chatWindowPath = '//*[@id="chat-window"]/div['
	flag=0
	sleep(1)
	for i in range(1, 10):
		try:
			path = chatWindowPath+str(i)+']'
			dayChat = driver.find_element_by_xpath(path)
			flag = 1
		except Exception as e:
			# print(e)
			print("Chat Completed")
			if(flag):
				return
			else:
				raise e
		dayTag = driver.find_element_by_xpath(chatWindowPath+str(i)+']'+'/div[1]/span')
		print('Found', i)
		txt = dayTag.text
		if(txt in dayList):
			print('Pass: Material Found')
			downloadMaterials(path)
		# sleep(0.1)
	print("Nothing Found\n")




def switchGroup():
	global gName
	os.chdir("Downloads")
	try:
		WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cookie_consent"]/button'))).click()
		print('Cookie Closed')
	except Exception as e:
		print('Cookie Not Found')
	try:
		group = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-layout/div/div/div[1]/div[1]/app-sidebar/div[1]/div[2]/div[1]')))
		group.click()
	except Exception as e:
		print('Fail: Unable to Switch Group')
		sleep(5)
		driver.quit()
		quit()
	maxGroup = 20
	for i in range(1, maxGroup+1):
		gPath = '/html/body/app-root/app-layout/div/div/div/div[1]/app-sidebar/div[1]/div[2]/div['+str(i)+']'
		try:
			group = driver.find_element_by_xpath(gPath)
			gName = driver.find_element_by_xpath(gPath+'/div/div[1]/div/p').text
			group.click()
			print("\nGroup Found", gName)
			searchForMaterials()
		except Exception as e:
			print(e)
			print("Maximum Group Reached")
			return
		sleep(0.2)
	print('Pass: All Groups Checked')



login()
switchGroup()

print("Pass: Successfully Executed")

sleep(5)
driver.quit()