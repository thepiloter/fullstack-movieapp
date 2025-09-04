from django.core.management.base import BaseCommand
from movies.models import Category, Movie


class Command(BaseCommand):
    help = "Populate database with sample data"

    def handle(self, *args, **options):
        # Create categories
        categories = ["Adventure", "Romance", "Drama", "Science Fiction"]
        for cat_name in categories:
            category, created = Category.objects.get_or_create(name=cat_name)
            if created:
                self.stdout.write(f"Created category: {cat_name}")

        # Create movies
        movies_data = [
            {
                "film_adi": "The Adventure Begins",
                "aciklama": "An epic adventure movie that takes you on a journey through unknown lands.",
                "resim": "1.jpeg",
                "anasayfa": True,
            },
            {
                "film_adi": "Love in Paris",
                "aciklama": "A romantic story set in the beautiful city of Paris.",
                "resim": "2.jpeg",
                "anasayfa": True,
            },
            {
                "film_adi": "The Drama Within",
                "aciklama": "A compelling drama that explores the depths of human emotion.",
                "resim": "3.jpeg",
                "anasayfa": False,
            },
            {
                "film_adi": "Future World",
                "aciklama": "A science fiction masterpiece set in a dystopian future.",
                "resim": "4.jpeg",
                "anasayfa": False,
            },
        ]

        for movie_data in movies_data:
            movie, created = Movie.objects.get_or_create(
                film_adi=movie_data["film_adi"], defaults=movie_data
            )
            if created:
                self.stdout.write(f'Created movie: {movie_data["film_adi"]}')

        self.stdout.write(
            self.style.SUCCESS("Successfully populated database with sample data")
        )
