from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

know_smallest_price = 999999999999999999999999
kwon_smallest_button = None

driver.get("https://www.price.com.hk/product.php?p=518770")
quotations = driver.find_elements(By.CSS_SELECTOR, '.page-product > ul > li[id]')
for quotation in quotations
    price_elem = quotation.find_element(By.CSS_SELECTOR, '.text-price-number')
    price = float(price_elem..get_attribute('.data-price'))

    quotation_elem = .quotation.find_element(By.CSS_SELECTOR, '.new-referral_btn')

    if price < know_smallest_price
            know_smallest_price = price
            know_smallest_btn = quotation_elem

    know_smallest_btn.click()


driver.find_element(By.CSS_SELECTOR, .fx).get_attribute('.data-price')

elem.send_keys("魚")
elem.send_keys(Keys.ENTER)

import time
time.sleep(5)


all_products = []

while True:
    product_brief_list = driver.find_element(By.CSS_SELECTOR, '.product-brief-list')

    for product_brief in product_brief_list.find_elements(By.CSS_SELECTOR, '.product-brief-wrapper'):
        title = product_brief.find_element(By.CSS_SELECTOR, '.brand-product-name>h4').text
        price = product_brief.find_element(By.CSS_SELECTOR, '.price').text
        all_products.append([title, price])

    next_btn = driver.find_element(By.CSS_SELECTOR, "#paginationMenu_nextBtn")

    if next_btn.get_attribute("class") == "disabled":
        break

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    next_btn.click()

    time.sleep(5)

print("done")