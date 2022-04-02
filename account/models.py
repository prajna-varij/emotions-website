from email.mime import image
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
import uuid

DEFAULT_IMAGE = 'default_image.jpg'

class Profile(models.Model):
    """Extension of default User model.
       Adds a profile image and description."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=DEFAULT_IMAGE, upload_to='profile_pics')
    description = models.TextField(default='Add description here.')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """Decrease the image size for user profile."""
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class video(models.Model):
    name = models.TextField()
    file = models.FileField(upload_to= "media/videos")
    description = models.TextField(blank = True,null= True)
    uuid = models.UUIDField(default=uuid.uuid4)
    image = models.ImageField(upload_to = "media/images")


    def __str__(self):
        return self.name




class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = PhoneField(blank=True, help_text='Contact phone number')
    subject = models.TextField()

    def __str__(self):
        return self.name




