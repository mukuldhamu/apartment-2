from django.db import models
from django import forms

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


# price_choice = (('1', '$5000'), ('2', '$15,000'), ('3', '$25,000'), ('4', '$40,000'), ('5', '$50,000'))
# apartment_choice = (('1', '1BHK'), ('2', '2BHK'), ('3', '3BHK'))
# possession_choice = (('1', 'ready to move'), ('2', 'work on progress'))


class Property_details1(models.Model):
    img = models.ImageField(upload_to="app1/Media/", blank=True)
    uname = models.CharField(max_length=40)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=12)
    price_range = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    possession = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    flat_type = models.CharField(max_length=20)


class BuyUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    owner_first_name = models.CharField(max_length=20, default="")
    owner_last_name = models.CharField(max_length=20, default="")
    owner_email = models.EmailField(default='NULL')
    owner_contact_no = models.CharField(default='enter_phNo', max_length=12)

    appt_desc = models.CharField(max_length=5000)
    cust_first_name = models.CharField(max_length=100, default='Enter_name')
    cust_last_name = models.CharField(max_length=50, default='Enter_name')
    cust_email = models.EmailField(default='NULL')
    cust_contact_no = models.CharField(max_length=12, default='enter_phNo')

    def __str__(self):
        return self.appt_desc[0:7] + "..."

class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default='NULL')
    subject = models.CharField(max_length=50)
    message = models.TextField()