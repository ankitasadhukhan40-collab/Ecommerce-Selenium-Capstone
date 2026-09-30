import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader
from utils.screenshot import Screenshot


@pytest.fixture
def driver():

    config = ConfigReader.load_config()

    options = Options()

    options.add_argument(
        "--start-maximized"
    )

    options.add_argument(
        "--disable-notifications"
    )

    options.add_argument(
        "--disable-popup-blocking"
    )

    driver = webdriver.Chrome(
        options=options
    )

    driver.get(
        config["base_url"]
    )

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get(
            "driver"
        )

        if driver:

            Screenshot.capture(
                driver,
                f"FAILED_{item.name}"
            )
