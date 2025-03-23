from core.dashboard.models import Category

CATEGORY_MAPPING = {
    "Recien Agregadas":85,
    "Estrenos":86,
    "Estrenos Cam (mala calidad)":87,
    "Accion":88,
    "Ciencia Ficcion":89,
    "Comedia":90,
    "Crimen":91,
    "Drama":92,
    "Romance":93,
    "Suspenso":94,
    "Terror":95,
    "Documentales":96
}

def get_subs_movie_category_id(name):
    category = Category.objects.get(content_type=11, id=CATEGORY_MAPPING.get(name))
    return category.id