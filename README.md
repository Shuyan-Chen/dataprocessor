# Data Processor
Excel Data Extractor is a Django backend application that processes uploaded Excel files and provides API endpoints to access the processed data.

## Setup Instructions
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run database migrations:
6. Start the development server:

## Usage Guide

### API Endpoints

1. Upload Excel File:
- URL: `/file_extractor/upload/`
- Method: POST
- Parameters: file (multipart/form-data)
- Response: Success or failure message

2. Retrieve Processed Data:
- URL: `/file_extractor/processed-data/`
- Method: GET
- Response: List of processed data in JSON format

## Code Overview





