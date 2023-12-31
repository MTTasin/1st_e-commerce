# Generated by Django 5.0 on 2023-12-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='carousels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='static/img/corusels/')),
            ],
        ),
        migrations.CreateModel(
            name='fixed_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='static/img/fixed/')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='product_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='static/img/')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
