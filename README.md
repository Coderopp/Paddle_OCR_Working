
# Paddle_OCR_Working

## OCR & Captioning Script

This repository contains a Python script for performing OCR (Optical Character Recognition) and image captioning tasks. The code utilizes various libraries and models to extract text from images and generate captions for those images.

## Features
- **OCR**: Extract text from images using PaddleOCR.
- **Image Captioning**: Generate descriptive captions for images using an AI model.
- **Entity Extraction**: Identify specific entities such as width, height, and depth from the extracted OCR text.

## Prerequisites
Before you can run the script, you will need the following installed:

- Python 3.x
- Required libraries:
  - PaddleOCR
  - OpenCV
  - PIL (Python Imaging Library)
  - PyTorch
  - Transformers
  - Matplotlib
  - Any additional libraries mentioned in `requirements.txt`

To install all required libraries, run:
```bash
pip install -r requirements.txt
```

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/ocr-captioning.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ocr-captioning
    ```

3. Run the Python script with your desired input:
    ```bash
    python converted_script.py --input_path /path/to/images --output_path /path/to/save/results
    ```

### Parameters:
- `--input_path`: Path to the folder containing input images.
- `--output_path`: Path where the OCR and captioning results will be saved.

## Example
Here’s an example of running the script:
```bash
python converted_script.py --input_path ./images --output_path ./results
```

This will process all images in the `./images` directory, apply OCR and captioning, and save the results to the `./results` folder.

## Notes
- Ensure that the images you input are in supported formats (e.g., JPG, PNG).
- The performance of the OCR and captioning models may vary depending on the image quality and text complexity.

## License
This project is licensed under the MIT License.
