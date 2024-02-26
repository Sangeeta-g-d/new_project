from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

# Create your models here.
class NewUser(AbstractUser):
    user_type = models.CharField(max_length=100, default='operator')
    phone_no = models.CharField(max_length=100)
    adhar_no = models.CharField(max_length=30)
    pan_no = models.CharField(max_length=40, null=True)

class UploadFile(models.Model):
    excel = models.FileField(upload_to='uploads/')

class APMCTender(models.Model):
    commodity = models.CharField(max_length=300)
    commission_agent = models.CharField(max_length=300)
    lot_id = models.CharField(max_length=100)
    Bags = models.IntegerField()
    lot_code = models.CharField(max_length=300)
    quality = models.CharField(max_length=200)
    rs = models.FloatField()
    operator_id = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=4)
    created_on = models.DateField(default=timezone.now)

class APMCETender(models.Model):
    tender_id = models.ForeignKey('APMCTender', on_delete=models.CASCADE, default=1)
    commodity = models.CharField(max_length=300)
    commission_agent = models.CharField(max_length=300)
    lot_id = models.CharField(max_length=100)
    Bags = models.IntegerField()
    lot_code = models.CharField(max_length=300)
    quality = models.CharField(max_length=200)
    rs = models.FloatField()
    operator_id = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=4)
    created_on = models.DateField(default=timezone.now)

class Grades(models.Model):
    quality = models.CharField(max_length=300)
    minimum = models.IntegerField()
    maximum = models.IntegerField()

class PasswordReset(models.Model):
    user_id = models.ForeignKey(NewUser , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
