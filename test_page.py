from counter_page import CounterPage
from contact_page import ContactPage


def test_example(selenium):
 	selenium.get('http://localhost:3000')
 	assert selenium.title == 'Portal link'
 	assert selenium.current_url == 'http://localhost:3000/'
 	assert not selenium.find_elements_by_css_selector(".App-intro .counter")


def test_example_page(selenium):
	page = CounterPage(selenium)
	page.open()
	assert selenium.current_url == 'http://localhost:3000/counter'
	assert page.counter.text == '0'
	
	for x in range(10):
 		assert page.number == str(x)
 		page.plus_one()
	assert	page.counter.text == '10'


def test_location_root(selenium):
	selenium.get('http://localhost:3000')
	assert selenium.current_url == 'http://localhost:3000/'
	location = selenium.find_element_by_css_selector('.App-pathname i')
	assert location.text == '/'


def test_location_counter(selenium):
	page = CounterPage(selenium)
	page.open()
	assert page.location.text == "/counter"


def test_location_contacts(selenium):
	page = ContactPage(selenium)
	page.open()
	assert page.location.text == '/contacts'


def test_form(selenium):
	page = ContactPage(selenium)
	page.open()
	page.name.send_keys('ivan')
	page.email.send_keys('email.com')
	assert page.name.get_attribute('value')=='ivan'
	assert page.email.get_attribute('value')=='email.com'

def test_form_add(selenium):
	page = ContactPage(selenium)
	page.open()
	page.name.send_keys('ivan')
	page.email.send_keys('email.com')
	page.button.click()
	assert page.name.get_attribute('value')==''
	assert page.email.get_attribute('value')==''




			
			


