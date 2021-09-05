import time
def test_eng_should_see_add_button(browser): # В фикстуру передаём аргумент browser из нашего conftest
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30) # Ставим паузу в 30 сек как и сказано в задании


    add_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket").is_enabled()
    # Ищем уникальный селектор для кнопки

    assert add_button, "button is missing" # проверяем что кнопка присутствует на странице