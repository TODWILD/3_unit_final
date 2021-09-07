def test_eng_add_button_should_be_seen(browser):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(1) 
    a1=browser.find_element(By.CSS_SELECTOR, "[value={}]".format(str(language1)))#выбор языка
    a1.click()
    time.sleep(3)
    but=browser.find_element_by_css_selector("button.btn.btn-default")#смена языка на сайте
    but.click()
    time.sleep(10)
    add_button = browser.find_element_by_class_name(".btn-add-to-basket").is_enabled()

    assert add_button, "Отсутствует кнопка добавления товара в корзину"
    
