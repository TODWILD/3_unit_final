def test_eng_add_button_should_be_seen(browser):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    add_button = browser.find_element_by_class_name(".btn-add-to-basket").is_enabled()

    assert add_button, "Отсутствует кнопка добавления товара в корзину"
    
