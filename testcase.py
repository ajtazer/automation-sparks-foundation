from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

driver.maximize_window()

driver.get('https://www.google.com/')
driver.find_element('name', 'q').send_keys('sparks foundation')
driver.find_element('name', 'btnK').click()
time.sleep(0.25)
driver.get('https://www.thesparksfoundationsingapore.org/')
if driver.find_element_by_xpath("//div[@id='home']/div/div/h1/a/img"):
    print('Logo Exists\n Clicking on Logo')
    driver.find_element_by_xpath("//div[@id='home']/div/div/h1/a/img").click()
if driver.find_element_by_link_text("About Us"):
    print('About Button Exists\n Clicking on About')
    driver.find_element_by_link_text("About Us").click()
driver.find_element_by_link_text("Executive Team").click()
driver.find_element_by_xpath("//img[@alt='image']").click()
driver.close()
driver.get("https://www.thesparksfoundationsingapore.org/about/executive-team/")
driver.find_element_by_xpath("//div[3]/a/img").click()
driver.get("https://www.linkedin.com/in/tanwikaushik/")
driver.close()
driver.get("https://www.thesparksfoundationsingapore.org/about/executive-team/")
driver.find_element_by_link_text("LINKS").click()
driver.find_element_by_link_text("Software & App").click()
driver.get("https://www.thesparksfoundationsingapore.org/links/software-and-app/")
