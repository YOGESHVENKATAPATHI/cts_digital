from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Browser

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

driver.implicitly_wait(10)

# Open Selenium Playground

driver.get(
    "https://www.lambdatest.com/selenium-playground/"
)

print("Home Page Title:")
print(driver.title)

# Click Simple Form Demo

driver.find_element(
    By.LINK_TEXT,
    "Simple Form Demo"
).click()

# Verify URL

assert "simple-form-demo" in driver.current_url

print("URL Verification Passed")
print(driver.current_url)

# Navigate Back

driver.back()

print("Returned to Home Page")

# Open Google in New Tab

driver.execute_script(
    'window.open("https://www.google.com");'
)

# Print All Window Handles

print("\nWindow Handles:")
print(driver.window_handles)

# Switch to Google Tab

driver.switch_to.window(
    driver.window_handles[1]
)

print("\nGoogle Title:")
print(driver.title)

# Switch Back

driver.switch_to.window(
    driver.window_handles[0]
)

print("\nReturned to Original Tab")

# Window Size

print("\nCurrent Window Size:")
print(driver.get_window_size())

driver.set_window_size(
    1280,
    800
)

print("\nNew Window Size:")
print(driver.get_window_size())

# Screenshot

driver.save_screenshot(
    "playground_screenshot.png"
)

print("\nScreenshot Saved")

driver.quit()