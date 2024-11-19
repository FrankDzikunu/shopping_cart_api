# **Shopping Cart API**

A backend API for managing an online shopping cart, built with Django and Django REST Framework. This API supports adding products, managing cart items, and performing CRUD operations on cart data.

---

## Overview
The **Shopping Cart API** is a RESTful API designed to manage products and shopping cart functionality for an e-commerce application. It allows users to browse products, add them to the shopping cart, and manage the cart items. The API is built using Django and Django REST Framework (DRF), with OpenAPI documentation (Swagger and ReDoc) for easy exploration.

---

## Features
- **Product Management**: View, create, update, and delete products.
- **Cart Management**: Add, update, or remove items in the shopping cart.
- **Product Filtering**: Filter products by category, price range, and availability.
- **Stock Management**: Track the availability of products in the cart.
- **Authentication & Permissions**: Secure access control for product management.
- **API Documentation**: Swagger and ReDoc for easy API exploration and testing.

---

## Technologies
- **Backend Framework**: Django (v5.1)
- **API Framework**: Django REST Framework (DRF)
- **API Documentation**: Swagger & ReDoc via `drf-yasg`
- **Database**: SQLite (for development; can be changed to PostgreSQL, MySQL, etc., for production)
- **Static Files**: WhiteNoise (for serving static files in production)

---

## **Project Structure**
```
shopping_cart_api/
│
├── cart/
│   ├── models.py       # Cart models
│   ├── serializers.py  # Cart serializers
│   ├── views.py        # Cart views
│   └── tests.py        # Unit tests
│
├── products/
│   ├── models.py       # Product models
│   ├── serializers.py  # Product serializers
│   ├── views.py        # Product views
│   └── tests.py        # Unit tests
│
├── shopping_cart_api/
│   ├── settings.py     # Django settings
│   ├── urls.py         # URL routing
│   └── wsgi.py         # WSGI entry point
│
├── requirements.txt    # Python dependencies
├── manage.py           # Django management script
└── README.md           # Project documentation
```

---

## Installation

### Prerequisites
- Python 3.8+
- Django 5.1+
- Django REST Framework
- `drf-yasg` for API documentation
- SQLite (or another preferred database for production)

### Steps to Set Up

1. **Clone the Repository**
   Clone the repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/shopping-cart-api.git
   cd shopping-cart-api
   ```

2. **Create a Virtual Environment**
   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required dependencies using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` should include:

   ```plaintext
   Django==5.1
   djangorestframework==3.14
   drf-yasg==1.21.5
   whitenoise==6.2
   ```

4. **Database Setup**
   Set up the database (SQLite by default) by running Django’s migration commands.

   ```bash
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**
   If you want to access the Django admin interface, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the admin account.

6. **Run the Development Server**

   Start the development server to begin using the API.

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at `http://127.0.0.1:8000/`.

---

## API Endpoints

### 1. **Products**

- **GET** `/api/products/`: List all products.
- **POST** `/api/products/`: Create a new product (admin only).
- **GET** `/api/products/{id}/`: Retrieve a specific product.
- **PUT** `/api/products/{id}/`: Update a specific product (admin only).
- **DELETE** `/api/products/{id}/`: Delete a specific product (admin only).

#### Filters (GET `/api/products/`):
- `category`: Filter by category (e.g., `category=electronics`).
- `min_price`: Filter by minimum price (e.g., `min_price=10.00`).
- `max_price`: Filter by maximum price (e.g., `max_price=100.00`).

### 2. **Cart Items**

- **GET** `/api/cart/`: List all items in the cart.
- **POST** `/api/cart/`: Add a product to the cart or update the quantity if it already exists.
- **PUT** `/api/cart/{id}/`: Update the quantity of a cart item.
- **DELETE** `/api/cart/{id}/`: Remove an item from the cart.

### 3. **API Documentation**

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

These links provide interactive API documentation where you can test the endpoints directly.

---

## Permissions & Authentication

### Product Management
- **POST**, **PUT**, and **DELETE** endpoints for products are restricted to **admin users** only.
- **GET** endpoints for products are accessible to everyone.

### Cart Management
- All users can add products to their cart and update/remove cart items.
- Cart operations are not restricted by user role (no authentication required for cart-related actions).

---

## Example Requests

### 1. **Get List of Products**
   ```bash
   GET /api/products/
   ```

   Response:
   ```json
   [
     {
       "id": 1,
       "name": "Product A",
       "category": "Electronics",
       "price": 29.99,
       "image_thumbnail": "http://example.com/thumbnail.jpg",
       "image_mobile": "http://example.com/mobile.jpg",
       "image_tablet": "http://example.com/tablet.jpg",
       "image_desktop": "http://example.com/desktop.jpg",
       "stock": 10,
       "description": "A great electronic product."
     }
   ]
   ```

### 2. **Add Product to Cart**
   ```bash
   POST /api/cart/
   {
     "product_id": 1,
     "quantity": 2
   }
   ```

   Response:
   ```json
   {
     "id": 1,
     "product": {
       "id": 1,
       "name": "Product A"
     },
     "quantity": 2
   }
   ```

### 3. **Remove Product from Cart**
   ```bash
   DELETE /api/cart/1/
   ```

   Response:
   ```json
   {
     "message": "Cart item removed successfully."
   }
   ```

---

## Testing the API

### Test Setup

To run the tests for this project, ensure that you have the correct environment set up and the database is migrated. Then, use the following command to run the test suite.

```bash
python manage.py test
```

The test suite covers:
- Adding and removing items from the cart.
- Viewing and filtering products.
- Validating permissions for creating, updating, and deleting products.

---

## Deployment

### Production Environment

1. **Set Up Environment Variables**: Ensure that sensitive data such as the Django secret key and database credentials are stored in environment variables (e.g., `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, etc.).

2. **Static Files**: Use WhiteNoise for serving static files in production. The static files will be collected into the `staticfiles` directory.

   ```bash
   python manage.py collectstatic
   ```

3. **Database**: In a production environment, it's recommended to use PostgreSQL or MySQL instead of SQLite. Update your `DATABASES` setting in `settings.py` to reflect the production database.

4. **Deploy to Render or Heroku**: You can deploy this application to platforms like [Render](https://render.com/) or [Heroku](https://heroku.com/).

---

## Deployment on Render

The project is deployed using [Render](https://render.com). Follow the steps below to deploy the application:

### Prerequisites
- A [Render account](https://render.com).
- The application must be pushed to a Git repository (e.g., GitHub, GitLab).

### Deployment Steps
1. **Connect Repository**  
   - Log in to your Render account.
   - Click on **New** > **Web Service**.
   - Connect your GitHub or GitLab repository to Render.
   - Select your repository containing the project.

2. **Configure Deployment Settings**  
   - Set **Environment** to `Python`.
   - Use the following **Build Command**:  
     ```bash
     pip install -r requirements.txt
     ```
   - Set the **Start Command**:  
     ```bash
     gunicorn shopping_cart_api.wsgi:application
     ```
   - Add your environment variables:
     - `DEBUG=False`
     - `DJANGO_SETTINGS_MODULE=shopping_cart_api.settings`
     - `ALLOWED_HOSTS=your-app-name.onrender.com`
     - `DATABASE_URL=your-database-url`

3. **Add Static File Configuration**  
   Render serves static files using **WhiteNoise**. Ensure you have the following configurations in your `settings.py`:
   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATIC_URL = '/static/'
   MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Add to MIDDLEWARE
   ```

4. **Database Setup**  
   - If using PostgreSQL, Render provides a managed PostgreSQL database. Add it from the **Dashboard** under **Add-ons**.
   - Update your `DATABASES` settings in `settings.py`:
     ```python
     import dj_database_url

     DATABASES = {
         'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
     }
     ```

5. **Deploy**  
   - Once the setup is complete, click on **Deploy**. Render will automatically build and deploy the application.

6. **Access the Application**  
   - After a successful deployment, your application will be accessible at `https://your-app-name.onrender.com`.

### Notes
- Ensure the `requirements.txt` includes all dependencies, especially `gunicorn` and `dj-database-url`.
- Static files should be collected using:
  ```bash
  python manage.py collectstatic
  ```

---

### **Deploy with Railway**
1. Install the Railway CLI:
   ```bash
   npm install -g railway
   ```
2. Log in:
   ```bash
   railway login
   ```
3. Initialize Railway project:
   ```bash
   railway init
   ```
4. Add PostgreSQL to your Railway project:
   ```bash
   railway add postgresql
   ```
5. Deploy the app:
   ```bash
   railway up
   ```

---


## Deploy link

`https://shopping-cart-api-won0.onrender.com`

---

## **Contact**
For questions or inquiries, reach out to:
- **Frank Dzikunu**  
  Email: fdzikunu@stu.ucc.edu.gh  
  GitHub: [Frank Dzikunu](https://github.com/FrankDzikunu)

--- 
