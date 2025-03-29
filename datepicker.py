from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait until the input field is visible and interactable
wait = WebDriverWait(driver, 10)
date_input = wait.until(EC.element_to_be_clickable((By.ID, "datetimepicker-input")))

# Clear and input the date
date_input.clear()
date_input.send_keys("01/01/2024")
date_input.send_keys(Keys.RETURN)


