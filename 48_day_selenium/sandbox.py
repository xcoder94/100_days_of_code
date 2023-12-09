from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

python_site_url = 'https://www.python.org'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(python_site_url)

# Amazon Html tree is changed this way is wrong this time
# product_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# product_cents = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
# print(f'{product_dollar.text},{product_cents.text}')

# This is finding by ID and find this product price methods
# element_with_id = driver.find_element(By.ID, 'corePrice_desktop')
# price = element_with_id.find_element(By.CLASS_NAME, 'a-price').text
# print(float(price.replace('$', '')))

# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.get_attribute('placeholder'))
# button = driver.find_element(By.ID, 'submit')
# print(button.size)

# doc_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Challenge my code
# main_list = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# list_elements = main_list.find_elements(By.TAG_NAME, 'li')
# events_dict = {}
# for i in list_elements:
#     time = i.find_element(By.TAG_NAME, 'time')
#     time2 = time.get_attribute('datetime')
#     name = i.find_element(By.TAG_NAME, 'a')
#     values_dict = {
#         'time': f'{time2[0:10]}',
#         'name': f'{name.text}'
#     }
#     events_dict[list_elements.index(i)] = values_dict
#
# print(events_dict)

# Challenge Angela's code
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }

print(events)

driver.close()  # Closes only tab
# driver.quit()   # Closes browser
