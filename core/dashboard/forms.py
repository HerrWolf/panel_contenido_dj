from django.forms import (ModelForm, TextInput, ModelChoiceField, Select, SelectMultiple,
                          Textarea)
from core.dashboard.models import Category, ContentType, Movie


class CategoryForm(ModelForm):
    content_type = ModelChoiceField(
        queryset=ContentType.objects.all(),
        widget=Select(
            attrs={
                'class': 'form-control select2',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['name'].label = "Nombre de categoría"
        self.fields['content_type'].label = "Tipo de contenido"

    class Meta:
        model = Category
        fields = 'name', 'content_type'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre',
                }
            )
            # Ya no necesitamos definir content_type aquí porque está arriba
        }
        exclude = ['created_at', 'updated_at']


class MovieForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tmdb_id'].widget.attrs['autofocus'] = True
        self.fields['tmdb_id'].label = "TMDB ID"
        self.fields['title'].label = "Titulo de la pelicula"
        self.fields['original_title'].label = "Titulo Original de la pelicula"
        self.fields['poster_url'].label = "URL del poster"
        self.fields['backdrop_url'].label = "URL del backdrop"
        self.fields['state'].label = "Estado"
        self.fields['overview'].label = "Sinopsis"
        self.fields['release_date'].label = "Año"
        self.fields['categories'].label = "Selecciona las categorías"
        self.fields['video_path'].label = "Path del video"

        # Filter categories where content_type.id is 1 or 11
        self.fields['categories'].queryset = Category.objects.filter(
            content_type__id__in=[1]
        ).exclude(pk=1)

        # Configurar el widget - Nota: no usar .widget = SelectMultiple()
        self.fields['categories'].widget.attrs.update({
            'class': 'form-control select2',
            'multiple': 'multiple',
            'id': 'id_categories'
        })

    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
        widgets = {
            'title': TextInput(
                attrs={
                    'placeholder': 'Título',
                }
            ),
            'original_title': TextInput(
                attrs={
                    'placeholder': 'Título original',
                }
            ),
            'tmdb_id': TextInput(
                attrs={
                    'placeholder': 'TMDB ID',
                }
            ),
            'poster_url': TextInput(
                attrs={
                    'placeholder': 'URL del poster',
                }
            ),
            'backdrop_url': TextInput(
                attrs={
                    'placeholder': 'URL del backdrop',
                }
            ),
            'overview': Textarea(
                attrs={
                    'placeholder': 'Resumen',
                }
            ),
            'release_date': TextInput(
                attrs={
                    'placeholder': 'Fecha de estreno',
                }
            ),
            'video_path': TextInput(
                attrs={
                    'placeholder': 'URL del video',
                }
            ),
            # 'categories': SelectMultiple(
            #     attrs={
            #         'class': 'form-control select2',
            #         'multiple': 'multiple',
            #         'id': 'id_categories',
            #     }
            # )
        }
