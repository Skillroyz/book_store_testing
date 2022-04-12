from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

driver.execute_script("window.scrollBy(0, 600);")
ruby = driver.find_element_by_css_selector("[title='Selenium Ruby']").click()
reviews = driver.find_element_by_css_selector("[href='#tab-reviews']").click()
rating = driver.find_element_by_css_selector("[class='stars']>span a:nth-child(5)").click()
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Test")
email = driver.find_element_by_id("email")
email.send_keys("test@gmail.com")
submit = driver.find_element_by_id("submit").click()

driver.quit()