# Generated by Django 2.2.3 on 2024-07-09 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto',
            field=models.ImageField(upload_to='artistas'),
        ),
    ]
