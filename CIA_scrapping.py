from bs4 import BeautifulSoup
import cv2
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--disable-gpu")  # Disable GPU rendering (for headless mode stability)
options.add_argument("--no-sandbox")  # Add this option if running on a Linux server
options.add_argument("--disable-dev-shm-usage")  # Prevents issues with limited shared memory
options.add_argument("--disable-images")  # Disables images to speed up loading
options.add_argument("start-maximized")  # Start Chrome maximized
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
import random, sys , os ,time

driver = webdriver.Chrome(options=options)
driver.get('z')
driver.set_page_load_timeout(5)  # Set a page load timeout of 30 seconds


try:
    # Use an explicit wait to wait for the table to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "curr_table")))
    
    # Get page source after the table has loaded
    page_source = driver.page_source
finally:
    driver.quit()

# Wait for the table to load (you may increase this time if needed)
driver.implicitly_wait(10)
page_source = driver.page_source
driver.quit()

# response = requests.get(link)
soup = BeautifulSoup(page_source,'html.parser')
print(soup)