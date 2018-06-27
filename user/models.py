from django.db import models
from enumerations.enum import UserType, BloodGroup, Gender, Category
from django.urls import reverse


# Create your models here.
# User Table

class User(models.Model):
    user_name = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Gender], default=Gender.M)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    contact = models.CharField(max_length=12)
    email = models.EmailField()
    photo = models.ImageField()
    category = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Category],
                                default=Category.GEN)
    blood_group = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in BloodGroup],
                                   default=BloodGroup.ABP)
    type = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in UserType], default=UserType.U)

    def __str__(self):
        return self.name + ' - ' + self.type

    def get_absolute_url(self):
        return reverse('user:user_list')

