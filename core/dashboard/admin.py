from django.contrib import admin
from core.dashboard.models import ContentType, Category, Movie

# Register your models here.
admin.site.register(ContentType)
admin.site.register(Category)
admin.site.register(Movie)
