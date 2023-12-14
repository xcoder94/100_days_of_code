from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

linked_in = 'https://www.linkedin.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(linked_in)
time.sleep(1)
driver.find_element(By.NAME, 'session_key').send_keys('o7451155@yandex.com')
driver.find_element(By.NAME, 'session_password').send_keys('Zxcvbnm7451155')
# driver.find_element(By.NAME, 'email').send_keys('Test@test.ru')

sign_up_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
sign_up_button.click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a').click()
time.sleep(2)
search_input = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
search_input.send_keys('Python developer')
search_input.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH, '//button[normalize-space()="Все фильтры"]').click()
driver.implicitly_wait(1)
element = driver.find_element(By.CSS_SELECTOR, 'input.input.artdeco-toggle__button')
# driver.execute_script('arguments[0].click();', element)
# driver.find_element(By.CSS_SELECTOR, 'div.search-reusables__filters-bar-grouping full-width div div button').click()

# driver.close()
