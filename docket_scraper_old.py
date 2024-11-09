import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
from pyvirtualdisplay import Display

def test_register_of_actions():
    # Set up virtual display
    display = Display(visible=0, size=(1920, 1080))
    display.start()

    # Setup Chrome options
    chrome_options = Options()
    # Remove the headless argument
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Setup Chrome WebDriver using webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Navigate to the URL
        url = "https://portal-dc.tylertech.cloud/app/RegisterOfActions/#/DF776BA893A6FB7A3A8BB6D01F57968CB4CD808A86B2E789B257B77623695A95F96DB25395EB7C0081A6543F2F01C3C87F6E63505B2D4F00532C3AC5492C3336087483DC9F7128EB5DF1A1DCEF780A6B/anon/portalembed"
        driver.get(url)

        # Wait for the page to load (adjust timeout as needed)
        wait = WebDriverWait(driver, 20)

        # Check if the main app div is present
        app_div = wait.until(EC.presence_of_element_located((By.ID, "app")))
        print("Main app div loaded successfully.")

        # Check for the presence of the case summary section
        case_summary = wait.until(EC.presence_of_element_located((By.ID, "header-info")))
        print("Case summary section found.")

        # Look for document icons
        document_icons = driver.find_elements(By.CSS_SELECTOR, "img.roa-icon.roa-clickable")
        print(f"Found {len(document_icons)} clickable document icons.")

        # Attempt to click the first document icon (if any exist)
        if document_icons:
            print(f"Attempting to click document icon: {document_icons[0].get_attribute('outerHTML')}")
            
            # Try JavaScript click
            driver.execute_script("arguments[0].click();", document_icons[0])
            print("Clicked document icon using JavaScript.")
            
            # Wait and check for any changes
            time.sleep(5)
            
            # Check for JavaScript errors
            logs = driver.get_log('browser')
            for log in logs:
                if log['level'] == 'SEVERE':
                    print(f"JavaScript error: {log['message']}")
            
            # Check network activity
            # performance_logs = driver.get_log('performance')
            # for log in performance_logs:
            #     if 'Network.responseReceived' in log['message']:
            #         print(f"Network activity detected: {log['message']}")
            
            # Take a screenshot
            driver.save_screenshot("after_click.png")
            print("Screenshot saved as 'after_click.png'")
            
            # Print current URL
            print(f"Current URL after click: {driver.current_url}")
            
            # Check page source for any changes
            if 'pdf' in driver.page_source.lower():
                print("The page source contains 'pdf'. The document might be embedded in the page.")
            else:
                print("No 'pdf' found in the page source.")

        # Check for any error messages
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message")
            print(f"Error message found: {error_message.text}")
        except:
            print("No error messages found.")

        # You can add more specific checks here based on the page structure

    except TimeoutException:
        print("Timed out waiting for page elements to load")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the browser
        driver.quit()
        # Stop the virtual display
        display.stop()

if __name__ == "__main__":
    test_register_of_actions()