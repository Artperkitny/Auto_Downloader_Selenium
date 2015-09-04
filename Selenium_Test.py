import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


test_data = ("https://www.youtube.com/watch?v=QMokMQ8Bu7Y",
			"https://www.youtube.com/watch?v=e0Og94zSuYM",
			"https://www.youtube.com/watch?v=OVMuwa-HRCQ",
			"https://www.youtube.com/watch?v=pfvfd5YxuxA",
			"https://www.youtube.com/watch?v=5PvZFmE-xtU",)

chromedriver = os.path.dirname(os.path.realpath(__file__))+"/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
for i in test_data:
	driver.get("http://youtubeinmp3.com/fetch/?api=advanced&format=JSON&video=http://www.youtube.com/watch?v={}".format(i[32:]))
	time.sleep(22.5)
										
driver.quit()

