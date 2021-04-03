from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics', null=False)
    bio = models.CharField(max_length=500, null=False, default="")
    score = models.IntegerField(default=0, null=False)
    work_experience = models.CharField(max_length=10, null=False, default="")
    slug = models.SlugField(max_length=500, null=False, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        slug1 = slugify(self.user.first_name)
        slug2 = slugify(self.user.last_name)
        self.slug = slugify(slug1 + slug2)
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 720 or img.width > 1280:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)
