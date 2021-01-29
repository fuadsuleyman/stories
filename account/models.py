from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    
    CATEGORY_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    
    # first_name = models.CharField('Name', max_length=30, blank=True, null=True)
    # last_name = models.CharField('Surname', max_length=40, blank=True, null=True)
    gender = models.PositiveIntegerField(("Gender"), choices=CATEGORY_CHOICES, blank=True, null=True)
    address = models.CharField("Address", max_length=1024, blank=True, null=True)
    biography = models.TextField("Biograpyhy", blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'