from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Avaliation(models.Model):
    TIPO_ENTREGA = (
        (1, 'estrela1'),
        (2, 'estrela2'),
        (3, 'estrela3'),
        (4, 'estrela4'),
        (5, 'estrela5'),
    )
    TIPO_CATEGORIA = (
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
    )

    user_instagram = models.CharField(
        max_length=25, verbose_name='Instagram Avaliado(Ex:@lojinha)')
    categoria = models.CharField(max_length=25, choices=TIPO_CATEGORIA,)
    description = models.TextField(verbose_name='Conte sobre o produto')
    nomeProduto = models.CharField(
        max_length=25, verbose_name='Nome do Produto')
    entregaRapida = models.IntegerField(
        choices=TIPO_ENTREGA, verbose_name='Velocidade da Entrega'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_instagram
