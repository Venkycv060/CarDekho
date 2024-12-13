# The browser_manager.py will handle the setup and teardown of the WebDriver, allowing for browser automation (e.g., Chrome, Firefox). We'll use Selenium for managing the browser.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
import os
import threading


class BrowserManager:
    def __init__(self, browser='chrome', headless=False):
        self.browser = browser
        self.headless = headless
        self.driver = None

    def start_browser(self):
        """Starts the browser and returns the WebDriver instance."""
        if self.browser == 'chrome':
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument("--headless")  # Run browser in headless mode (no GUI)
            options.add_argument("--start-maximized")  # Open browser in maximized mode
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")

            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            self.driver.implicitly_wait(10)  # Wait for elements to load

        elif self.browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")  # Run browser in headless mode (no GUI)

            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            self.driver.implicitly_wait(10)

        elif self.browser == 'edge':
            options = webdriver.EdgeOptions()
            if self.headless:
                options.add_argument("--headless")  # Run browser in headless mode (no GUI)

            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            self.driver.implicitly_wait(10)

        else:
            raise ValueError("Browser type not supported")

        return self.driver

    def open_url(self, url):
        """Opens a given URL in the browser."""
        if self.driver is None:
            self.start_browser()
        self.driver.get(url)

    def quit_browser(self):
        """Quits the browser."""
        if self.driver:
            self.driver.quit()

    def take_screenshot(self, filename):
        """Takes a screenshot and saves it with the given filename."""
        if self.driver:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = os.path.join(os.getcwd(), "screenshots", f"{filename}_{timestamp}.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")


# Function to run tests in all browsers simultaneously
def run_tests_in_browser(browser_name):
    browser_manager = BrowserManager(browser=browser_name, headless=True)
    browser_manager.start_browser()
    browser_manager.open_url("https://www.example.com")
    browser_manager.take_screenshot(f"example_{browser_name}")
    browser_manager.quit_browser()


# Running tests in all three browsers in parallel using threading
if __name__ == "__main__":
    browsers = ['chrome', 'firefox', 'edge']

    threads = []
    for browser_type in browsers:
        thread = threading.Thread(target=run_tests_in_browser, args=(browser_type,))
        threads.append(thread)
        thread.start()

    # Join all threads to ensure they finish before the program ends
    for thread in threads:
        thread.join()



# Usage example:
browser_anager = BrowserManager(browser='chrome', headless=True)
driver = browser_anager.start_browser()
browser_anager.open_url("https://www.example.com")
browser_anager.take_screenshot("example")
browser_anager.quit_browser()

