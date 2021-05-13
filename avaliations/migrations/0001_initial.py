# Generated by Django 3.1.7 on 2021-05-12 21:04

import avaliations.validate
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_instagram', models.CharField(max_length=25, validators=[avaliations.validate.clear_user_instagram], verbose_name='Instagram Avaliado(Ex:@lojinha)')),
                ('category', models.CharField(choices=[('autos_e_pecas', 'Autos e Peças'), ('para_sua_casa', 'Para a Sua Casa'), ('eletronicos_e_celulares', 'Eletrônicos e celulares'), ('musica_e_hobbies', 'Musicas e Hobbies'), ('artigos_infatis', 'Artigos Infantis'), ('moda_e_beleza', 'Moda e Beleza'), ('animais_de_estimacao', 'Animais de Estimação'), ('servicos', 'Serviços'), ('agro_e_industrias', 'Agro e Industrias'), ('esportes_e_lazer', 'Esportes e Lazer'), ('comercio_e_escritorio', 'Comercio e Escritorio')], max_length=25)),
                ('description', models.TextField(verbose_name='Conte sobre o produto')),
                ('titleAvaliation', models.CharField(max_length=100, verbose_name='Titulo do Produto')),
                ('ratingAvaliation', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='avaliations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
