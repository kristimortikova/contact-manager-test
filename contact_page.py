class ContactPage(object):
	def __init__(self, selenium):
		super(ContactPage, self).__init__()
		self.selenium = selenium

	def open(self):
		self.selenium.get('http://localhost:3000/contacts')

	@property
	def name(self):
		return self.selenium.find_element_by_css_selector("input[name=name]")

	@property
	def email(self):
		return self.selenium.find_element_by_css_selector("input[name=email]")

	@property
	def button(self):
		return self.selenium.find_element_by_css_selector("button#add")

	@property
	def location(self):
		return self.selenium.find_element_by_css_selector(".App-pathname i")	
