from selector import selector

class CounterPage(object):
	def __init__(self, selenium):
		super(CounterPage, self).__init__()
		self.selenium = selenium

	def open(self):
		self.selenium.get('http://localhost:3000/counter')

	counter=selector(".App-intro .counter")
    
	
	button=selector(".App-intro")
	

	def plus_one(self):
		self.button.click()

	
	@property
	def number(self):
		return self.counter.text


	location=selector(".App-pathname i")
		