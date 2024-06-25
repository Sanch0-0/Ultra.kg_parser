# Ultra.kg Parser

This project is designed for parsing data from the Ultra.kg website and saving it into a database.

## Project Structure

The project consists of the following directories and files:

- `database/` - Directory for database operations
  - `__init__.py` - Initialization file for the `database` package
  - `connection.py` - File for establishing a connection to the database
  - `manager.py` - File for managing database operations

- `parsing/` - Directory for parsing data
  - `__init__.py` - Initialization file for the `parsing` package
  - `parsing.py` - File for executing data parsing

- `main.py` - Main file for running the parser
- `requirements.txt` - File containing the list of libraries required for the project
- `.env` - File for environment variables (not included in version control)
- `.env.example` - Example file for environment variables


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ultra-kg-parser.git
    cd ultra-kg-parser
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file by copying from `.env.example` and fill in the necessary environment variables:
    ```bash
    cp .env.example .env
    ```

## Usage

1. Ensure that your database is set up and running.

2. Run the parser:
    ```bash
    python main.py
    ```