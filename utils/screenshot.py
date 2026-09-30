import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, name):
        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        screenshot_folder = os.path.join(
            project_root,
            "screenshots"
        )

        os.makedirs(screenshot_folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{name}_{timestamp}.png"

        path = os.path.join(
            screenshot_folder,
            filename
        )

        driver.save_screenshot(path)

        print(f"Screenshot saved: {path}")

        return path
