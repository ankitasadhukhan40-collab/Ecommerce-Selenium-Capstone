import os
import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

from utils.csv_reader import CSVReader
from utils.config_reader import ConfigReader
from utils.screenshot import Screenshot


PROJECT_ROOT = os.path.dirname(
os.path.dirname(
os.path.abspath(__file__)

)
)

CSV_PATH = os.path.join(
PROJECT_ROOT,
"data",
"testdata.csv"
)

class TestMaxStyleEcommerce:
    # ========================================================
    # SETUP
    # ========================================================

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver

        self.config = ConfigReader.load_config()

        self.data = CSVReader.get_first_record(
            CSV_PATH
        )

        print("\nTest data loaded:")
        print(self.data)

    # ========================================================
    # COMPLETE E-COMMERCE TEST
    # ========================================================

    def test_max_style_ecommerce_flow(self):
        # ====================================================
        # STEP 1 - LAUNCH BROWSER
        # ====================================================

        print("\nSTEP 1: LAUNCH BROWSER")

        current_url = self.driver.current_url

        print(
            f"Current URL: {current_url}"
        )

        assert "automationexercise" in current_url.lower(), (
            "Application did not open correctly."
        )

        Screenshot.capture(
            self.driver,
            "01_home_page"
        )

        # ====================================================
        # STEP 2 - LOGIN
        # ====================================================

        print("\nSTEP 2: LOGIN")

        login_page = LoginPage(
            self.driver,
            self.config["timeout"]
        )

        login_page.open_login()

        login_page.login(
            self.data["email"],
            self.data["password"]
        )

        assert login_page.verify_login(), (
            "Login failed."
        )

        print("Login successful.")

        Screenshot.capture(
            self.driver,
            "02_login_success"
        )
        # ====================================================
        # CLEAR EXISTING CART
        # ====================================================

        print("\nCLEARING EXISTING CART")

        cart_page = CartPage(
            self.driver,
            self.config["timeout"]
        )

        cart_page.clear_cart()

        print("Existing cart cleared.")

        # ====================================================
        # STEP 3 - OPEN PRODUCTS
        # ====================================================

        # STEP 3 - OPEN PRODUCTS

        print("\nSTEP 3: OPEN PRODUCTS")

        home_page = HomePage(
            self.driver,
            self.config["timeout"]
        )

        home_page.open_products()

        print(
            f"Products page URL: {self.driver.current_url}"
        )

        assert "/products" in self.driver.current_url.lower(), (
            f"Products page was not opened. "
            f"Current URL: {self.driver.current_url}"
        )

        Screenshot.capture(
            self.driver,
            "03_products_page"
        )

        # ====================================================
        # STEP 4 - SEARCH PRODUCT
        # ====================================================

        print("\nSTEP 4: SEARCH PRODUCT")

        product_page = ProductPage(
            self.driver,
            self.config["timeout"]
        )

        search_product = self.data["search_product"]

        print(
            f"Searching for product: {search_product}"
        )

        product_page.search_product(
            search_product
        )

        assert product_page.verify_search_results(), (
            "Search results were not displayed."
        )

        product_count = (
            product_page.get_product_count()
        )

        assert product_count > 0, (
            "No products found."
        )

        print(
            f"Products found: {product_count}"
        )

        Screenshot.capture(
            self.driver,
            "04_search_product"
        )

        # ====================================================
        # STEP 5 - OPEN PRODUCT
        # ====================================================

        print("\nSTEP 5: OPEN PRODUCT")

        product_page.open_first_product()

        assert "/product_details/" in (
            self.driver.current_url.lower()
        ), (
            "Product details page was not opened."
        )

        print(
            "Product details page opened."
        )

        Screenshot.capture(
            self.driver,
            "05_product_details"
        )

        # ====================================================
        # STEP 6 - UPDATE QUANTITY
        # ====================================================

        print("\nSTEP 6: UPDATE QUANTITY")

        quantity = int(
            self.data["quantity"]
        )

        product_page.set_quantity(
            quantity
        )

        print(
            f"Quantity selected: {quantity}"
        )

        Screenshot.capture(
            self.driver,
            "06_quantity_updated"
        )

        # ====================================================
        # STEP 7 - ADD PRODUCT TO CART
        # ====================================================

        print("\nSTEP 7: ADD PRODUCT TO CART")

        product_page.add_product_to_cart()

        print(
            "Product added to cart."
        )

        Screenshot.capture(
            self.driver,
            "07_product_added_to_cart"
        )

        # ====================================================
        # STEP 8 - OPEN CART
        # ====================================================

        print("\nSTEP 8: OPEN CART")

        product_page.view_cart_from_popup()

        print(
            "Cart opened from popup."
        )

        # ====================================================
        # STEP 9 - VERIFY CART
        # ====================================================

        print("\nSTEP 9: VERIFY CART")

        cart_page = CartPage(
            self.driver,
            self.config["timeout"]
        )

        assert cart_page.verify_cart_displayed(), (
            "Cart page was not displayed."
        )

        Screenshot.capture(
            self.driver,
            "08_cart_page"
        )

        # ====================================================
        # STEP 10 - VERIFY PRODUCT IN CART
        # ====================================================

        print("\nSTEP 10: VERIFY PRODUCT IN CART")

        cart_product_count = (
            cart_page.get_cart_product_count()
        )

        assert cart_product_count >= 1, (
            "Cart is empty."
        )

        print(
            f"Products in cart: {cart_product_count}"
        )

        # ====================================================
        # STEP 11 - VERIFY QUANTITY
        # ====================================================

        print("\nSTEP 11: VERIFY QUANTITY")

        actual_quantity = (
            cart_page.get_quantity()
        )

        expected_quantity = str(
            quantity
        )

        print(
            f"Expected quantity: {expected_quantity}"
        )

        print(
            f"Actual quantity: {actual_quantity}"
        )

        assert actual_quantity == expected_quantity, (
            f"Expected quantity {expected_quantity}, "
            f"but got {actual_quantity}"
        )

        # ====================================================
        # STEP 12 - CART DETAILS
        # ====================================================

        print("\nSTEP 12: CART DETAILS")

        details = (
            cart_page.get_product_details()
        )

        print()
        print("=" * 60)
        print("                 MAX STYLE")
        print("             SHOPPING CART")
        print("=" * 60)

        for item in details:
            print(item)

        print("=" * 60)

        # ====================================================
        # FINAL SCREENSHOT
        # ====================================================

        Screenshot.capture(
            self.driver,
            "09_cart_verification"
        )

        # ====================================================
        # TEST PASSED
        # ====================================================

        print()
        print("=" * 60)
        print("          MAX STYLE TEST PASSED")
        print("=" * 60)
        print()