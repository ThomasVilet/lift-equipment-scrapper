# lift equipment-scrapper
- This script will scrape data from various websites that contain information about lifting equipment, muscles being targetted, company, etc... It will then be stored in a database that will be available of use by an API - Github here: [].

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the scraper:
    ```bash
    python main.py
    ```

## Directory Structure

- `data/`: Contains the SQLite database file.
- `scrapers/`: Contains the individual scraper modules for each brand.
- `main.py`: The main script to run the web scraping process.
- `database.py`: Handles the database connection and schema creation.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: Provides an overview of the project and instructions for setup and usage.

## Structure of the Database

- Excercise
-   Name
-   Type (Free/Machine/Cable)
-   Category (Stength/Cardio/Calisthenics)
-   Muscle (targeted muscle)
    