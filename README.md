# Vehicle Identifier and Quote Generator

This Django project allows users to upload a picture of a vehicle, identify the type of vehicle using Azure Custom Vision, and calculate an appropriate insurance premium. The project also includes functionality to search for quotes using a reference number stored on an Azure MySQL database.

## Features

- Upload a vehicle image and identify the vehicle type using Azure Custom Vision.
- Calculate and display a randomly generated insurance price.
- Store user details (age and city) and display them along with the insurance quote.
- Search for quotes using a reference number.
- Deployable on Microsoft Azure with Azure MySQL database.

## Requirements

- Python 3.8+
- Django 3.2+
- MySQL
- Azure Custom Vision

## Installation

1. **Clone the repository**:
    git clone link
    cd vehicle-identifier
    
2. **Create a virtual environment**:

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the dependencies**:

4. **Create a `.env` file in the project root and add the following environment variables**:

    ```env
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host.mysql.database.azure.com
    DB_PORT=3306
    SECRET_KEY=your_secret_key
    MYSQL_SSL_CA=/path/to/ca-certificate.crt  
    PREDICTION_KEY=your_prediction_key
    PREDICTION_ENDPOINT=your_prediction_endpoint
    PROJECT_ID=your_project_id
    ITERATION_NAME=your_iteration_name
    AZURE_ACCOUNT_NAME=your_account_name
    AZURE_ACCOUNT_KEY=your_account_key
    AZURE_CONTAINER=your_container_name
    ```
5. **Apply database migrations**:

    python manage.py makemigrations
    python manage.py migrate

6. **Create a superuser**:

    python manage.py createsuperuser

7. **Run the development server**:

    python manage.py runserver

## Usage

- **Home Page**: Upload a car image and enter user details (age and city).
- **Results Page**: Displays the identified vehicle type, user details, reference number, and insurance price.
- **Search Page**: Search for a quote using a reference number.
- **Reference Page**: Displays the info of the reference number entered into search
- **Quote Not Found**: Displays a message if the reference number is not found.
