
Copy code
# Invoice PDF Generator

This script reads Excel files containing invoice data and generates PDF invoices. The script processes all Excel files in the `invoices` directory, extracts relevant data, and creates a formatted PDF for each invoice.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- Reads invoice data from Excel files.
- Generates a PDF invoice for each Excel file.
- Extracts and formats invoice numbers, dates, and itemized details.
- Calculates and includes the total price.
- Adds company name and logo to the PDF.

## Requirements

- Python 3.x
- pandas
- fpdf
- pathlib
- glob

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/emmanuelpatrick14/Invoice-PDF-Generator.git

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install pandas fpdf
    ```

4. **Ensure your data and resources are available:**
   - Place the Excel files in the `invoices` directory.
   - Ensure the company logo image `pythonhow.png` is available in the project directory.

## Usage

1. **Run the script:**
    ```bash
    python invoice_generator.py
    ```

2. **Generated PDFs:**
   - The script will read each Excel file in the `invoices` directory, process the data, and generate a PDF in the `PDFs` directory.
