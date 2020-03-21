import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
	browser.get(link)
	time.sleep(30)
	#True, если будет любое значение у метода *.find_element(), кроме None
	assert browser.find_element(By.XPATH, '//form[@id="add_to_basket_form"]/button'), \
	'There is no "Add to basket" button on the page'