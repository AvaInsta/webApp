# Generated by Django 3.1.7 on 2021-05-12 21:04

from django.db import migrations, models
import report.validate


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_instagram_report', models.CharField(max_length=100, validators=[report.validate.clear_user_instagram], verbose_name='Loja denunciada')),
                ('titleReport', models.CharField(max_length=100, verbose_name='Titulo da denúncia:')),
                ('descriptionReport', models.TextField(verbose_name='Nos conte o que aconteceu:')),
            ],
        ),
    ]
