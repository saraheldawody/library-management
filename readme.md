# Library Management System

## Overview

This is a **Django Rest Framework (DRF)** application designed to manage a library system. The system includes features to manage books, authors, and borrowing processes. Users can borrow and return books, while administrators can manage the library catalog.

---

## Features

### 1. **User Management**
- User registration with email and password confirmation.
- JWT-based authentication for secure access.
- Separate permissions for admin users and normal users:
  - Admins can create, update, and delete books and authors.
  - Users can borrow and return books.

### 2. **Library Management**
- CRUD operations for:
  - Authors.
  - Books.
- Search and filter functionality for books by:
  - Title (search).
  - Author (filter).

### 3. **Borrowing System**
- Users can:
  - Borrow a book (if available).
  - Return a borrowed book.
  - View the list of books they have borrowed.
- Automatic handling of book availability:
  - Decrement available copies when a book is borrowed.
  - Increment available copies when a book is returned.

---

## API Endpoints

### Authentication
- `POST /user/register/`  
  Register a new user.  
  **Required fields:** `username`, `email`, `password`, `confirm_password`.

- `POST /token/`  
  Obtain JWT tokens (access and refresh).

- `POST /token/refresh/`  
  Refresh an expired access token.

---

### Library
- `GET /library/authors/`  
  List all authors.

- `POST /library/authors/`  
  Create a new author (Admin only).

- `GET /library/books/`  
  List all books with optional search and filtering.

- `POST /library/books/`  
  Add a new book (Admin only).

- `POST /library/borrow/`  
  Borrow a book.

- `POST /library/return/<book_id>/`  
  Return a borrowed book.

- `GET /library/borrowed/`  
  List all books borrowed by the logged-in user.

---

## Installation

### Prerequisites
- Python 3.9+
- Django 5.x
- SQLite (default database)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-management.git
   cd library-management
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run database migrations:
    ```bash
    python manage.py migrate
    ```
4. Create a superuser (for admin access):
    ```bash
    python manage.py createsuperuser
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
6. Access the admin panel:
    ```arduino
    http://127.0.0.1:8000/admin/
    ```
### Usage
1. Register as a user or log in using the admin credentials.
2. Use the endpoints to manage authors and books.
3. Borrow and return books using authenticated endpoints.
4. Admin users can manage the catalog via the admin panel or APIs.

### Project Structure
```graphql
library_management/
├── library/                # Library app for books, authors, and borrowing
│   ├── models.py           # Models for Author, Book, and Borrow
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # Viewsets and API views
│   ├── permissions.py      # Custom permissions
│   ├── admin.py            # Admin configurations
├── user/                   # User management app
│   ├── serializers.py      # User registration serializer
│   ├── views.py            # User registration API view
├── library_management/     # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
```

### Technologies Used
- Backend Framework: Django Rest Framework (DRF)
- Authentication: JWT (via rest_framework_simplejwt)
- Database: SQLite
- Pagination and Filters: DRF's built-in tools, Django Filters

### Future Enhancements
- Add notifications for overdue books.
- Implement fine calculation for late returns.
- Add a recommendation system for users based on borrowing history.

### License
This project is open-source and available under the MIT License.

### Author
Sarah

[GitHub](https://github.com/saraheldawody)

[LinkedIn](https://www.linkedin.com/in/saraheldawody/)

Feel free to contribute or report any issues! 😊