from selenium import webdriver
browser = webdriver.Firefox(executable_path=r'D:\Programming_random_data\firefox_gecko_driver\geckodriver.exe')
browser.get('http://localhost:8000')
assert 'Django' in browser.title

