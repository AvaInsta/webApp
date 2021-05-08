# Generated by Django 3.1.7 on 2021-05-07 19:10

from django.db import migrations, models
import report.validate


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report_store_instagram_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='store_instagram_report',
            field=models.CharField(max_length=100, validators=[report.validate.clear_user_instagram], verbose_name='Loja denunciada'),
        ),
    ]