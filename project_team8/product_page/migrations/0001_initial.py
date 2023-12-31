# Generated by Django 4.2.5 on 2023-11-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('in_stock', models.BooleanField()),
                ('radiation', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
