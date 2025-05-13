# ALX Travel App

A Django-based travel listing platform with RESTful API endpoints.

## Features

- Travel listings management
- RESTful API with Swagger documentation
- MySQL database integration
- CORS support for cross-origin requests
- Celery task queue integration

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/alx_travel_app.git
   cd alx_travel_app
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r alx_travel_app/requirement.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the project root with the following variables:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=mysql://user:password@localhost:3306/alx_travel_app
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## API Documentation

API documentation is available at:
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## License

This project is licensed under the MIT License. 