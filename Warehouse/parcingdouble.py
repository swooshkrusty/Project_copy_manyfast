import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def scrape_website(url):
    # Use the browser instance created outside of the function
    browser.get(url)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h4"))
    )
    h4_tag = browser.find_element(By.TAG_NAME, "h4").text

    try:
        barcode_formats = browser.find_element(
            By.XPATH,
            "//div[contains(@class, 'product-text-label') and contains(text(), 'Barcode Formats:')]/span[contains(@class, 'product-text')]",
        )
        barcode_formats = barcode_formats.text
    except NoSuchElementException:
        barcode_formats = "Not found"

    try:
        category_element = browser.find_element(
            By.XPATH,
            "//div[contains(@class, 'product-text-label') and contains(text(), 'Category:')]/span[contains(@class, 'product-text')]",
        )
        category = category_element.text
    except NoSuchElementException:
        category = "Not found"

    try:
        manufacturer_element = browser.find_element(
            By.XPATH,
            "//div[contains(@class, 'product-text-label') and contains(text(), 'Manufacturer:')]/span[contains(@class, 'product-text')]",
        )
        manufacturer = manufacturer_element.text
    except NoSuchElementException:
        manufacturer = "Not found"

    try:
        description_element = browser.find_element(
            By.XPATH,
            "//div[contains(@class, 'product-text-label') and contains(text(), 'Description:')]/span[contains(@class, 'product-text')]",
        )
        description = description_element.text
    except NoSuchElementException:
        description = "Not found"

    try:
        ingredients_element = browser.find_element(
            By.XPATH,
            "//div[contains(@class, 'product-text-label') and contains(text(), 'Ingredients:')]/span[contains(@class, 'product-text')]",
        )
        ingredients = ingredients_element.text
        # if ingredients_element else "Not found"
    except NoSuchElementException:
        ingredients = "Not found"

    try:
        nutrition_facts_elements = browser.find_element(
            By.XPATH,
            "//div[contains(@class, 'product-text-label') and contains(text(), 'Nutrition Facts:')]/span[contains(@class, 'product-text')]",
        )
        nutrition_facts = nutrition_facts_elements.text
    except NoSuchElementException:
        nutrition_facts = "Not found"

    attributes_elements = browser.find_elements(
        By.XPATH,
        "//div[contains(@class, 'product-text-label') and contains(text(), 'Attributes:')]/ul[@id='product-attributes']/li[@class='product-text']",
    )
    attributes = (
        [element.text for element in attributes_elements]
        if attributes_elements
        else ["Not found"]
    )

    image_elements = browser.find_elements(By.CSS_SELECTOR, ".thumb-box img")
    image_urls = [
        img.get_attribute("src") for img in image_elements
    ]  # gets all image URLs

    return (
        h4_tag,
        barcode_formats,
        category,
        manufacturer,
        description,
        ingredients,
        nutrition_facts,
        attributes,
        image_urls,
    )


# Set up the Selenium browser with options
options = webdriver.ChromeOptions()
options.headless = True  # Run in headless mode
browser = webdriver.Chrome(options=options)

# List of URLs to scrape
urls_to_scrape = [
    # "https://www.barcodelookup.com/0075020095657",
    "https://www.barcodelookup.com/0075020103338",
    # "https://www.barcodelookup.com/0858010005627",
]

# Open the CSV file outside of the loop
with open("product_info.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "Product Name",
            "Barcode Formats",
            "Category",
            "Manufacturer",
            # "Barcode UPC",
            "Description",
            "Ingredients",
            "Nutrition Facts",
            "Attributes",
            "Image1",
            "Image2",
            "Image3",
            "Image4",
            "Image5",
            "Image6",
            "Image7",
        ]
    )  # Write the header once

    # Loop through each URL and scrape data
    for url in urls_to_scrape:
        (
            product_name,
            barcode_formats,
            category,
            manufacturer,
            description,
            ingredients,
            nutrition_facts,
            attributes,
            image_urls,
        ) = scrape_website(url)

        # Ensure that there are always five columns for images
        image_urls += [""] * (5 - len(image_urls))
        image_urls = image_urls[:5]

        writer.writerow(
            [product_name]
            + [barcode_formats]
            + [category]
            + [manufacturer]
            + [description]
            + [ingredients]
            + [nutrition_facts]
            + [attributes]
            + image_urls
        )  # Write data for each product

browser.quit()
