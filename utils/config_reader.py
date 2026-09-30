import json
import os


class ConfigReader:

    @staticmethod
    def load_config():

        # Get the project root directory
        project_root = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        # Build the configuration file path
        config_path = os.path.join(
            project_root,
            "config",
            "config.json"
        )

        print(f"\nReading configuration from:")
        print(config_path)

        # Check if configuration file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(
                f"\nConfig file not found!\n"
                f"Expected location:\n{config_path}"
            )

        # Read JSON configuration
        with open(
            config_path,
            "r",
            encoding="utf-8"
        ) as file:

            config = json.load(file)

        return config

