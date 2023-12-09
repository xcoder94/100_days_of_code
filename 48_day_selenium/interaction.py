from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://en.wikipedia.org/wiki/Main_Page'
test_url = 'http://secure-retreat-92358.herokuapp.com/'

# driver_path = '/home/xon/Documents/100_days_of_code/48_day_selenium/chromedirver/chromedriver'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(test_url)

# articles_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(articles_count.text)

driver.find_element(By.NAME, 'fName').send_keys('Test')
driver.find_element(By.NAME, 'lName').send_keys('Test')
driver.find_element(By.NAME, 'email').send_keys('Test@test.ru')

sign_up_button = driver.find_element(By.CLASS_NAME, 'btn')
sign_up_button.click()

# driver.close()
