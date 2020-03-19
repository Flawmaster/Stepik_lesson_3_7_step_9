import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	#добавляем опцию language
	parser.addoption('--language', \
		action = 'store', \
		default = None, \
		help = 'Choose language: ru, en, ... (etc.)')

@pytest.fixture(scope='function')
def browser(request):
	language = request.config.getoption('language')
	#если language не равен None, то передаем опцию в браузер
	if language:
		options = Options()
		options.add_experimental_option('prefs', \
			{'intl.accept_languages': language})
		print('\n\nStarting Chrome browser for test')
		browser = webdriver.Chrome(options=options)
	#если language равен None(не был введен) - выдаем ошибку
	else:
		raise pytest.UsageError('Language must not be blank!')
	yield browser
	print('\nQuit browser')
	browser.quit()