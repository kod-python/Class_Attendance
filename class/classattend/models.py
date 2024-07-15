from django.db import models

# Create your models here.
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100, default="firstName")
    lastName = models.CharField(max_length=100, default="lastName")
    email= models.EmailField(max_length=254, default="email")
    course = models.CharField(max_length=200, default="course")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName