# **Shopping Cart API**

A backend API for managing an online shopping cart, built with Django and Django REST Framework. This API supports adding products, managing cart items, and performing CRUD operations on cart data.

---

## **Features**
- Add products to the shopping cart.
- Update the quantity of items in the cart.
- View all cart items.
- Remove items from the cart.
- RESTful API structure for seamless integration with frontend applications.

---

## **Technologies Used**
- **Backend Framework**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Hosting**: Railway (or any cloud platform)
- **Dependencies**:
  - `djangorestframework`: For building the REST API.
  - `dj-database-url`: For parsing database URLs in deployment.
  - `gunicorn`: For serving the application in production.

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed:
- Python (>=3.8)
- PostgreSQL
- Git

---

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/FrankDzikunu/shopping_cart_api.git
   cd shopping_cart_api
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Create a PostgreSQL database.
   - Add the connection details to `.env`:
     ```env
     DATABASE_URL=postgres://username:password@localhost:5432/dbname
     SECRET_KEY=your-secret-key
     DEBUG=True
     ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to test the API locally.

---

### **API Endpoints**
| Method | Endpoint              | Description                |
|--------|-----------------------|----------------------------|
| GET    | `/api/products/`      | List all products.         |
| POST   | `/api/cart/`          | Add an item to the cart.   |
| GET    | `/api/cart/`          | View all cart items.       |
| PATCH  | `/api/cart/{id}/`     | Update a cart item.        |
| DELETE | `/api/cart/{id}/`     | Remove an item from the cart. |

---

## **Deployment**

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


## **Testing**

Run the test suite with:
```bash
python manage.py test
```

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

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

---



---

## **Contact**
For questions or inquiries, reach out to:
- **Frank Dzikunu**  
  Email: fdzikunu@stu.ucc.edu.gh  
  GitHub: [Frank Dzikunu](https://github.com/FrankDzikunu)

--- 
