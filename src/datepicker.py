import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """
    Sets up and returns a Selenium WebDriver instance using Chrome.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # Optional: start in full screen
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def open_target_page(driver, url):
    """
    Navigates to the given URL.
    """
    driver.get(url)
    time.sleep(2)

def select_date(driver, date_string):
    """
    Selects the date in the input field using the datepicker.
    """
    try:
        # Find the input field
        input_field = driver.find_element(By.ID, "datepicker")
        input_field.click()
        input_field.clear()
        input_field.send_keys(date_string)
        input_field.send_keys(Keys.RETURN)
        print(f"[INFO] Date '{date_string}' selected successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to select date: {e}")

def main():
    """
    Main function that controls the browser and selects a date.
    """
    url = "https://jqueryui.com/resources/demos/datepicker/default.html"
    date_string = "07/04/2025"  # MM/DD/YYYY format

    driver = setup_driver()
    try:
        open_target_page(driver, url)
        select_date(driver, date_string)
    finally:
        time.sleep(5)  # View result before closing
        driver.quit()

if __name__ == "__main__":
    main()


