from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader


# Read configuration
config = ConfigReader.load_config()

# Chrome settings
options = Options()
options.add_argument("--start-maximized")

# Start Chrome
driver = webdriver.Chrome(
    options=options
)

# Open website
driver.get(
    config["base_url"]
)

print("Website opened successfully!")
print("Current URL:", driver.current_url)

# Keep browser open
input("Press ENTER to close the browser...")

# Close browser
driver.quit()
