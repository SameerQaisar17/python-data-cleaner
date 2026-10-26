import csv

input_file = "customers.csv"
output_file = "cleaned_customers.csv"

cleaned_customers = []
seen_customers = set()

duplicate_count = 0
incomplete_count = 0
original_count = 0

try:
    with open(input_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_columns = {"Name", "Email"}

        if not required_columns.issubset(reader.fieldnames or []):
            print("Error: The CSV must contain Name and Email columns.")

        else:
            for row in reader:
                original_count += 1

                name = (row.get("Name") or "").strip()
                email = (row.get("Email") or "").strip().lower()

                # Skip records with missing information
                if not name or not email:
                    incomplete_count += 1
                    continue

                # Create a unique customer identifier
                customer = (name.lower(), email)

                # Skip duplicate records
                if customer in seen_customers:
                    duplicate_count += 1
                    continue

                seen_customers.add(customer)

                cleaned_customers.append({
                    "Name": name,
                    "Email": email
                })

            with open(
                output_file, "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file, fieldnames=["Name", "Email"]
                )
                writer.writeheader()
                writer.writerows(cleaned_customers)

            print("\n===== DATA CLEANING REPORT =====")
            print("Original records:", original_count)
            print("Duplicate records removed:", duplicate_count)
            print("Incomplete records removed:", incomplete_count)
            print("Cleaned records:", len(cleaned_customers))
            print("Output file:", output_file)
            print("Data cleaning completed successfully!")

except FileNotFoundError:
    print("Error: customers.csv was not found.")
    print("Place the CSV file in the same folder as this script.")

except PermissionError:
    print("Error: Unable to access a file.")
    print("Close the CSV files in other programs and try again.")