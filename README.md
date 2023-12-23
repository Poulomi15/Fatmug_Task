# Fatmug_Task
# Vendor Management System

The Vendor Management System is a Django-based application designed to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Table of Contents

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Database Setup](#database-setup)
- [Configuration](#configuration)
- [How to Run the Project Locally](#how-to-run-the-project-locally)
- [API Endpoints](#api-endpoints)
- [Performance Metrics](#performance-metrics)
- [Additional Information](#additional-information)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Poulomi15/Fatmug_Task.git
   cd vendor-management-system
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Dependencies
Django
Django REST Framework
(Add any other dependencies)
Database Setup
Configure your database settings in settings.py.
Apply migrations to create database tables:
bash
Copy code
python manage.py migrate
Configuration
Update configuration settings in settings.py as needed.

How to Run the Project Locally
Run the development server:

bash
Copy code
python manage.py runserver
Access the API at: http://localhost:8000/api/

API Endpoints
POST /api/vendors/
Create a new vendor.

Request:
json
Copy code
{
  "name": "Vendor ABC",
  "contact_details": "Contact info",
  "address": "Vendor address",
  "vendor_code": "ABC123"
}
Response:
json
Copy code
{
  "id": 1,
  "name": "Vendor ABC",
  "contact_details": "Contact info",
  "address": "Vendor address",
  "vendor_code": "ABC123",
  "on_time_delivery_rate": 0.0,
  "quality_rating_avg": 0.0,
  "average_response_time": 0.0,
  "fulfillment_rate": 0.0
}
(Repeat this structure for each API endpoint)

Performance Metrics
On-Time Delivery Rate
Calculated each time a PO status changes to 'completed'.
Logic: Count the number of completed POs delivered on or before delivery_date and divide by the total number of completed POs for that vendor.
Quality Rating Average
Updated upon the completion of each PO where a quality_rating is provided.
Logic: Calculate the average of all quality_rating values for completed POs of the vendor.
(Repeat this structure for other metrics)
