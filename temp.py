from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Or use another driver
driver.get('https://in.investing.com/rates-bonds/forward-rates')  # Replace with the actual URL

# Wait for page to load if needed
# driver.implicitly_wait(10)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
# print(soup)

# Find and print tbody content
table = soup.find('table')
# print(table)
tbody = table.find('tbody')
print(tbody)
for row in tbody.find_all('tr'):
    cells = row.find_all('td')
    cell_values = [cell.get_text(strip=True) for cell in cells]
    print(cell_values)