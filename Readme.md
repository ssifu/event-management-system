# Event Management System

## Overview

The Event Management System is a web application built using Django, a Python web framework. It provides functionality for users to create, manage, and register for events. The system ensures user authentication, allowing only registered users to participate in events. Additionally, it features a user-friendly interface and a basic search functionality.

## Features

- **User Registration:** New users can create accounts, providing their basic details such as first name, last name, username, email, and password.

- **Event Registration:** Registered users can sign up for events, with a limit on the number of available slots.

- **User Authentication:** Only authenticated users can register for events. Users are only allowed to unregister from events they've previously registered for.

- **Admin Panel:** Django's admin panel is utilized for managing events and user registrations. Admins have control over the system's data.

- **User Dashboard:** Users have access to a personalized dashboard where they can view and manage the events they've registered for.

- **API Endpoints (Django Rest Framework):** API endpoints are created for listing all events, providing details of a specific event, user registration for an event, and fetching a user's registered events.

## Project Structure

The project consists of Django models for Users, Events, and UserEventRegistration. Views handle user sign-up, login, home page, event registration, and other functionalities. Templates and static files are organized to ensure a clean and responsive user interface.

## Setup

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Apply Database Migrations:**
   ```
   python manage.py migrate
   ```

4. **Run the Development Server:**
   ```
   python manage.py runserver
   ```

## API Endpoints

### List of All Events

- **Endpoint:** `/api/events/`
- **Method:** GET
- **Description:** Retrieve a list of all events.

### Details of a Specific Event

- **Endpoint:** `/api/events/<event_id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific event identified by `event_id`.

### User's Registered Events

- **Endpoint:** `/api/user/registered-events/<user_id>/`
- **Method:** GET
- **Description:** Retrieve a list of events registered by a user identified by `user_id` along with registration dates.

## API Documentation

The API documentation can be accessed using one of the following methods:

- [http://localhost:8000/docs](http://localhost:8000/docs)

Visit [http://localhost:8000](http://localhost:8000) in your browser to access the application.
