# Personal Portfolio

A Django-based personal portfolio website with a blog section, built to showcase projects and share articles.

## Features

- **Portfolio** – Display projects with title, description, image, and external URL.
- **Blog** – Publish posts with title, body text, and publication date.
- **Admin Panel** – Manage projects and blog entries via Django's built-in admin interface.
- **Media Uploads** – Images are uploaded and served through Django's media handling.

## Tech Stack

- Python 3.8.4
- Django 3.0.8
- SQLite (development)
- Gunicorn (WSGI server)
- WhiteNoise (static files serving)
- Pillow (image processing)

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd personal_portfolio
   ```

2. Create and activate a virtual environment:

   ```bash
   python3.8 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` to view the site.

## Configuration

- **local_settings.py** – Place a `local_settings.py` file in `personal_portfolio/` to override settings for local development (e.g., `DEBUG=True`). The project loads it automatically if present.
- **SECRET_KEY** – Keep the production secret key secure. Use environment variables or local settings for sensitive values.
- **ALLOWED_HOSTS** – Update this in `settings.py` for your deployment domain.

## Deployment

The project is configured for Heroku deployment:

- **Procfile** – Runs `gunicorn personal_portfolio.wsgi` as the web process.
- **runtime.txt** – Specifies `python-3.8.4`.
- **WhiteNoise** – Handles static file serving in production.

To deploy to Heroku:

```bash
heroku create <app-name>
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## Project Structure

```
personal_portfolio/
├── blog/               # Blog app (models, views, templates, URLs)
├── portfolio/          # Portfolio app (models, views, templates, URLs, static files)
├── personal_portfolio/ # Project settings, URLs, WSGI/ASGI config
├── media/              # User-uploaded media files
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── Procfile            # Heroku process definition
├── runtime.txt         # Python runtime version
└── LICENSE
```

## License

See the [LICENSE](LICENSE) file for details.
