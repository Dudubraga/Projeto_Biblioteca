# Generated by Django 5.1.2 on 2024-11-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id_livro', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('ano_publicacao', models.IntegerField()),
            ],
        ),
    ]
