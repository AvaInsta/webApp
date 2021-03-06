from django import forms
from .models import Avaliation
from django.core.validators import validate_slug, validate_email
from django.core.validators import validate_slug, validate_email
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

choice_list = [
    ('autos_e_pecas', 'Autos e Peças'),
    ('para_sua_casa', 'Para a Sua Casa'),
    ('eletronicos_e_celulares', 'Eletrônicos e celulares'),
    ('musica_e_hobbies', 'Músicas e Hobbies'),
    ('artigos_infatis', 'Artigos Infantis'),
    ('moda_e_beleza', 'Moda e Beleza'),
    ('animais_de_estimacao', 'Animais de Estimação'),
    ('servicos', 'Serviços'),
    ('agro_e_industrias', 'Agro e Indústrias'),
    ('esportes_e_lazer', 'Esportes e Lazer'),
    ('comercio_e_escritorio', 'Comércio e Escritório'),
]

# CKEDITOR_CONFIGS = {
#    'default': {
#        'toolbar': 'full',
#        'height': 300,
#        'width': 300,
#    },
# }

choice_list = [
    ('autos_e_pecas', 'Autos e Peças'),
    ('para_sua_casa', 'Para a Sua Casa'),
    ('eletronicos_e_celulares', 'Eletrônicos e celulares'),
    ('musica_e_hobbies', 'Musicas e Hobbies'),
    ('artigos_infatis', 'Artigos Infantis'),
    ('moda_e_beleza', 'Moda e Beleza'),
    ('animais_de_estimacao', 'Animais de Estimação'),
    ('servicos', 'Serviços'),
    ('agro_e_industrias', 'Agro e Industrias'),
    ('esportes_e_lazer', 'Esportes e Lazer'),
    ('comercio_e_escritorio', 'Comercio e Escritorio'),
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
}


class CreateForm(forms.ModelForm):
    class Meta:
        model = Avaliation
        fields = ['store_instagram', 'category', 'description',
                  'titleAvaliation', 'ratingAvaliation']
        widgets = {
            'store_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'titleAvaliation': forms.TextInput(attrs={'class': 'form-control'}),
        }
