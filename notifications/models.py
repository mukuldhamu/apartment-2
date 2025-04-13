from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length= 256)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

@receiver(post_save, sender = User)
def create_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        Notification.objects.create(user = kwargs.get('instance'), title = 'Welcome to Apartment Rentz !', message = 'Thanks for signing up !')

class Notification1(models.Model):
    owner = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=90)

    def __str__(self):
        return self.owner
