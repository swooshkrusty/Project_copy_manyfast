import cv2
from pyzbar.pyzbar import decode
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# with open ("https://www.barcodelookup.com/0075020103338", "r") as f:

# Replace 'url' with the actual URL you want to scrape
url = "https://www.barcodelookup.com/0075020103338"

# Make a request to the website
r = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(r.text, "html.parser")

# Find all elements with the class 'special-class'
elements = soup.find_all(class_="product-text")

# Extract the text or any other attribute from the elements
for element in elements:
    print(element.text)  # or element['href'] if  you want to extract links.

# Function to add a color tint to the frame
# ... (rest of your function)


# Function to perform web scraping using Selenium
def selenium_lookup_barcode(barcode):
    # Setup WebDriver
    driver = webdriver.Chrome()
    driver.get(f"https://www.barcodelookup.com/{barcode}")
    try:
        # Wait for the Cloudflare redirect to complete or for the page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        # Now you can access the page content
        page_content = driver.page_source
        # Here you would parse the page_content with BeautifulSoup or another method
        # to extract the information you need

    finally:
        # Remember to close the browser
        driver.quit()


# Your existing video capture setup code
# ... (rest of your code)
# Function to add a color tint to the frame
def add_color_tint(frame, color):
    """
    Adds a color tint to the frame.
    :param frame: The original image.
    :param color: A tuple of BGR values to add as a tint.
    :return: The color-tinted image.
    """
    return cv2.addWeighted(frame, 0.9, color, 0.1, 0)


# This will use the default camera (usually the built-in camera if you're on a laptop)
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

used_codes = []

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Decode any barcodes in the frame
    for code in decode(frame):
        code_data = code.data.decode("utf-8")
        if code_data not in used_codes:
            print("Approved. You can enter!")
            print(code_data)
            used_codes.append(code_data)
            # Apply a green tint to the frame as an indicator of a valid code
            frame = add_color_tint(frame, (0, 255, 0))
            time.sleep(5)
        else:
            print("Sorry, this code has been already used!")
            # Apply a red tint to the frame as an indicator of an invalid code
            frame = add_color_tint(frame, (0, 0, 255))
            time.sleep(5)

    # Display the resulting frame
    cv2.imshow("Testing-code-scan", frame)

    # Press 'q' on the keyboard to exit the loop
    if cv2.waitKey(1) == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

used_codes = []

while True:
    # Capture frame-by-frame
    # ... (rest of your code)

    for code in decode(frame):
        code_data = code.data.decode("utf-8")
        if code_data not in used_codes:
            print("Approved. You can enter!")
            print(code_data)
            used_codes.append(code_data)
            # Apply a green tint to the frame
            frame = add_color_tint(frame, (0, 255, 0))
            # Call the selenium lookup function with the scanned barcode
            selenium_lookup_barcode(code_data)
            time.sleep(5)
        else:
            print("Sorry, this code has been already used!")
            frame = add_color_tint(frame, (0, 0, 255))
            time.sleep(5)

    # ... (rest of your code)

# ... (rest of your code)
