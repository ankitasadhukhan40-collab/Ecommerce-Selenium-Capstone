from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class HomePage(BasePage):
    PRODUCTS_LINK = (
        By.XPATH,
        "//a[@href='/products' and contains(normalize-space(), 'Products')]"
    )

    PRODUCTS_URL = "https://automationexercise.com/products"

    def open_products(self):

        print("Opening Products page...")

        try:

            # ------------------------------------------------
            # Try normal Products link first
            # ------------------------------------------------

            products_link = self.wait.until(
                EC.presence_of_element_located(
                    self.PRODUCTS_LINK
                )
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                products_link
            )

            try:

                self.wait.until(
                    EC.element_to_be_clickable(
                        self.PRODUCTS_LINK
                    )
                )

                products_link.click()

            except Exception:

                print(
                    "Normal Products click intercepted. "
                    "Using JavaScript click."
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    products_link
                )

            # ------------------------------------------------
            # Wait briefly for normal navigation
            # ------------------------------------------------

            try:

                WebDriverWait(
                    self.driver,
                    5
                ).until(
                    lambda driver:
                    "/products" in driver.current_url.lower()
                )

            except Exception:

                print(
                    "Products navigation did not complete. "
                    "Opening Products URL directly."
                )

                self.driver.get(
                    self.PRODUCTS_URL
                )

        except Exception:

            # ------------------------------------------------
            # Final fallback
            # ------------------------------------------------

            print(
                "Products link could not be used. "
                "Opening Products URL directly."
            )

            self.driver.get(
                self.PRODUCTS_URL
            )

        # ----------------------------------------------------
        # Final verification
        # ----------------------------------------------------

        self.wait.until(
            lambda driver:
            "/products" in driver.current_url.lower()
        )

        print(
            f"Products page URL: "
            f"{self.driver.current_url}"
        )