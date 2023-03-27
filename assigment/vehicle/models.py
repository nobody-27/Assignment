from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    USER_TYPE_CHOICES = (
    (1, 'Super admin'),
    (2, 'Admin'),
    (3,'User')
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True,blank=True)

    @property
    def get_role_details(self):
        if self.user_type == 1:
            return "Super Admin"
        elif self.user_type == 2:
            return "Admin"
        else:
            return "User"

    def __str__(self) -> str:
        return f'Name:-{self.username}----ROLE:- {self.get_role_details}'


# alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Vehicle_Types(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Vehicle_Type"
        verbose_name_plural = "Vehicle_Types"


class Vehicle(models.Model):
    number = models.CharField(max_length=200,verbose_name="Number")
    type = models.ForeignKey(Vehicle_Types,on_delete=models.CASCADE,related_name="types")
    model = models.TextField()
    decription = models.TextField()


    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self) -> str:
        return f'{self.number}'
    
   
