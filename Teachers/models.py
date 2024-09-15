from django.db import models

class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

class Pupil(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models
    subject = models.CharField(max_length=100, blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    