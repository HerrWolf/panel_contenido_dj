from django.core.management.base import BaseCommand
from django.db import transaction

from core.app1_fuss.models import CatTipoContenido as App1FussCatTipoContenido
from core.dashboard.models import ContentType


class Command(BaseCommand):
    help = 'Este comando genera los tipos de contenido en base a la base de datos app1_fuss_db'

    def handle(self, *args, **kwargs):
        self.stdout.write('Ejecutando mi comando personalizado...')
        types = App1FussCatTipoContenido.objects.all()
        for type in types:
            with transaction.atomic():
                ContentType.objects.create(name=type.tipo_contenido)
            self.stdout.write(f'Creando tipo de contenido: {type.tipo_contenido}')
        self.stdout.write('Comando ejecutado con éxito')