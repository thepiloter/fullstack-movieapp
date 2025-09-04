# Movie App - Django Web Application

A fully containerized Django web application for browsing movies. This application runs completely isolated in Docker containers with no external API dependencies.

## Features

- Browse movies by categories
- View movie details
- Responsive design with Bootstrap
- SQLite database (included)
- Admin panel for managing content
- Self-contained with sample data

## Technology Stack

- **Backend**: Django 4.0.3
- **Database**: SQLite3
- **Frontend**: HTML, Bootstrap 5.1.3
- **Containerization**: Docker & Docker Compose

## Quick Start with Docker

### Prerequisites

- Docker
- Docker Compose

### Option 1: Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd fullstack-movieapp

# Build and run the application
docker-compose up --build

# Access the application
# Web App: http://localhost:8000
# Admin Panel: http://localhost:8000/admin (admin/admin123)
```

### Option 2: Using Docker directly

```bash
# Build the Docker image
docker build -t movieapp .

# Run the container
docker run -p 8000:8000 movieapp

# Access the application at http://localhost:8000
```

## Local Development (without Docker)

### Prerequisites

- Python 3.9+
- pip

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Navigate to the Django project directory
cd movieapp

# Run migrations
python manage.py migrate

# Populate database with sample data
python manage.py populate_db

# Create a superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Access the application at http://127.0.0.1:8000
```

## Application Structure

```
fullstack-movieapp/
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose configuration
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── movieapp/                  # Django project
    ├── manage.py              # Django management script
    ├── db.sqlite3             # SQLite database
    ├── movieapp/              # Main Django app
    │   ├── settings.py        # Django settings
    │   ├── urls.py            # URL configuration
    │   └── ...
    ├── movies/                # Movies application
    │   ├── models.py          # Database models
    │   ├── views.py           # View functions
    │   ├── urls.py            # URL patterns
    │   ├── templates/         # HTML templates
    │   ├── static/            # Static files (images)
    │   └── management/        # Custom Django commands
    └── account/               # User account application
```

## Database Models

### Movie
- `film_adi`: Movie title
- `aciklama`: Movie description
- `resim`: Image filename
- `anasayfa`: Homepage display flag

### Category
- `name`: Category name

## API Endpoints

- `/`: Homepage with featured movies
- `/home`: Same as homepage
- `/movies`: All movies page
- `/movies/<id>`: Movie detail page
- `/admin/`: Django admin panel

## Admin Access

- **Username**: admin
- **Password**: admin123

## Sample Data

The application comes pre-populated with:
- 4 categories: Adventure, Romance, Drama, Science Fiction
- 4 sample movies with descriptions and images

## Development Notes

- The application uses SQLite for simplicity and portability
- Static files are served by Django in development mode
- Bootstrap is loaded from CDN for styling
- No external API keys or services required
- Images are stored locally in the static files directory

## Docker Configuration Details

- **Base Image**: python:3.9-slim
- **Port**: 8000
- **Volume Mount**: ./movieapp:/app (for development)
- **Environment**: DEBUG=1 (development mode)
- **Auto-restart**: unless-stopped

## Troubleshooting

### Docker Issues
- Ensure Docker is running
- Check port 8000 is not in use
- Try `docker-compose down` then `docker-compose up --build`

### Local Development Issues
- Ensure Python 3.9+ is installed
- Run `pip install -r requirements.txt` in project root
- Check Django is properly installed: `python -m django --version`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## License

This project is provided as-is for educational and development purposes.
