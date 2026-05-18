# BookShelf

A Django book catalog with a full REST API. Built to learn Django fundamentals from the ground up — models, views, templates, forms, authentication, and DRF — in the context of a content-driven publishing site.

## Stack

- **Backend:** Python 3.14, Django 6.0
- **API:** Django REST Framework 3.17
- **Database:** SQLite (dev)
- **Frontend:** Django templates + a small amount of inline CSS

## Features

- Public book catalog with search, list view, and per-book detail pages
- Django admin for editorial content management (authors, categories, books)
- Authenticated "Add a Book" form for staff
- REST API at `/api/books/` with read-only public access and write access for authenticated users
- Browsable API via DRF for easy testing

## Architecture Notes

**Why two view layers (HTML and API)?** The HTML views serve a public reader audience; the API exposes the same data as JSON so other systems (a mobile app, a partner site, a search index) can consume it. Both share the same models — single source of truth.

**Why both function-based and class-based views?** Function-based views (`book_list`, `book_detail`, `book_create`) make the request/response cycle explicit and were useful for learning. Class-based views (`BookCreateView`, the DRF generic views) cut boilerplate once the pattern is standard.

**Performance.** The list view uses `select_related("author")` and `prefetch_related("categories")` to avoid N+1 queries — a 50-book page renders in 2 SQL queries instead of 151.

**Security.** All POST forms include `{% csrf_token %}`. The API uses `IsAuthenticatedOrReadOnly` so anonymous users can read but not write.

## Running locally

```bash
git clone https://github.com/ashdean22/bookshelf-django.git
cd bookshelf-django
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/books/` for the catalog or `http://127.0.0.1:8000/api/books/` for the API.

## What I'd do next

- **Object-level permissions** on the API — only the user who added a book can edit it.
- **Pagination** on the list view and API — currently returns all books in one response.
- **Tests** — pytest + pytest-django covering models, views, and API endpoints.
- **PostgreSQL** in production, with environment-based settings via `django-environ`.
- **A "reading list" feature** — a `UserBook` join model linking users to books with a status (want-to-read, reading, finished).
