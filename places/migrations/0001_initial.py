# Generated by Django 5.0.1 on 2024-01-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('visited', models.BooleanField()),
            ],
            options={
                'db_table': 'places',
            },
        ),
    ]
