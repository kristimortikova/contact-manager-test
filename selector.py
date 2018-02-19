def selector(value, many=False):
	@property
	def selector_property(self):
		if many:
			return self.selenium.find_elements_by_css_selector(value)
		return self.selenium.find_element_by_css_selector(value)
	return selector_property