# lift equipment-scrapper
- This script will scrape data from various websites that contain information about lifting equipment, muscles being targetted, company, etc... It will then be stored in a database that will be available of use by an API - Github here: [Not available yet].

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

- `Scrappers/`: Contains the 3 websites used to obtain all the information about general machines, cables, and exercises.
- `main.py`: The main script to show the output of the database made from the webscrappers.
- `database.py`: Initializes database and handles the information from the scrappers.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: Provides an overview of the project and instructions for setup and usage.

## Structure of the Database

- Excercise
-   `Name`
-   `Type (Free/Machine/Cable)`
-   `Category (Stength/Cardio/Calisthenics)`
-   `Muscle (targeted muscle)`
    