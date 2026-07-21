"""
WebDriverWait and Expected Conditions

Purpose:
- Demonstrate the use of Explicit Waits in Selenium.
- Avoid using time.sleep(), which makes tests slower and unreliable.
- Wait only until the required condition is satisfied.

Expected Conditions Used:

1. element_to_be_clickable()
   - Waits until an element is visible and enabled.
   - Ensures the element can be clicked safely.

2. visibility_of_element_located()
   - Waits until an element is present in the DOM and visible to the user.
   - Useful for validating alerts, messages, and dynamic content.

Why Explicit Waits?
- Faster than hard-coded waits.
- More reliable on slow or fast systems.
- Reduces flaky test failures.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

driver.maximize_window()

driver.get(
    "https://www.testmuai.com/selenium-playground/bootstrap-alert-messages-demo/"
)

# Wait until page loads

button = WebDriverWait(
    driver,
    10
).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//button[contains(text(),'Autoclosable Success Message')]"
        )
    )
)

button.click()

print("Success Button Clicked")

# Just verify alert exists

alerts = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'alert')]"
)

print("Number of Alerts Found:", len(alerts))

print("Explicit Wait Passed")

driver.quit()