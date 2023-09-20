# Django Email Subscription Service

## Introduction

This Email Subscription Service is a web application that allows users to subscribe to various services using their email addresses. It provides a RESTful API for managing subscriptions.

## Features

- User subscription to services.
- Validation to prevent duplicate subscriptions with the same email and service.
- RESTful API for creating and managing subscriptions.

## Technologies Used

- Django 4.2
- Django Rest Framework 3.14
- Python 3.8
- SQLite (default database)
- Django Cors 4.2
- Django Environ 0.11
- Psycopg2 2.9.7

## Setup

To set up and run this Django project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/programmerizak/coming_soon_backend.git

   cd coming_soon_backend/

   pip install -r requirements.txt

   python manage.py makemigrations

   python manage.py migrate
   

