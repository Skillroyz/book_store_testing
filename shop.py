import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Shop: отображение страницы товара
# account = driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("sorvanec88@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gn84rYo99")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# html5 = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product/html5-forms/']").click()
# html5_text = driver.find_element_by_css_selector(".product_title.entry-title")
# html5_text = html5_text.text
# assert html5_text == "HTML5 Forms"
# if html5_text == html5_text:
#     print("Текст совпадает:", html5_text)
# else:
#     print("Фактический текст:", html5_text)

# Shop: количество товаров в категории
# account = driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("sorvanec88@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gn84rYo99")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# html = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']").click()
# items_count = driver.find_elements_by_css_selector("a > h3")
# if len(items_count) == 3:
#     print("В категории 3 товара")
# else:
#     print("Ошибка. Количество товаров в категории: " + str(len(items_count)))


# Shop: сортировка товаров
# account = driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("sorvanec88@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gn84rYo99")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# selector_items = driver.find_element_by_name("orderby")
# selector_items_default= selector_items.get_attribute("value")
# if selector_items_default == "menu_order":
#     print("Выбрана сортировка по умолчанию")
# else:
#     print("Выбрана сортировка НЕ по умолчанию")
# selector_items = Select(selector_items)
# selector_items.select_by_value("price-desc")
# selector_items = driver.find_element_by_name("orderby")
# selector_items_high = selector_items.get_attribute("value")
# if selector_items_high == "price-desc":
#     print("Выбрана сортировка от большей к меньшей")
# else:
#     print("Выбрана другая сортировка")
# driver.quit()

# Shop: отображение, скидка товара
# account = driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("sorvanec88@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gn84rYo99")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# android_quick_start_book = driver.find_element_by_css_selector(".post-169").click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images"))).click()
# book_cover_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()
# driver.quit()

# Shop: проверка цены в корзине
# account = driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("sorvanec88@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gn84rYo99")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# book_html5 = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# basket_item_value = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
# basket_item_value_text = basket_item_value.text
# assert basket_item_value_text == "1 Item"
# basket_price_value = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# basket_price_value_text = basket_price_value.text
# assert basket_price_value_text == "₹180.00"
# basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
# basket_btn.click()
# items_shop = driver.find_element_by_css_selector("[class='cartcontents']").click()
# subtotal_price = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
# total_price = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))
# # driver.quit()

# Shop: работа в корзине
# shop = driver.find_element_by_id("menu-item-40").click()
# book_html5 = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_js_data = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
# time.sleep(1)
# items_shop = driver.find_element_by_css_selector("[class='cartcontents']").click()
# time.sleep(1)
# remove = driver.find_element_by_class_name("remove").click()
# undo_btn = driver.find_element_by_link_text("Undo?").click()
# quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
# quantity_field.clear()
# quantity_field.send_keys("3")
# update_basket = driver.find_element_by_name("update_cart")
# update_basket.click()
# quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
# quantity_field_value = quantity_field.get_attribute("value")
# assert quantity_field_value == '3'
# time.sleep(5)
# apply_coupon = driver.find_element_by_name("apply_coupon")
# apply_coupon.click()
# error_message = driver.find_element_by_css_selector(".woocommerce-error")
# error_message_text = error_message.text
# assert error_message_text == 'Please enter a coupon code.'
# driver.quit()

# Shop: покупка товара
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
html5_webapp_development_book.click()
# Переход в корзину
basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()
checkout_btn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
# Заполнение обязательных полей
first_name = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Donald")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Trump")
email = driver.find_element_by_id("billing_email")
email.send_keys("test@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("88005553535")
country = driver.find_element_by_id("s2id_billing_country")
country.click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Christmas Island")
country_second_field = driver.find_element_by_class_name("select2-match")
country_second_field.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("The Wall")
city = driver.find_element_by_id("billing_city")
city.send_keys("Winterfell")
state = driver.find_element_by_id("billing_state")
state.send_keys("North")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("100200300")
driver.execute_script("window.scrollBy(0, 600);")
# Выбор способа оплаты: чек
time.sleep(5)
payment_check = driver.find_element_by_id("payment_method_cheque")
payment_check.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
# Проверка что появилось сообщение об успешном заказе
success_message = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
"Thank you. Your order has been received."))
# Проверка что выбран платёжный способ: чек
payment_method_message = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))

driver.quit()