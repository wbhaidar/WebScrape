from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to create a Safari WebDriver
def create_driver():
    return webdriver.Safari()

# Function to check availability
def check_availability():
    print("Checking availability...")
    url = "https://puffingbilly.com.au/buy-tickets/excursion/#belgrave-lakeside"
    driver = create_driver()
    driver.get(url)

    try:
        # Wait for the page to load
        time.sleep(5)  # Adjust this based on your page load time
        
        # Locate availability elements (update with correct selectors)
        availability_elements = driver.find_elements(By.CLASS_NAME, "ticket-availability-class")  # Replace with the correct class name

        # Check for available tickets
        available_dates = []
        for element in availability_elements:
            if "Available" in element.text:  # Adjust condition to match the actual text
                available_dates.append(element.text)

        if available_dates:
            print(f"Tickets available for: {available_dates}")
            # Add notification logic here if needed
        else:
            print("No tickets available.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


# Keep the script running
if __name__ == "__main__":
	check_availability()
