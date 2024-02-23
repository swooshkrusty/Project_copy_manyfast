import cv2
from pyzbar.pyzbar import decode
import time
import csv  # Step 1: Import the csv module

# Function to write barcode data to a CSV file
def write_barcode_to_csv(barcode_data, filename='scanned_barcodes.csv'):
    with open(filename, 'a', newline='') as file:  # Open the file in append mode
        writer = csv.writer(file)
        # Write the barcode data and the current timestamp
        writer.writerow([barcode_data, time.strftime("%Y-%m-%d %H:%M:%S")])

# Function to add a color tint to the frame
def add_color_tint(frame, color):
    # ... (existing code)

# This will use the default camera
cap = cv2.VideoCapture(0)
# ... (existing code)

used_codes = []

while True:
    # Capture frame-by-frame
    # ... (existing code)

    for code in decode(frame):
        code_data = code.data.decode("utf-8")
        if code_data not in used_codes:
            print("Approved. You can enter!")
            print(code_data)
            used_codes.append(code_data)
            # Apply a green tint to the frame
            frame = add_color_tint(frame, (0, 255, 0))
            # Step 3: Save the scanned barcode to CSV
            write_barcode_to_csv(code_data)
            time.sleep(5)
        else:
            print("Sorry, this code has been already used!")
            frame = add_color_tint(frame, (0, 0, 255))
            time.sleep(5)

    # ... (existing code)

# ... (existing code)
