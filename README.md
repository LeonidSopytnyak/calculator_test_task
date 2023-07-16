# Calculator App
The Calculator App is a simple web application that allows users to perform
arithmetic calculations and calculate the square of a number.

## Features

- Arithmetic calculations: Addition, subtraction, multiplication, and division.
- Square calculation: Calculate the square of a number.
- RESTful API: The app provides a RESTful API for performing calculations.

## Technologies Used

- Python
- aiohttp
- aiohttp-swagger:
- pytest

## Setup and Installation

1. Clone the repository:

   `git clone https://github.com/your-username/calculator-app.git`

2. Install the required dependencies:

    `pip install -r requirements.txt`

3. Run the application:

   `python main.py`

4. Access the application in your web browser:

   `http://0.0.0.0:8080/api/v1/doc`
## API Documentation

The API documentation is available at the following URL:
http://0.0.0.0:8080/api/v1/doc

## Running Tests

To run the tests, execute the following command:

   `unit tests: pytest server/application/test/unit/test.py`

   `api tests: pytest server/application/test/api/test.py`