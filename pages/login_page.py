from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)


class LoginPage:

    # =========================================================
    # LOCATORS
    # =========================================================

    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a[href='/login']"
    )

    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "input[data-qa='login-email']"
    )

    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "input[data-qa='login-password']"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-qa='login-button']"
    )

    LOGGED_IN_USER = (
        By.CSS_SELECTOR,
        "a[href='/logout']"
    )

    # =========================================================
    # CONSTRUCTOR
    # =========================================================

    def __init__(self, driver, timeout=10):

        self.driver = driver
        self.timeout = timeout

        self.wait = WebDriverWait(
            self.driver,
            self.timeout
        )

    # =========================================================
    # OPEN LOGIN PAGE
    # =========================================================

    def open_login(self):

        print(
            "Opening Login page..."
        )

        # -----------------------------------------------------
        # Already on login page
        # -----------------------------------------------------

        if "/login" in self.driver.current_url.lower():

            print(
                "Already on Login page."
            )

            return

        # -----------------------------------------------------
        # Locate login link
        # -----------------------------------------------------

        try:

            login_link = self.wait.until(
                EC.presence_of_element_located(
                    self.LOGIN_LINK
                )
            )

            # Scroll login link into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                login_link
            )

            # -------------------------------------------------
            # Normal click
            # -------------------------------------------------

            try:

                self.wait.until(
                    EC.element_to_be_clickable(
                        self.LOGIN_LINK
                    )
                ).click()

            except ElementClickInterceptedException:

                print(
                    "Login click intercepted. "
                    "Using JavaScript click..."
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    login_link
                )

            # -------------------------------------------------
            # Wait for login URL
            # -------------------------------------------------

            try:

                self.wait.until(
                    EC.url_contains(
                        "/login"
                    )
                )

            except TimeoutException:

                print(
                    "Login navigation did not complete. "
                    "Opening /login directly..."
                )

                self.driver.get(
                    "https://automationexercise.com/login"
                )

        except TimeoutException:

            print(
                "Login link could not be located. "
                "Opening /login directly..."
            )

            self.driver.get(
                "https://automationexercise.com/login"
            )

        # -----------------------------------------------------
        # Verify login page loaded
        # -----------------------------------------------------

        self.wait.until(
            EC.presence_of_element_located(
                self.EMAIL_INPUT
            )
        )

        print(
            f"Login page URL: {self.driver.current_url}"
        )

    # =========================================================
    # LOGIN
    # =========================================================

    def login(self, email, password):

        print(
            f"Login email: {email}"
        )

        # -----------------------------------------------------
        # EMAIL
        # -----------------------------------------------------

        email_input = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL_INPUT
            )
        )

        email_input.clear()

        email_input.send_keys(
            email
        )

        # -----------------------------------------------------
        # PASSWORD
        # -----------------------------------------------------

        password_input = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD_INPUT
            )
        )

        password_input.clear()

        password_input.send_keys(
            password
        )

        # -----------------------------------------------------
        # LOGIN BUTTON
        # -----------------------------------------------------

        login_button = self.wait.until(
            EC.presence_of_element_located(
                self.LOGIN_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            login_button
        )

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.LOGIN_BUTTON
                )
            ).click()

        except ElementClickInterceptedException:

            print(
                "Login button click intercepted. "
                "Using JavaScript click..."
            )

            self.driver.execute_script(
                "arguments[0].click();",
                login_button
            )

        # -----------------------------------------------------
        # WAIT FOR LOGIN COMPLETION
        # -----------------------------------------------------

        self.wait.until(
            EC.presence_of_element_located(
                self.LOGGED_IN_USER
            )
        )

        print(
            "Login submitted successfully."
        )

    # =========================================================
    # VERIFY LOGIN
    # =========================================================

    def verify_login(self):

        try:

            self.wait.until(
                EC.presence_of_element_located(
                    self.LOGGED_IN_USER
                )
            )

            print(
                "Login verification successful."
            )

            return True

        except TimeoutException:

            print(
                "Login verification failed."
            )

            return False
