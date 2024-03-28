from django.db import models

#user
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    user_role = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

#Profile
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    theme = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Notification
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date = models.DateTimeField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

#Customer
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    industry = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name

#Admin
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_name = models.CharField(max_length=20)

    def __str__(self):
        return self.admin_name

#Deal
class Deal(models.Model):
    deal_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    deal_name = models.CharField(max_length=255)
    deal_desc = models.TextField()
    deal_value = models.DecimalField(max_digits=10, decimal_places=2)
    deal_status = models.CharField(max_length=10)
    start_date = models.DateTimeField()
    expected_close_date = models.DateTimeField()
    actual_close_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.deal_name

#MyTask
class MyTasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=20)
    due_date = models.DateField()

    def __str__(self):
        return self.task_title

#Upcoming Activity
class UpcomingActivity(models.Model):
    event_id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

