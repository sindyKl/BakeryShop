# Generated by Django 4.1.3 on 2022-12-17 14:44

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
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=25, null=True, unique=True, verbose_name='Slug')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='products', verbose_name='Image')),
            ],
        ),
    ]