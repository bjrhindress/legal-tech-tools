import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
from pyvirtualdisplay import Display

def test_register_of_actions():
    display = Display(visible=0, size=(1920, 1080))
    display.start()

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Add this line to disable PDF viewers
    chrome_options.add_experimental_option("prefs", {
        "plugins.always_open_pdf_externally": True
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        url = "INSERT URL HERE"
        driver.get(url)

        wait = WebDriverWait(driver, 20)

        # Wait for the document icons to be clickable
        document_icons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.roa-icon.roa-clickable")))
        print(f"Found {len(document_icons)} clickable document icons.")

        if document_icons:
            icon = document_icons[0]
            print(f"Attempting to click document icon: {icon.get_attribute('outerHTML')}")
            
            # Scroll the icon into view
            driver.execute_script("arguments[0].scrollIntoView(true);", icon)
            time.sleep(1)  # Give time for any animations to complete
            
            # Try multiple click methods
            try:
                icon.click()
                print("Clicked document icon using regular click.")
            except ElementClickInterceptedException:
                ActionChains(driver).move_to_element(icon).click().perform()
                print("Clicked document icon using ActionChains.")
            except:
                driver.execute_script("arguments[0].click();", icon)
                print("Clicked document icon using JavaScript.")
            
            # Wait for potential download or new window
            time.sleep(5)
            
            # Check for new windows or tabs
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
                print(f"Switched to new window. Current URL: {driver.current_url}")
            
            # Check downloads folder
            downloads_path = os.path.expanduser("~/Downloads")
            downloaded_files = [f for f in os.listdir(downloads_path) if f.endswith('.pdf')]
            if downloaded_files:
                print(f"PDF downloaded: {downloaded_files[-1]}")
            else:
                print("No PDF file found in downloads folder.")

        # Take a screenshot
        driver.save_screenshot("after_click.png")
        print("Screenshot saved as 'after_click.png'")

    except TimeoutException:
        print("Timed out waiting for page elements to load")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()
        display.stop()

if __name__ == "__main__":
    test_register_of_actions()