import os
from .crop import crop
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from allauth.socialaccount.models import SocialAccount

import io
from PIL import Image
from django.core.files import File
from urllib.request import urlopen
from django.core.files.temp import NamedTemporaryFile


def user_directory_path(instance, filename):
    profile_pic_name = f'users_images/{instance.username}/profile.jpg'
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name


class User(AbstractUser):
    image = models.ImageField(upload_to=user_directory_path, blank=True)   
    phone = PhoneNumberField(blank=True)
    bio = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            crop(self.image.path)

        elif SocialAccount.objects.filter(user=self.pk):
            url = SocialAccount.objects.filter(user=self.pk)[0].extra_data['picture']
            self.save_from_url(url)


    def save_from_url(self, url):
        """Save image to ImageField from URL"""
        
        img_tmp = NamedTemporaryFile()

        with urlopen(url) as uo:
            assert uo.status == 200

            img = Image.open(io.BytesIO(uo.read()))
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            img.save(img_tmp, 'JPEG')
            img_tmp.flush()
        img = File(img_tmp)
        self.image.save(img_tmp.name, img)

            

User._meta.get_field('email')._unique=True
