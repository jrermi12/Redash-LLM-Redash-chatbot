# Imports for pandas, sqlalchemy, etc.
import pandas as pd
from sqlalchemy import create_engine


# Function to load data from CSV to Postgres (replace with your actual credentials)
def load_csv_to_postgres(csv_path, schema_name, table_name):
    DATABASE_URL = (
        "postgresql://postgres:54321@localhost:5432/youtube_data"  # Replace with your database connection details
    )
    engine = create_engine(DATABASE_URL)

    try:
        # Read CSV file
        df = pd.read_csv(csv_path)

        # Load data using SQLAlchemy
        with engine.connect() as connection:
            df.to_sql(table_name, connection, schema=schema_name, if_exists="replace", index=False)

        print(f"Data from '{csv_path}' loaded successfully.")

    except Exception as error:
        print(f"Error loading data: {error}")


# Define your CSV file paths, schema names, and table names
csv_files = [
    ("/home/mart/trial/youtube-data/viewer age/viewer_age_table data.csv", "youtube_data", "viewer_age_table"),
    # ... other CSV details ...
]

# Load data from each CSV file
for csv_file, schema_name, table_name in csv_files:
    load_csv_to_postgres(csv_file, schema_name, table_name)

print("All data loaded successfully!")
