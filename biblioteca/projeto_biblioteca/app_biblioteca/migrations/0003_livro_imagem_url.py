# Generated by Django 5.1.2 on 2024-11-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0002_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='imagem_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
