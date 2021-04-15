
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_instagram', models.CharField(max_length=25)),
                ('categoria', models.CharField(choices=[('autos_e_pecas', 'Autos e Peças'), ('para_sua_casa', 'Para a Sua Casa'), ('eletronicos_e_celulares', 'Eletrônicos e celulares'), ('musica_e_hobbies', 'Musicas e Hobbies'), ('artigos_infatis', 'Artigos Infantis'), ('moda_e_beleza', 'Moda e Beleza'), ('animais_de_estimacao', 'Animais de Estimação'), ('servicos', 'Serviços'), ('agro_e_industrias', 'Agro e Industrias'), ('esportes_e_lazer', 'Esportes e Lazer'), ('comercio_e_escritorio', 'Comercio e Escritorio')], max_length=25)),
                ('description', models.TextField()),
                ('nomeProduto', models.CharField(max_length=25)),
                ('entregaRapida', models.IntegerField(choices=[(1, 'estrela1'), (2, 'estrela2'), (3, 'estrela3'), (4, 'estrela4'), (5, 'estrela5')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
