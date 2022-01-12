from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

 
class InstitutionProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics', null=False)
    institution_name = models.CharField(max_length=200, null=False, default="")
    bio = models.TextField(max_length=1000, null=False, default="")
    slug = models.SlugField(max_length=500, null=False, blank=True)
    address = models.TextField(max_length=800, null=False)
    phone_number = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.institution_name)
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 720 or img.width > 1280:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)
