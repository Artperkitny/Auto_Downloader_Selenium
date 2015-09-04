from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# driver.get("http://www.google.com")

# element = driver.find_element_by_id("lst-ib")
# element.send_keys("selenium", Keys.ENTER)

# time.sleep(5)

# assert "Python" not in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

#STAGING: https://genesis.rentlytics.com/trilogy/marketing-cost-analysis/visualization
#PROD: https://secure.rentlytics.com/trilogy/marketing-cost-analysis/visualization

#User Info
email = "art@rentlytics.com"
password = "pass4art"

def login():
	Email = driver.find_element_by_name("email")
	Password = driver.find_element_by_name("password")
	Email.send_keys(email)
	Password.send_keys(password, Keys.ENTER)

# driver.get("https://genesis.rentlytics.com/trilogy/marketing-cost-analysis/visualization")
# time.sleep(5)
# login()
# time.sleep(20)
# element1 = driver.find_elements_by_xpath("//*[@id='number_span']")


driver.get("https://secure.rentlytics.com/trilogy/marketing-cost-analysis/visualization")
login()
wait = WebDriverWait(driver, 5000)
element2 = wait.until(EC.element_to_be_clickable((By.CLASS,"dashboard-layout-subcell-host ng-scope")))
print len(element2)
for element in element2:
	print "----element----\n"
	print element.text 

#assertEqual(element1,element2) 

driver.close()