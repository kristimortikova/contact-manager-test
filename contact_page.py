from selector import selector

class ContactPage(object):
	def __init__(self, selenium):
		super(ContactPage, self).__init__()
		self.selenium = selenium

	def open(self):
		self.selenium.get('http://localhost:3000/contacts')

	name=selector("input[name=name]")
	
	email=selector("input[name=email]")
	
	button=selector('button#add')
	
	location=selector(".App-pathname i")

	contact_name=selector(".Contact-name")

	contact_email=selector(".Contact-email")

	contacts=selector(".Contact", many=True)

	def add(self, name, email):
		self.name.send_keys(name)
		self.email.send_keys(email)
		self.button.click()
		
	
