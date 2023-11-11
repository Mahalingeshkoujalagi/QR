import os
import cv2
from pyzbar.pyzbar import decode
import csv

def decode_qr_code(image_path):
    image = cv2.imread(image_path)
    barcode = decode(image)

    if barcode:
        barcodeData = barcode[0].data.decode('utf-8')
        return barcodeData
    else:
        return None

def main(input_folder, output_csv):
    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Image File', 'Link'])

        for filename in os.listdir(input_folder):
            if filename.endswith('.png') or filename.endswith('.jpg'):
                image_path = os.path.join(input_folder, filename)
                link = decode_qr_code(image_path)

                if link:
                    csv_writer.writerow([filename, link])

if __name__ == "__main__":
    input_folder = "qr_codes"
    output_csv = "image_links.csv"

    main(input_folder, output_csv)
