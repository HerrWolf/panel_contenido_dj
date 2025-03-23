from django.core.management.base import BaseCommand

from core.contenido_fuss.models import Peliculas
from core.dashboard.models import Movie, Category
import json
import time

from icecream import ic

from core.media_downloader import MediaDownloader


class Command(BaseCommand):
    help = 'Import movies from contenido_fuss_db to default database'

    def add_arguments(self, parser):
        parser.add_argument('--limit', type=int, help='Number of movies to import')

    def handle(self, *args, **options):
        # Ask for number of movies if not provided
        limit = options.get('limit')
        if not limit:
            limit = int(input('How many movies do you want to import? '))

        # Get movies from external database
        movies_to_import = Peliculas.objects.all()

        self.stdout.write(self.style.SUCCESS(f'Found {len(movies_to_import)} movies to process'))

        # Initialize the media downloader
        downloader = MediaDownloader()

        # Process each movie
        imported_count = 0
        skipped_count = 0

        for movie in movies_to_import:
            tmdb_id = movie.contentid
            genre1 = movie.genre1

            # Determine audio based on genre
            audio = None
            if "[LAT]" in genre1:
                audio = "lat"
            elif "[SUB]" in genre1:
                audio = "sub"
            else:
                self.stdout.write(self.style.WARNING(f"Skipping movie {tmdb_id}: Unknown audio format"))
                skipped_count += 1
                continue

            # Check if movie already exists with same tmdb_id and audio
            if Movie.objects.filter(tmdb_id=tmdb_id, audio=audio).exists():
                self.stdout.write(self.style.WARNING(f"Skipping movie {tmdb_id}: Already exists with audio {audio}"))
                skipped_count += 1
                continue

            # Get movie details from TMDB
            self.stdout.write(f"Downloading information for movie ID {tmdb_id}")
            movie_data = downloader.get_details_by_id('movie', int(tmdb_id))

            if not movie_data:
                self.stdout.write(self.style.ERROR(f"Failed to get details for movie {tmdb_id}"))
                skipped_count += 1
                continue

            movie_path = movie.url.replace("http://panduki.xyz/", "")

            category_sub_dict = {
                'Recien Agregadas':85,
                'Estrenos':86,
                'Estrenos Cam (mala calidad)':87,
                'Accion':88,
                'Ciencia Ficcion':89,
                'Comedia':90,
                'Crimen':91,
                'Drama':92,
                'Romance':93,
                'Suspenso':94,
                'Terror':95,
                'Documental':96
            }

            # Create new movie
            try:
                new_movie = Movie(
                    title=movie_data.get('title', ''),
                    original_title=movie_data.get('original_title', ''),
                    tmdb_id=tmdb_id,
                    poster_url=f"https://image.tmdb.org/t/p/w500{movie_data.get('poster_path', '')}" if movie_data.get(
                        'poster_path') else None,
                    backdrop_url=f"https://image.tmdb.org/t/p/original{movie_data.get('backdrop_path', '')}" if movie_data.get(
                        'backdrop_path') else None,
                    state='catalogo',
                    audio=audio,
                    overview=movie_data.get('overview', ''),
                    release_date=movie_data.get('release_date', '')[:4] if movie_data.get('release_date') else '',
                    video_path=movie_path,
                )
                new_movie.save()

                # Add categories here if needed
                genres = movie.genre2
                genres_list = genres.split(',')
                for genre in genres_list:
                    if movie.genre1 == '[LAT]':
                        category = Category.objects.filter(name=genre).first()
                    else:
                        category = Category.objects.filter(id=category_sub_dict[genre]).first()
                    if category:
                        new_movie.categories.add(category)

                    # self.stdout.write(self.style.SUCCESS(f"category: {category}"))

                imported_count += 1
                self.stdout.write(self.style.SUCCESS(f"Imported movie: {new_movie.title}"))

                if imported_count >= limit:
                    break

                # Add a small delay to avoid API rate limits
                time.sleep(0.5)


            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing movie {tmdb_id}: {str(e)}"))
                skipped_count += 1

        # self.stdout.write(self.style.SUCCESS(f"Import completed: {imported_count} imported, {skipped_count} skipped"))
        self.stdout.write(self.style.SUCCESS(f"Import limit: {limit}"))