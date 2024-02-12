# Web Scraping Example
#### Robert Conner 
![LinkedIn](img/linkedin_icon.webp) https://www.linkedin.com/in/robert-conner8/

![Personal Website](img/website_icon.webp) https://www.RobertjConner.com/

## Description
This project demonstrates a web scraping tool designed to extract profile information from web pages. The tool utilizes Selenium and BeautifulSoup to navigate through search results, retrieve profiles, and extract details such as full name, tagline, experience, education, and profile link. In my case, I used similar code to capture a list of individuals who shared my alma mater and industry to create a specialized list for expanded networking.

## Features
- Automated web scraping: The tool automates the process of navigating through search results and extracting profile information.
- Automated Page Scrolling for Dynamic Pages: Some websites use dynamic loading, preventing many webscrapping applications. This code automatically scrolls the page until it reaches the bottom, before scraping any information. This ensures all data is accessible.
- Profile data extraction: It retrieves key details from web pages, including full name, tagline, experience, education, and profile link.
- Customizable and extensible: Users can modify the script to extract additional information or adapt it for other websites.

## How It Works
- Initialization: The script initializes the necessary libraries and global variables.
- Opening the Link: It uses Selenium to open the search link provided by the user.
- Scrolling: The tool scrolls to the bottom of the page to load more profiles dynamically.
- Profile Extraction: It extracts profile information using BeautifulSoup, including full name, tagline, experience, education, and profile link.
- Pagination: The script clicks on pagination buttons to navigate to the next page of search results.
- Data Storage: Profile information is stored in a pandas DataFrame.
- Looping: The process continues until all profiles have been extracted.

## Getting Started
- Install Dependencies: Ensure you have the required dependencies installed. You can install them using pip install <dependency>.
- Download ChromeDriver: Download the latest version of ChromeDriver compatible with your Chrome browser. You can find the latest release on the ChromeDriver Downloads page: https://chromedriver.chromium.org/downloads. Make sure to choose the appropriate version for your operating system.
- Configure Chrome Driver: Set the path to the ChromeDriver executable in the script's options. For example, if you've downloaded ChromeDriver and placed it in the same directory as your script, you can set the path like this:

```
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options, executable_path='./chromedriver.exe')
```

- Run the Script: Execute the script and provide the search URL as input. You will want to ensure that you modify the beautifulsoup code to represent the website you are scraping. You find the labels and attributes used to identify the specfic information on the page by viewing the source (easily done in Chrome by going to Developer Options), and then modifying the code accordingly.

- Data Retrieval: The script will scrape profile information and store it in a pandas DataFrame.

![Example Dataframe Info](/img/cols.png "Pandas Dataframe Info")

## Technical Details
- Dependencies: The project relies on libraries such as Selenium, BeautifulSoup, pandas, numpy, matplotlib, and seaborn.
- Selenium: Used for web automation, including opening the search page, scrolling, and pagination.
- BeautifulSoup: Utilized for parsing the HTML content of profiles.
- Pandas: Used for storing and manipulating scraped data in a DataFrame.
- Chrome Driver: Required for Selenium to interact with the Chrome browser.

## Other Use Cases
This web scraping tool can be adapted for various other websites and use cases, including:

- Extracting job postings from career websites.
- Scraping product information from e-commerce platforms.
- Gathering news articles from news websites.
- Collecting real estate listings from property websites.
- Monitoring changes in website content for research or tracking purposes.
