from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Book(models.Model):
    title       = models.CharField(max_length=50, default="Not available")
    author      = models.CharField(max_length=20, default="Not available")
    subject     = models.CharField(max_length=20, default="Not available")
    genre       = models.CharField(max_length=20, default="Not available")
    description = models.CharField(max_length=150, default="Not available")
    image       = models.ImageField(default="book.jpg")

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return 'LibrarySite/media/book.jpg'

class myUser(models.Model):
    user        = models.OneToOneField(User)
    birthday    = models.DateField(null=True)
    firstName       = models.CharField(max_length=20)
    lastName       = models.CharField(max_length=25)

    def __unicode__(self):
        return self.firstName

#create user obj to attach to myUser object

#def create_myUser_callback(sender, instance, **kwargs):
#    user, new = myUser.objects.get_or_create(user=instance)
#post_save.connect(create_myUser_callback, User)






#put reviews
#put other books by author
