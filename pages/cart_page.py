from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CartPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ============================================================
    # LOCATORS
    # ============================================================

    CART_TABLE = (
        By.ID,
        "cart_info_table"
    )

    CART_ROWS = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr"
    )

    PRODUCT_ROW = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr"
    )

    QUANTITY_BUTTON = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr .cart_quantity button"
    )

    DELETE_BUTTON = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr .cart_delete a"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr .cart_description h4 a"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr .cart_price p"
    )

    PRODUCT_TOTAL = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr .cart_total_price"
    )

    # ============================================================
    # VERIFY CART DISPLAYED
    # ============================================================

    def verify_cart_displayed(self):

        try:

            self.wait.until(
                EC.url_contains("/view_cart")
            )

            self.wait.until(
                EC.presence_of_element_located(
                    self.CART_TABLE
                )
            )

            return True

        except TimeoutException:

            return False

    # ============================================================
    # CLEAR CART
    # ============================================================

    def clear_cart(self):

        print("Checking for existing cart items...")

        # Open cart directly
        self.driver.get(
            "https://automationexercise.com/view_cart"
        )

        self.wait.until(
            EC.url_contains("/view_cart")
        )

        try:

            rows = self.driver.find_elements(
                *self.CART_ROWS
            )

            product_rows = []

            for row in rows:

                try:

                    product_name = row.find_element(
                        By.CSS_SELECTOR,
                        ".cart_description h4 a"
                    ).text.strip()

                    if product_name:
                        product_rows.append(row)

                except Exception:
                    continue

            if not product_rows:

                print("Cart is already empty.")
                return

            print(
                f"Existing cart products: "
                f"{len(product_rows)}"
            )

            # Delete products one at a time
            while True:

                rows = self.driver.find_elements(
                    *self.CART_ROWS
                )

                product_row_found = False

                for row in rows:

                    try:

                        product_name = row.find_element(
                            By.CSS_SELECTOR,
                            ".cart_description h4 a"
                        ).text.strip()

                        if not product_name:
                            continue

                        product_row_found = True

                        print(
                            f"Removing existing product: "
                            f"{product_name}"
                        )

                        delete_button = row.find_element(
                            By.CSS_SELECTOR,
                            ".cart_delete a"
                        )

                        self.driver.execute_script(
                            "arguments[0].click();",
                            delete_button
                        )

                        # Wait until this row disappears
                        self.wait.until(
                            EC.staleness_of(row)
                        )

                        break

                    except Exception:
                        continue

                if not product_row_found:
                    break

            print("Cart cleared successfully.")

        except Exception as e:

            print(
                f"Cart clearing completed with message: {e}"
            )

    # ============================================================
    # GET CART PRODUCT COUNT
    # ============================================================

    def get_cart_product_count(self):

        try:

            rows = self.wait.until(
                EC.presence_of_all_elements_located(
                    self.CART_ROWS
                )
            )

            product_rows = []

            for row in rows:

                try:

                    product_name = row.find_element(
                        By.CSS_SELECTOR,
                        ".cart_description h4 a"
                    )

                    if product_name.text.strip():
                        product_rows.append(row)

                except Exception as e:

                    print(
                        f"Skipping non-product cart row: {e}"
                    )

            print(
                f"Cart rows found: {len(product_rows)}"
            )

            return len(product_rows)

        except TimeoutException:

            print(
                "No product rows found in cart."
            )

            return 0

    # ============================================================
    # GET QUANTITY
    # ============================================================

    def get_quantity(self):

        rows = self.wait.until(
            EC.presence_of_all_elements_located(
                self.CART_ROWS
            )
        )

        for row in rows:

            try:

                product_name = row.find_element(
                    By.CSS_SELECTOR,
                    ".cart_description h4 a"
                ).text.strip()

                if not product_name:
                    continue

                quantity_element = row.find_element(
                    By.CSS_SELECTOR,
                    ".cart_quantity button"
                )

                quantity = quantity_element.get_attribute(
                    "textContent"
                ).strip()

                print(
                    f"Product: {product_name}"
                )

                print(
                    f"Quantity element tag: "
                    f"{quantity_element.tag_name}"
                )

                print(
                    f"Quantity element text: "
                    f"{quantity_element.text!r}"
                )

                print(
                    f"Quantity element textContent: "
                    f"{quantity!r}"
                )

                print(
                    "Quantity element outerHTML: "
                    f"{quantity_element.get_attribute('outerHTML')}"
                )

                return quantity

            except Exception as e:

                print(
                    f"Unable to read quantity "
                    f"from cart row: {e}"
                )

        raise AssertionError(
            "Quantity field not found in cart."
        )

    # ============================================================
    # GET PRODUCT DETAILS
    # ============================================================

    def get_product_details(self):

        rows = self.wait.until(
            EC.presence_of_all_elements_located(
                self.CART_ROWS
            )
        )

        details = []

        for row in rows:

            try:

                name = row.find_element(
                    By.CSS_SELECTOR,
                    ".cart_description h4 a"
                ).text.strip()

                if not name:
                    continue

                price = row.find_element(
                    By.CSS_SELECTOR,
                    ".cart_price p"
                ).text.strip()

                quantity = row.find_element(
                    By.CSS_SELECTOR,
                    ".cart_quantity button"
                ).get_attribute(
                    "textContent"
                ).strip()

                total = row.find_element(
                    By.CSS_SELECTOR,
                    ".cart_total_price"
                ).text.strip()

                details.append(
                    f"Product  : {name}\n"
                    f"Price    : {price}\n"
                    f"Quantity : {quantity}\n"
                    f"Total    : {total}"
                )

            except Exception as e:

                print(
                    f"Unable to read product details: {e}"
                )

        return details
