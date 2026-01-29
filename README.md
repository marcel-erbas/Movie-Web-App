# Movie Library

A Flask web application for managing users and their favorite movies, featuring a modern dark theme and OMDb API integration.

## Features

*   **User Management**: Create and delete user profiles.
*   **Movie Collection**: Add movies via OMDb API search, update titles, and delete entries.
*   **Modern UI**: Responsive dark theme.
*   **Data Persistence**: SQLite database with SQLAlchemy ORM.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install flask flask-sqlalchemy requests python-dotenv
    ```

2.  **Environment Variables:**
    Create a `.env` file in the root directory and add your OMDb API key:
    ```
    OMDB_API_KEY=your_api_key_here
    ```

3.  **Run the Application:**
    ```bash
    python app.py
    ```
    The app will be available at `http://127.0.0.1:5000`.