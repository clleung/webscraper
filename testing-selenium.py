from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Configure Chrome options
options = Options()
options.headless = True  # Enable headless mode
options.add_argument("--window-size=1920,1200")  # Set the window size

# Set the path to the Chromedriver
DRIVER_PATH = '/path/to/chromedriver'

# Initialize the Chrome driver with the specified options
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# Your code here to interact with the page
# ...

# It's a good practice to close the driver when you're finished
driver.quit()