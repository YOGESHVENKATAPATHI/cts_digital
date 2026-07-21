from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

driver.maximize_window()


# SIMPLE FORM DEMO


driver.get(
    "https://www.lambdatest.com/selenium-playground/simple-form-demo"
)

# By.ID
element1 = driver.find_element(
    By.ID,
    "user-message"
)
print("ID Locator Works")

# By.NAME
elements = driver.find_elements(By.NAME, "value")

if len(elements) > 0:
    print("NAME Locator Works")
else:
    print("No element found with NAME locator")

# By.CLASS_NAME
element3 = driver.find_element(
    By.CLASS_NAME,
    "form-control"
)
print("CLASS Locator Works")

# By.TAG_NAME
element4 = driver.find_element(
    By.TAG_NAME,
    "input"
)
print("TAG Locator Works")

# XPath
element5 = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("XPATH Locator Works")

# CSS Selector
element6 = driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)
print("CSS Locator Works")


# CSS SELECTOR VARIATIONS


driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

driver.find_element(
    By.CSS_SELECTOR,
    "input[id='user-message']"
)

driver.find_element(
    By.CSS_SELECTOR,
    "input.form-control"
)

print("All CSS Selectors Working")


# CHECKBOX DEMO XPATH


driver.get(
    "https://www.lambdatest.com/selenium-playground/checkbox-demo"
)

label1 = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Option 1')]"
)

print("Label Found:", label1.text)

labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("Options Found:", len(labels))


# CLOSE BROWSER


driver.quit()