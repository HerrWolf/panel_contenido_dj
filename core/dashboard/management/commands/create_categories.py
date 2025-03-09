from django.core.management.base import BaseCommand
from django.db import transaction

from core.app1_fuss.models import CatCategorias as App1FussCatCategorias, \
    CatTipoContenido as App1FussCatTipoContenido
from core.dashboard.models import ContentType, Category


class Command(BaseCommand):
    help = 'Este comando genera las categorias basadas en la base de datos app1_fuss_db'

    def handle(self, *args, **kwargs):
        self.stdout.write('Ejecutando mi comando personalizado...')
        app1_fuss_categories = App1FussCatCategorias.objects.all()
        for category in app1_fuss_categories:
            app1_fuss_content_type_name = App1FussCatTipoContenido.objects.get(cve=category.cve_cat_tipo_contenido)
            content_type_base = ContentType.objects.get(name=app1_fuss_content_type_name.tipo_contenido)
            with transaction.atomic():
                Category.objects.create(
                    name=category.categoria,
                    content_type=content_type_base
                )
            # self.stdout.write(f'ID: {category.cve} | Name: {category.categoria} | tipo_contenido: '
            #                   f'{category.cve_cat_tipo_contenido} | {app1_fuss_content_type_name.tipo_contenido}'
            #                   f' | {content_type_base.id}')
        self.stdout.write('Comando ejecutado con éxito')