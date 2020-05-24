from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import requests
import time
import os

dir = os.path.dirname(__file__)
chrome_driver_path = dir + "/chromedriver"


driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

keyword     = 'Thor'
size        = 'Large' # Large, Medium, or Small (Case Sensitive)

driver.get("https://duckduckgo.com/?q=" + keyword + "&iax=images&ia=images&t=h_&iaf=size%3A" + size)


time.sleep(2)
driver.find_element_by_class_name('tile.tile--img.has-detail').click()
time.sleep(2)

url = driver.find_element_by_class_name('detail__media__img-highres.js-detail-img.js-detail-img-high')

print(url.get_attribute('src'))

myfile = requests.get(url.get_attribute('src'))
open('images/'+ keyword +'.png', 'wb').write(myfile.content)

driver.quit()
