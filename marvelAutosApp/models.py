from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(verbose_name="Person's first name", max_length=30)
    last_name = models.CharField(verbose_name="Person's last name", max_length=30)
    dob = models.DateField(verbose_name="Person's Date Of Birth")
    contact_number = models.CharField(verbose_name="Person's Contact Number", max_length=15)
    mail_address = models.EmailField(verbose_name="Peron's Mail Address", max_length=50)
    address = models.CharField(verbose_name="Person's Address", max_length=500)
    