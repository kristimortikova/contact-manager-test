class CounterPage(object):
	"""docstring for ClassName"""
	def __init__(self, selenium):
		super(CounterPage, self).__init__()
		self.selenium = selenium

	def open(self):
		self.selenium.get('http://localhost:3000')
    
	@property
	def counter(self):
		return self.selenium.find_element_by_css_selector(".App-intro .counter")
	
	@property
	def button(self):
		return self.selenium.find_element_by_css_selector(".App-intro")

	def plus_one(self):
		self.button.click()

	@property
	def number(self):
		return self.counter.text