from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField('Category', max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Slug', max_length=25, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    description = models.TextField('Description')
    image = models.ImageField('Image', blank=True, upload_to='products')

    def save(self, *args, **kwargs): 
        if self.slug is None:
            self.slug = slugify(self.name) # editing slugfield
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
