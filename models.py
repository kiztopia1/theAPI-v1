from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# refrence models
    
class SubCity(models.Model):
    name            = models.CharField(max_length=100)
    def __str__(self):
        return self.name 
     
class Disease(models.Model):
    name            = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Medications(models.Model):
    drag_name           = models.CharField(max_length=100)
    description         = models.TextField()
    def __str__(self):
        return self.name
    
    
# creat your models here




    
# patient information form
class Patient(models.Model):
    SEX = (
        ('male', 'male'),
        ('female', 'female')
        )
    
    STATUS = (
        ('marid', 'marid'),
        ('singel', 'singel')
    )
    
    name            = models.CharField(max_length=100)
    age             = models.IntegerField()
    # dateOfBirth     = models.DateField()
    maritalStatus   = models.CharField(max_length = 100, null = False, choices = STATUS)
    sex             = models.CharField(max_length = 100, null = False, choices = SEX)
    adress          = models.CharField(max_length = 100, null = False)
    phone1          = models.CharField(max_length = 100, null = False)
    phone2          = models.CharField(max_length = 100, null = False)
    language        = models.CharField(max_length = 100, null = False, default = 'Amahric')
    # city            = models.ForeignKey(SubCity, default="N/A" , on_delete=models.CASCADE)

    
    
    def __str__(self):
        return self.name
    
# --------------------------- medical history model -------------------------- #

class History(models.Model):
    patient             = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date                = models.DateTimeField(auto_now_add=True)
    disease             = models.CharField(max_length = 100)
    medications         = models.CharField(max_length=100)
    description         = models.TextField()
     
    def __str__(self):
        return self.description

# ----------------------------- lab results model ---------------------------- #

class labResult(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=100)
    history          = models.ForeignKey(History, on_delete= models.CASCADE) 
    def __str__(self):
        return self.name
    
# ------------------------------ active patients ----------------------------- #

class Active_patient(models.Model):
    patient = models.ForeignKey(Patient, on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.patient.name