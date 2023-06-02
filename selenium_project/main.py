from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumChromeDriver:
    def __init__(self):
        self.driver = None
    
    # Initialize driver to start
    def setup_driver(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    # Initialize web driver to specific url
    def search(self):
        website = "https://www.newegg.com/"
        self.driver.get(website)
        
    # Navigate to the "Today's Best Deal"
    def navigate(self):
        best_deals_xpath = '//*[@id="trendingBanner_720202"]/span'
        self.best_deals_link = self.driver.find_element("xpath", best_deals_xpath)
        self.best_deals_link.click()
        
    # Scrape product info from the current Best Deals    
    def scrape_details(self):
        best_deals_product_info_xpath = "//div[contains(@class, 'item-cells-wrap tile-cells five-cells')][.//span]"
        self.best_deals_names = self.driver.find_elements("xpath", best_deals_product_info_xpath)
        
        # Iterate through the current spans within div
        for best_deals_name in self.best_deals_names:
            text_content = best_deals_name.text
            print(text_content)
        
if __name__ == '__main__':
    chrome_driver = SeleniumChromeDriver()
    chrome_driver.setup_driver()
    chrome_driver.search()
    chrome_driver.navigate()
    chrome_driver.scrape_details()
