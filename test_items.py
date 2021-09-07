import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_eng_add_button_should_be_seen(browser,language1):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(1) 
    l=browser.find_element(By.CSS_SELECTOR, "[value={}]".format(str(language1)))#выбор языка
    l.click()
    time.sleep(3)
    button=browser.find_element_by_css_selector("button.btn.btn-default")#смена языка на сайте
    button.click()
    time.sleep(10)
    add_button = browser.find_element_by_class_name(".btn-add-to-basket").is_enabled()

    assert add_button, "Отсутствует кнопка добавления товара в корзину"
    
