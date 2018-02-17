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
 	


