# Open excel file and read sites
import pandas as pd
data = pd.read_excel('frequencies.xlsx')
urls = data['page_url_domain_second']
base = "https://www.similarweb.com/website/"
start_urls = []
for url in urls:
    start_urls.append(base+str(url)+"/")

# Open from similarweb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# driver.get("https://www.similarweb.com/website/amazon.com/")

categories = []
for url in start_urls:
    driver = webdriver.Chrome(options=options, executable_path = PATH)
    driver.get(url)
    try:
        category = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='websiteRanks-item js-categoryRank']//a"))
        )
        categories.append(category.text)
        print(url+":"+category.text)
    except:
        categories.append("")
    driver.quit()
data['category'] = categories
data.to_excel("categorized.xlsx", index = False)





        
