from counter_page import CounterPage


def test_example(selenium):
 	selenium.get('http://localhost:3000')
 	assert selenium.title == 'Portal link'
 	assert selenium.current_url == 'http://localhost:3000/'
 	counter = selenium.find_element_by_css_selector(".App-intro .counter")
 	assert counter.text == '0'
 	button = selenium.find_element_by_css_selector(".App-intro")
 	for x in range(10): 
 		assert counter.text == str(x)
 		button.click()
 	assert	counter.text == '10'


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
			


