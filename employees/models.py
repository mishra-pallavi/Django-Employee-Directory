from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phono_number = models.CharField(max_length=12, blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, default='M')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

