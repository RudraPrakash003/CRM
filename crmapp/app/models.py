from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=20)
    address = models.TextField()
    username = models.CharField(max_length=40, unique=False, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CATEGORY = (
        ('Electronics', 'Elecronics'),
        ('Fashion', 'Fashion')
    )
    product_name = models.CharField(max_length=255)
    product_category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    product_value = models.FloatField(null=True)

class Purchased(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_ordered = models.DateField()
    status = models.CharField(max_length=100,null=True, choices=STATUS)

class MyTasks(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=255)
    due_date = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS)

class UpcomingActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
