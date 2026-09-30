from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoAlertPresentException


class BasePage:

    def __init__(self, driver, timeout=15):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            timeout
        )

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def type_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def is_visible(self, locator):

        try:

            self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except Exception:

            return False

    def wait_for_element(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def handle_alert(self, accept=True):

        try:

            alert = self.driver.switch_to.alert

            print(
                f"Alert detected: {alert.text}"
            )

            if accept:
                alert.accept()
            else:
                alert.dismiss()

            return True

        except NoAlertPresentException:

            return False
