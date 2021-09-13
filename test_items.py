from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_displayed_basket_btn(browser):
    browser[0].get(link)
    assert browser[0].find_elements_by_css_selector(
           '#add_to_basket_form .btn-add-to-basket'), (
           f'Basket button is not found on page {link} '
           f'for language "{browser[1]}"')
    sleep(3)
    
