# Generated by Django 3.1.7 on 2021-04-20 23:21

import avaliations.validate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliation',
            name='user_instagram',
            field=models.CharField(max_length=25, validators=[avaliations.validate.clear_user_instagram], verbose_name='Instagram Avaliado(Ex:@lojinha)'),
        ),
    ]