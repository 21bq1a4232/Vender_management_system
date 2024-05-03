# Vendor Management System API

## Overview

This Django-based Vendor Management System API provides endpoints to manage vendors, purchase orders, and track performance metrics.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- Django REST framework

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/21bq1a4232/Vender_management_system.git
    ```

2. **Change directory:**

    ```bash
    cd venderSystem
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. ** To run this project Globally:
   run this command
    ```bash
    pip install --upgrade setuptools wheel
    ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Vendors

- **GET /api/vendors/:** List all vendors.
- **POST /api/vendors/:** Create a new vendor.
- **GET /api/vendors/{id}/:** Retrieve details of a specific vendor.
- **PUT /api/vendors/{id}/:** Update a vendor.
- **DELETE /api/vendors/{id}/:** Delete a vendor.

### Purchase Orders

- **GET /api/purchase_orders/:** List all purchase orders.
- **POST /api/purchase_orders/:** Create a new purchase order.
- **GET /api/purchase_orders/{id}/:** Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{id}/:** Update a purchase order.
- **DELETE /api/purchase_orders/{id}/:** Delete a purchase order.

### Vendor Performance

- **GET /api/vendors/{vendor_id}/performance/:** Retrieve performance metrics for a specific vendor.

### Acknowledge Purchase Order

- **POST /api/purchase_orders/{po_id}/acknowledge/:** Acknowledge a purchase order and update relevant metrics.

## Usage

Provide examples and details on how to use the API endpoints. Include sample requests and responses.

```json
Example POST request for creating a vendor:
{
    "name": "Daniel White",
    "contact_details": "7890123456",
    "address": "456 Oak Street",
    "vendor_code": "07",
    "on_time_delivery_rate": 92.5,
    "quality_rating_avg": 4.5,
    "average_response_time": 11.8,
    "fulfillment_rate": 96.2
}
OR
{
    "name": "Daniel White",
    "contact_details": "7890123456",
    "address": "456 Oak Street",
}

Example POST request for creating a purchase order:
{
    "po_number": "PO004",
    "vendor": 4,
    "order_date": "2023-12-18T14:00:00Z",
    "delivery_date": "2023-12-25T14:00:00Z",
    "items": [{"name": "Accessory C", "quantity": 8, "price": 18.0}],
    "quantity": 8,
    "status": "pending",
    "quality_rating": null,
    "issue_date": "2023-12-18T13:00:00Z",
    "acknowledgment_date": "2023-12-18T15:30:00Z"
}
```
## Contributing

Contributions to this project are welcome! Here's how you can contribute:

- **Issues:** Submit a bug report or feature request by creating a new issue in the GitHub issue tracker.
- **Code:** Fork the repository, make your changes, and submit a pull request. Make sure your code is clear, documented, and has been tested in the current environment.
- **Documentation:** Help improve the project's documentation, either by improving clarity, accuracy, or by adding new content.

Before contributing, please read through existing issues and pull requests to ensure that your issue or contribution hasn't already been addressed.

## License

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
