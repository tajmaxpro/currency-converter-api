# Currency Converter API

## Description
This project is a RESTful API for converting currencies using an external [Exchange Rates Data API](https://apilayer.com/marketplace/exchangerates_data-api) service.

## Features
- Convert currencies based on real-time exchange rates.
- Supports a wide range of currencies.
- Easy-to-use API with clear documentation.

# Try It on Your Local Machine:

To test the project on your local machine, follow these steps:

## Requirements
- Python 3.x
- Django
- Django Rest Framework (DRF)
- Requests library

## Installation

1. Clone the repository:

    ```
   git clone https://github.com/tajmaxpro/currency-converter-api.git
   cd currency-converter-api
    ```   

2. **Create and Activate a Virtual Environment:**

    ```
    python -m venv yourvenv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Project Dependencies:**

    ```
    pip install -r requirements.txt
    ```

6. **Apply Migrations:**

    ```
    python manage.py migrate
    ```

7. **Run the Development Server:**

    ```
    python manage.py runserver
    ```

8. Access the API at http://localhost:8000/api/convert/


## API Usage

**Convert Currencies**

Endpoint: */api/convert/*

- Method: GET

Request Parameters:

- from_currency (required): The source currency code (e.g., USD).
- to_currency (required): The target currency code (e.g., RUB).
- amount (required): The amount to be converted.

*Example Request:*

    
    GET /api/convert/?from_currency=USD&to_currency=RUB&amount=1
   

*Example Response:*

   
    {

    "result": 96.02

    }
    

**Contact**

For inquiries or assistance with this project, please contact [@tajmaxpro](https://t.me/tajmaxpro).
