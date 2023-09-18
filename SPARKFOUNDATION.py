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

# Test Case 1: Check if the logo exists and click on it
try:
    logo_element = driver.find_element_by_xpath("//div[@id='home']/div/div/h1/a/img")
    if logo_element:
        print('Logo Exists\n Clicking on Logo')
        logo_element.click()
    else:
        print('Logo Not Found')
except NoSuchElementException:
    print('Logo Not Found')

# Test Case 2: Check if the "About Us" link exists and click on it
try:
    about_link = driver.find_element_by_link_text("About Us")
    if about_link:
        print('About Button Exists\n Clicking on About')
        about_link.click()
    else:
        print('About Link Not Found')
except NoSuchElementException:
    print('About Link Not Found')

driver.find_element_by_link_text("Executive Team").click()
if driver.find_element_by_xpath("//img[@alt='image']"):
    print("Photo FOUND , IT EXISTS")
driver.get("https://www.thesparksfoundationsingapore.org/about/executive-team/")

# Test Case 3: Check if the profile image on the "Executive Team" page exists and click on it
try:
    profile_image = driver.find_element_by_xpath("//div[3]/a/img")
    if profile_image:
        print("Profile Image Exists on Executive Team Page\n Clicking on Profile Image")
        # profile_image.click()
    else:
        print("Profile Image Not Found on Executive Team Page")
except NoSuchElementException:
    print("Profile Image Not Found on Executive Team Page")

# driver.get("https://www.linkedin.com/in/tanwikaushik/")
# driver.close()
driver.get("https://www.thesparksfoundationsingapore.org/about/executive-team/")

# Test Case 4: Check if the "LINKS" link exists on the "Executive Team" page and click on it
try:
    links_link = driver.find_element_by_link_text("LINKS")
    if links_link:
        print("LINKS Link Exists on Executive Team Page\n Clicking on LINKS")
        links_link.click()
    else:
        print("LINKS Link Not Found on Executive Team Page")
except NoSuchElementException:
    print("LINKS Link Not Found on Executive Team Page")

# Test Case 5: Check if the "Software & App" link exists on the "LINKS" page and click on it
try:
    software_app_link = driver.find_element_by_link_text("Software & App")
    if software_app_link:
        print("Software & App Link Exists on LINKS Page\n Clicking on Software & App")
        software_app_link.click()
    else:
        print("Software & App Link Not Found on LINKS Page")
except NoSuchElementException:
    print("Software & App Link Not Found on LINKS Page")

driver.get("https://www.thesparksfoundationsingapore.org/links/software-and-app/")

# Test Case 6: Check if the "Software & App" page loads successfully
software_app_page_title = driver.title
if "Software & App" in software_app_page_title:
    print("Software & App Page Loaded Successfully")
else:
    print("Software & App Page Failed to Load")

# Close the browser
driver.quit()
