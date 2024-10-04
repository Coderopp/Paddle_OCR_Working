from paddleocr import PaddleOCR
import requests
from PIL import Image
import io
import numpy as np
from tqdm import tqdm
import os
import subprocess
import sys
import pandas as pd

# Ugly hack fix for PaddlePaddle OpenCV import on Windows/Ubuntu
def fix_opencv_import():
    interpreter = sys.executable
    # Workaround for Windows
    if sys.platform == 'win32' and 'python.exe' not in interpreter:
        interpreter = sys.exec_prefix + os.sep + 'python.exe'
    try:
        import_cv2_proc = subprocess.Popen(
            [interpreter, "-c", "import cv2"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True  # This is the fix for Windows and Ubuntu
        )
        out, err = import_cv2_proc.communicate()
        retcode = import_cv2_proc.poll()
        if retcode != 0:
            cv2 = None
        else:
            import cv2
    except Exception as e:
        print(f"Error: Failed to import OpenCV - {str(e)}")

# Run the fix for OpenCV import
fix_opencv_import()

# Initialize OCR model
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def perform_ocr(image_url):
    def extract_text(item):
        if isinstance(item, (list, tuple)):
            for sub_item in item:
                yield from extract_text(sub_item)
        elif isinstance(item, dict):
            text = item.get('text', '')
            if isinstance(text, str) and text.strip():
                yield text.strip()
        elif isinstance(item, str) and item.strip():
            yield item.strip()

    try:
        # Download the image
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))

        # Convert image to array
        img_array = np.array(image)

        # Detect text
        result = ocr.ocr(img_array, cls=True)

        # Extract text
        texts = list(extract_text(result))

        if not texts:
            return "No text detected"

        return ', '.join(texts)  # Join texts with a separator
    except Exception as e:
        return f"Error: Failed to process image - {str(e)}"

def process_dataframe_ocr(input_csv, output_csv):
    # Load the dataframe
    df = pd.read_csv(input_csv)

    # Check if 'image_link' column exists
    if 'image_link' not in df.columns:
        print(f"Error: 'image_link' column not found in {input_csv}")
        return

    # Create a new column for OCR results
    df['ocr_text'] = ''

    # Create directory to save images (if needed)
    os.makedirs('images', exist_ok=True)

    # Process each row in the dataframe
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing OCR"):
        image_url = row['image_link']
        ocr_result = perform_ocr(image_url)
        df.at[index, 'ocr_text'] = ocr_result

    # Save the processed dataframe
    df.to_csv(output_csv, index=False)
    print(f"Processing complete. Results saved to '{output_csv}'.")

# Example usage
input_csv = '/content/batch_3.csv'  # Replace with the path to your input CSV file
output_csv = '/content/processed_images_with_ocr.csv'  # Replace with desired output path
process_dataframe_ocr(input_csv, output_csv)
