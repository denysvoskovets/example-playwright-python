# UI Playwright Python


## Project Overview

This project focuses on automating the testing process for the Automation https://www.automationexercise.com application. The tests cover key features of the app to ensure reliability and correct behavior. The structure of the project is designed according to best practices, making the test scripts clear, consistent, and easy to maintain.

## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/denysvoskovets/example-playwright-python.git
cd repo-name
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Additional Playwright Setup

If you're running Playwright for the first time, you might need to install the required browsers:

```bash
playwright install
```

### Additional .env setup
Create file with data.

```bash
APP_URL="https://www.automationexercise.com"
HEADLESS=true
BROWSERS=["chromium"]

TEST_USER.EMAIL=""    <- Create your account in the app
TEST_USER.USERNAME=""   <- Create your account in the app
TEST_USER.PASSWORD=""   <- Create your account in the app
```


### Running the Tests with Allure Report

```bash
pytest -m "regression" --alluredir=./allure-results
```

This will execute all tests in the project and display the results in the terminal.

### Viewing the Allure Report

After the tests have been executed, you can generate and view the Allure report with:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser.
