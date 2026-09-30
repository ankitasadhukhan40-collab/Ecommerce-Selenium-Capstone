import csv


class CSVReader:

    @staticmethod
    def get_first_record(file_path):

        with open(
            file_path,
            mode="r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            # Check headers
            if reader.fieldnames is None:
                raise ValueError(
                    "CSV file does not contain headers."
                )

            # Clean headers
            reader.fieldnames = [
                header.strip().lower()
                for header in reader.fieldnames
            ]

            print("Headers:", reader.fieldnames)

            # Read first record
            row = next(reader, None)

            if row is None:
                raise ValueError(
                    "CSV file does not contain any data."
                )

            # Check for extra columns
            if None in row:
                raise ValueError(
                    "CSV contains extra values.\n"
                    f"Extra values: {row[None]}"
                )

            # Clean row
            cleaned_row = {}

            for key, value in row.items():

                if key is None:
                    continue

                clean_key = key.strip().lower()

                clean_value = (
                    value.strip()
                    if value is not None
                    else ""
                )

                cleaned_row[clean_key] = clean_value

            # Required columns
            required_columns = [
                "test_case",
                "username",
                "email",
                "password",
                "search_product",
                "quantity"
            ]

            missing_columns = [
                column
                for column in required_columns
                if column not in cleaned_row
            ]

            if missing_columns:
                raise ValueError(
                    "Missing CSV columns: "
                    + ", ".join(missing_columns)
                )

            return cleaned_row

