"""
Web Scraping for Extracting Information

This script implements a web scraping tool using Selenium and BeautifulSoup to extract profile information from a social media site. The tool navigates through the platform search results, retrieves profiles, and extracts details such as full name, tagline, experience, education, and profile link.

The script utilizes Selenium for web automation, including opening the search page, scrolling to load more profiles, and clicking on pagination buttons. BeautifulSoup is used for parsing the HTML content of the profiles.

Note:
- This script is provided for educational purposes only. Web scraping social media may violate its terms of service and legal agreements. Users are responsible for ensuring compliance with applicable laws and terms of service.
- The script should be used responsibly and ethically, respecting the privacy and rights of individuals and organizations.
- Before using this script, ensure that you have proper authorization and consent to scrape data from any website.

Dependencies:
- requests
- urllib3
- BeautifulSoup (bs4)
- time
- functools
- re
- random
- numpy
- matplotlib
- seaborn
- pandas
- selenium

Usage:
1. Install the required dependencies using pip install.
2. Configure the Chrome driver path in the 'options.binary_location' variable.
3. Run the script and provide the search URL as input.
4. The script will scrape profile information and store it in a pandas DataFrame.

"""

# import libs
import requests #(for making HTTP requests)
import urllib3 #(URL handling)
from bs4 import BeautifulSoup as bs #(in case Selenium couldn’t handle everything)
import time
from functools import reduce
import re
import random

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


#To hide future warnings 
    #Deprecation warning pertain to future possible errors as the current code may be deprecated (eliminated)   
import warnings
warnings.filterwarnings("ignore", category=FutureWarning) 
import pandas as pd
#style options 

%matplotlib inline  
#if you want graphs to automatically without plt.show
pd.set_option('display.max_columns',500)

plt.style.use('seaborn-colorblind') #a style that can be used for plots


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By

# Initialize global variables
driver = None
loop_active = True


# import libs
import requests #(for making HTTP requests)
import urllib3 #(URL handling)
from bs4 import BeautifulSoup as bs #(in case Selenium couldn’t handle everything)
import time
from functools import reduce
import re
import random

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


#To hide future warnings 
    #Deprecation warning pertain to future possible errors as the current code may be deprecated (eliminated)   
import warnings
warnings.filterwarnings("ignore", category=FutureWarning) 
import pandas as pd
#style options 

%matplotlib inline  
#if you want graphs to automatically without plt.show
pd.set_option('display.max_columns',500)

plt.style.use('seaborn-colorblind') #a style that can be used for plots


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By

# Initialize global variables
driver = None
loop_active = True

# Function to open the supplied link using Selenium
def open_link(link):
    global driver
    
    # Establish chrome driver and go to report site URL - and refresh header
    options = Options()
    options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
    #options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options = options, service = Service("chromedriver.exe"))
    driver.get(link)

# Function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    start = time.time()
 
    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        # this command scrolls the window starting from
        # the pixel value stored in the initialScroll
        # variable to the pixel value stored at the
        # finalScroll variable
        initialScroll = finalScroll
        finalScroll += 1000

        # we will stop the script for 3 seconds so that
        # the data can load
        time.sleep(3)
        # You can change it as per your needs and internet speed

        end = time.time()

        # We will scroll for 20 seconds.
        # You can change it as per your needs and internet speed
        if round(end - start) > 20:
            break

# Function to extract information and store it in a DataFrame
def copy_names():
    global driver
    global loop_active
    
    # Scroll to the bottom of the page
    scroll_to_bottom(driver)
    time.sleep(5)
    
    # get the page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # get the page source
    profile_list = soup.find('ol', {'class': 'profile-list'})
    profiles = profile_list.find_all('li', {'class': 'ember-view'})
    pagination_button = driver.find_element(By.CSS_SELECTOR, "a.pagination__quick-link--next")
    
    data = []
    for profile in profiles:
        full_name_element = profile.find('a', {'data-test-link-to-profile-link': 'true'})
        full_name = full_name_element.text.strip() if full_name_element is not None else ''
        link_address = full_name_element['href'] if full_name_element is not None else ''
        tagline_element = profile.find('div', {'class': 'artdeco-entity-lockup__subtitle ember-view'})
        tagline = tagline_element.text.strip() if tagline_element is not None else ''

        
        # Find the div elements with class 'history-group'
        history_groups = profile.find_all('div', {'class': 'history-group'})
        print(len(history_groups))
        
        experience_items = []
        education_items = []
        
        if len(history_groups) >= 2:
            
            experience_items = history_groups[0].find_all('li', {'data-test-description-description': True})
            experience = [item.text.strip() for item in experience_items] if experience_items is not None else []

            education_items = history_groups[1].find_all('li', {'data-test-description-description': True})
            education = [item.text.strip() for item in education_items] if education_items is not None else []
        else:
            experience = ''
            education = ''

        data.append({
            'Full Name': full_name,
            'Tagline': tagline,
            'Experience': experience,
            'Education': education,
            'Link': link_address
        })

    df = pd.DataFrame(data)
    display(df)
    
    
    if pagination_button:
        pagination_button.click()
    else:
        loop_active = False

    return data

def start_loop():
    global full_list
    full_list = []
    
    global loop_active

    while loop_active:
        add_df = copy_names()
        full_list.append(add_df)

    # Close the browser window
    driver.quit()

# Open the supplied link
open_link('INSERT LINK HERE')

# Start copy loop
start_loop()
