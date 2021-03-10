from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_path = which("chromedriver")


driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get("https://duckduckgo.com")

# search_btn = driver.find_element_by_id("search_form_input_homepage")
search_input = driver.find_element_by_xpath("(//input[contains(@class,'js-search-input')])[1]")
search_input.send_keys("My user agent")
search_input.send_keys(Keys.ENTER)

# search_btn = driver.find_element_by_id("search_button_homepage")
# search_btn.click()

print(driver.page_source)