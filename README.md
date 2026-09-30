# Ecommerce-Selenium-Capstone
Ecommerce Selenium Automation Capstone
Project Overview

This project is an end-to-end web automation testing framework built using Python, Selenium WebDriver, and Pytest.

The automation validates a complete ecommerce workflow on Automation Exercise
.

Tech Stack

Python

Selenium WebDriver

Pytest

Page Object Model (POM)

CSV test data

JSON configuration

PyCharm

Chrome WebDriver

Test Scenario

The main automated test covers the following ecommerce flow:

Launch the application

Open the Login page

Login with test credentials

Open the Products page

Search for a product

Open the first matching product

Update the product quantity

Add the product to the cart

Open the shopping cart

Verify the cart is displayed

Verify the product exists in the cart

Verify the selected quantity

Display product, price, quantity, and total details

Capture screenshots during execution

Project Structure
Ecommerce_Selenium_Capstone/
│
├── config/
│   └── config.example.json
│
├── data/
│   └── testdata.csv
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests/
│   └── test_ecommerce.py
│
├── utils/
│   ├── csv_reader.py
│   ├── config_reader.py
│   └── screenshot.py
│
├── screenshots/
│   └── .gitkeep
│
├── .gitignore
├── README.md
├── requirements.txt
└── pytest.ini

Framework Design

The project follows the Page Object Model design pattern.

Page Objects

LoginPage handles login functionality.

HomePage handles homepage navigation.

ProductPage handles product search, product selection, quantity updates, and adding products to the cart.

CartPage handles cart verification, quantity verification, and cart details.

Utilities

CSVReader reads test data.

ConfigReader reads framework configuration.

Screenshot captures screenshots during test execution.

Test Data

Test data is maintained separately from the test code using CSV.

Example:

test_case,username,email,password,search_product,quantity
TC001,Test User,test@example.com,********,Top,3


Real credentials should not be committed to the repository.

Installation

Clone the repository and create a virtual environment:

python -m venv .venv


Activate the virtual environment.

Windows
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Running the Tests

Run the complete test:

pytest -v


Run the ecommerce test specifically:

pytest -v tests/test_ecommerce.py

Screenshots

Screenshots are generated automatically during test execution.

Generated screenshots are intentionally excluded from Git using .gitignore.

Test Reporting

The framework provides:

Step-by-step console logging

Pytest test results

Assertions for every major workflow stage

Automatic screenshots

Detailed failure information

Application Under Test

Automation Exercise:

https://automationexercise.com/

Author

Sneha Pal

Python Selenium Automation Testing Capstone Project
