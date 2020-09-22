from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.entry-content....')
elem.click()

elems = browser.find_elements_by_css_selector('p')
print(len(elems))
elems[0].text()

elem = browser.find_element_by_css_selector('html')
elem.text()

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('texto a buscar')
searchElem.submit()

browser.back()
browser.forward()
browser.refresh()
browser.quit()