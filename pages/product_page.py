from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ============================================================
    # LOCATORS
    # ============================================================

    SEARCH_INPUT = (
        By.ID,
        "search_product"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    SEARCH_RESULTS = (
        By.CSS_SELECTOR,
        ".features_items .product-image-wrapper"
    )

    PRODUCT_ITEMS = (
        By.CSS_SELECTOR,
        ".features_items .product-image-wrapper"
    )

    VIEW_PRODUCT_BUTTONS = (
        By.CSS_SELECTOR,
        ".features_items .choose a"
    )

    QUANTITY_INPUT = (
        By.ID,
        "quantity"
    )

    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "button.cart"
    )

    CART_POPUP = (
        By.ID,
        "cartModal"
    )

    VIEW_CART_LINK = (
        By.CSS_SELECTOR,
        "#cartModal a[href='/view_cart']"
    )

    # ============================================================
    # SEARCH PRODUCT
    # ============================================================

    def search_product(self, product_name):

        print(
            f"Searching for product: {product_name}"
        )

        search_input = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        search_input.clear()

        search_input.send_keys(
            product_name
        )

        search_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        )

        search_button.click()

        self.wait.until(
            EC.presence_of_all_elements_located(
                self.SEARCH_RESULTS
            )
        )

    # ============================================================
    # VERIFY SEARCH RESULTS
    # ============================================================

    def verify_search_results(self):

        try:

            results = self.wait.until(
                EC.presence_of_all_elements_located(
                    self.SEARCH_RESULTS
                )
            )

            return len(results) > 0

        except TimeoutException:

            return False

    # ============================================================
    # GET PRODUCT COUNT
    # ============================================================

    def get_product_count(self):

        try:

            products = self.wait.until(
                EC.presence_of_all_elements_located(
                    self.PRODUCT_ITEMS
                )
            )

            return len(products)

        except TimeoutException:

            return 0

    # ============================================================
    # OPEN FIRST PRODUCT
    # ============================================================

    def open_first_product(self):

        print(
            "Opening first product..."
        )

        product_buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                self.VIEW_PRODUCT_BUTTONS
            )
        )

        if not product_buttons:
            raise AssertionError(
                "No product available to open."
            )

        first_product = product_buttons[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            first_product
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_PRODUCT_BUTTONS
            )
        )

        first_product.click()

        self.wait.until(
            EC.url_contains(
                "/product_details/"
            )
        )

        print(
            f"Product details URL: "
            f"{self.driver.current_url}"
        )

    # ============================================================
    # SET QUANTITY
    # ============================================================

    def set_quantity(self, quantity):

        quantity_input = self.wait.until(
            EC.visibility_of_element_located(
                self.QUANTITY_INPUT
            )
        )

        quantity_input.click()

        quantity_input.clear()

        quantity_input.send_keys(
            str(quantity)
        )

        actual_value = quantity_input.get_attribute(
            "value"
        )

        print(
            f"Quantity entered in product page: "
            f"{actual_value}"
        )

        assert actual_value == str(quantity), (
            f"Quantity was not entered correctly. "
            f"Expected {quantity}, "
            f"but got {actual_value}"
        )

    # ============================================================
    # ADD PRODUCT TO CART
    # ============================================================

    def add_product_to_cart(self):

        print(
            "Adding product to cart..."
        )

        # Verify the quantity before clicking Add to Cart
        quantity_input = self.wait.until(
            EC.visibility_of_element_located(
                self.QUANTITY_INPUT
            )
        )

        quantity_before_cart = quantity_input.get_attribute(
            "value"
        )

        print(
            f"Quantity before Add to Cart: "
            f"{quantity_before_cart}"
        )

        add_to_cart = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_to_cart
        )

        add_to_cart.click()

        # Wait for cart popup
        self.wait.until(
            EC.visibility_of_element_located(
                self.CART_POPUP
            )
        )

        print(
            "Product added to cart."
        )

    # ============================================================
    # VIEW CART FROM POPUP
    # ============================================================

    def view_cart_from_popup(self):

        print(
            "Opening cart from popup..."
        )

        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_CART_LINK
            )
        )

        cart_link.click()

        self.wait.until(
            EC.url_contains(
                "/view_cart"
            )
        )

        print(
            f"Cart URL: {self.driver.current_url}"
        )
