# 🛒 E-Commerce Backend with FastAPI

![E-Commerce Backend](https://img.shields.io/badge/ecommerce--backend--fastapi-v1.0-blue.svg)
![API Documentation](https://img.shields.io/badge/api%20documentation-OpenAPI%20%2F%20Swagger-orange.svg)

Welcome to the **ecommerce-backend-fastapi** repository! This project showcases a modern, high-performance e-commerce REST API built with FastAPI. It features user authentication, product management, shopping cart functionality, and order processing, all with automatic API documentation.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Getting Started](#getting-started)
4. [API Documentation](#api-documentation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)
9. [Releases](#releases)

## Features

- **User Authentication**: Secure login and registration using JWT and OAuth2.
- **Product Management**: Add, update, and delete products easily.
- **Shopping Cart**: Users can manage their cart with a simple interface.
- **Order Processing**: Handle orders seamlessly from cart to checkout.
- **Automatic API Documentation**: Access interactive API docs via Swagger UI.

## Technologies Used

This project leverages a range of powerful technologies to deliver a robust e-commerce solution:

- **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **JWT Authentication**: Secure token-based authentication.
- **OAuth2**: Standard for access delegation, used for secure API access.
- **Swagger UI**: A tool for documenting APIs, providing a user-friendly interface.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- A PostgreSQL database or any other database of your choice

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Abudyx15YT/ecommerce-backend-fastapi.git
   cd ecommerce-backend-fastapi
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your database settings in the `.env` file.

5. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

Your e-commerce API should now be running at `http://127.0.0.1:8000`.

## API Documentation

To explore the API, visit the automatic documentation provided by Swagger UI at:

```
http://127.0.0.1:8000/docs
```

This interface allows you to test all endpoints and see how the API functions in real-time.

## Usage

Once your API is running, you can perform various operations:

### User Authentication

- **Register**: Create a new user account.
- **Login**: Authenticate and receive a JWT token for secure access.

### Product Management

- **Create Product**: Add a new product to the catalog.
- **Update Product**: Modify existing product details.
- **Delete Product**: Remove a product from the catalog.

### Shopping Cart

- **Add to Cart**: Include products in your shopping cart.
- **Remove from Cart**: Delete products from your cart.
- **View Cart**: Check the contents of your shopping cart.

### Order Processing

- **Checkout**: Complete the purchase process.
- **View Orders**: See past orders and their statuses.

## Contributing

We welcome contributions to enhance this project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Submit a pull request.

Please ensure that your code follows the project's coding standards and includes tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, feel free to reach out:

- **Author**: [Your Name](mailto:your.email@example.com)
- **GitHub**: [Abudyx15YT](https://github.com/Abudyx15YT)

## Releases

To download the latest release, visit [Releases](https://github.com/Abudyx15YT/ecommerce-backend-fastapi/releases). Make sure to download and execute the necessary files for your environment.

---

This README provides a comprehensive overview of the **ecommerce-backend-fastapi** project. Feel free to explore the code, contribute, and build your own e-commerce solutions using FastAPI!