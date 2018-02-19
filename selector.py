def selector(value):
	@property
	def selector_property(self):
		return self.selenium.find_element_by_css_selector(value)
	return selector_property