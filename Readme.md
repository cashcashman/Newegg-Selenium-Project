# Newegg Selenium Project (Python)
In this project Selenium is going to http://newegg.com, locating the _Today's Best Deals_ area, then printing in the console each of the items product descriptions (Title, Original Price, Current Price, Percentage Saved, Shipping Info) before closing.

## Requirements
Use the package manager [pip](https://pypi.org/project/selenium/) to install selenium.
```bash
pip install selenium
```
Also [pip](https://pypi.org/project/webdriver-manager/) to intall webdriver-manager
```bash
pip install webdriver-manager
```
## Initialzing
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
```
## Usage
``` python
# Starting webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Keeping window open after completing task
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# Opening site
driver.get('Insert http://... here')

# Locating element or elements
driver.find_element("xpath","insert //xpath here") # single element
driver.find_elements("xpath","insert //xpath here") # multiple elements

# Clicking element
driver.click()

# Printing element as text
variable = driver.find_elements("xpath","insert //xpath here")
text_content = variable.text
print(text_content)
```
