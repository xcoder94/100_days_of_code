from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

product_url = 'http://orteil.dashnet.org/experiments/cookie/'
# service = Service(executable_path='/home/xon/Documents/100_days_of_code/48_day_selenium/chromedirver/chromedriver')
# Keep Chrome open after program finishes
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(product_url)

cookie = driver.find_element(By.ID, 'cookie')


t_end = time.time() + 10
while time.time() < t_end:
    check_time = time.time() + 5
    while time.time() <= check_time:
        cookie.click()
    upgrades = driver.find_elements(By.CSS_SELECTOR, '#store div')
    upgrades.pop()
    reversed_prices = list(reversed(upgrades))
    money = int(driver.find_element(By.ID, 'money').text)
    for i in reversed_prices:
        if i.get_attribute('class') == 'amount':
            pass
        else:
            upgrade_price = i.find_element(By.CSS_SELECTOR, 'b')
            price_text = upgrade_price.text.split()[-1]
            print(upgrade_price.text)
            if ',' in price_text:
                price_text = price_text.replace(',', '')

            if int(price_text) <= money:
                element_id = i.get_attribute('id')
                driver.find_element(By.ID, f"{element_id}").click()
            else:
                pass
    upgrades = []
    reversed_prices = []

driver.close()  # Closes only tab
# driver.quit()   # Closes browser
