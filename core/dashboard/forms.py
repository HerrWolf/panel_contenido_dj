from django.forms import ModelForm, TextInput, ModelChoiceField, Select
from core.dashboard.models import Category, ContentType


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