from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
from datetime import datetime,timedelta


# Initialize the Safari WebDriver
driver = webdriver.Safari()

#driver.set_window_size(1080,800)

today = datetime.today()
first_day_melb = datetime(today.year + 1 , 1 , 1)
last_day_melb = datetime(today.year + 1, 1 , 6)
days_until_last_melb_day = (last_day_melb - today).days
days_until_first_melb_day= (first_day_melb - today).days

try:
    # Step 1: Open the website
    url = "https://puffingbilly.com.au/buy-tickets/excursion/#belgrave-lakeside"
    driver.get(url)
  
    wait = WebDriverWait(driver, 9)

    parent_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fl-node-83p6hzx42ibj")))

    right_arrow_button_selector = "[class*='date-right-arrow']"

    for i in range(days_until_last_melb_day):
    
        driver.switch_to.default_content()  # Switch back to the main page
        parent_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fl-node-83p6hzx42ibj")))
        #print("Found the parent div of the second iframe.")

        second_iframe = parent_div.find_element(By.TAG_NAME, "iframe")
        #print("Found the second iframe.")

        driver.switch_to.frame(second_iframe)  # Re-enter the iframe
       # print("Switched to the iframe.")

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        all_elements = driver.find_elements(By.CLASS_NAME, "GBEAvailCalFirstFare")

        if i >= days_until_first_melb_day and i<= days_until_last_melb_day:
            #print(f"i is {i}, days_until_first_day {days_until_first_melb_day}, days_until_last_day {days_until_last_melb_day}")
            for element in all_elements:
                text = element.text.strip()
                if text not in ["Fully Booked", "Not Available", "Departed"]:
                    date_available=datetime.today()+timedelta(days=i)
                    print(f"Available: {text} on {date_available}")

        right_arrow_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, right_arrow_button_selector)))
        right_arrow_button.click()
        #print(f"Clicked right arrow button {i + 1} time(s)")
            
        #time.sleep(7)

    page_src=driver.page_source
    with open("page_sourcef", 'w') as f:
        f.write(page_src)


except Exception as e:
    print(f"An error occurred: {e}")
    try:
        page_src5=driver.page_source
        print(f"Attempting to save page source...")
        with open("page_source_error.html", 'w') as f:
            f.write(page_src5)
        print(f"Pge saved successfully...")
    except Exception as write_error:
        print(f"failed to save page source: {write_error}")

finally:
    # Step 7: Close the browser
    driver.quit()