from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Registration_login: регистрация аккаунта
# account = driver.find_element_by_id("menu-item-50").click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("sorvanec88@gmail.com")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Gn84rYo99")
# register = driver.find_element_by_css_selector("[name='register']").click()

# Registration_login: логин в систему
account = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("sorvanec88@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Gn84rYo99")
login = driver.find_element_by_css_selector("[name='login']").click()
logout_text = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout>a")
logout_text = logout_text.text
assert logout_text == "Logout"

driver.quit()