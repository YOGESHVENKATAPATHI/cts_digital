"""
Hands-On 4 - Task 1

Selenium Components

1. WebDriver
   - Acts as a bridge between test scripts and browsers.
   - Sends commands to the browser.

2. Selenium Grid
   - Executes tests on multiple browsers and machines.
   - Supports parallel execution.

3. Selenium IDE
   - Record and playback tool.
   - Generates automation scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    ),
    options=options
)

driver.implicitly_wait(10)

driver.get(
    "https://www.lambdatest.com/selenium-playground/"
)

print("Page Title:", driver.title)

driver.quit()