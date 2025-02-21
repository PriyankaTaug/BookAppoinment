from django.db import models
from django.utils.timezone import now
# Create your models here.

class Specilaization(models.Model):
    special_name =  models.CharField(max_length=100,unique=True)

class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True)
    specilaization =  models.ForeignKey(Specilaization,on_delete=models.CASCADE)
    experience = models.PositiveIntegerField()
    avaiable_days = models.CharField(max_length=100)
    available_time = models.TimeField()

class Nurse(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True)
    department = models.CharField(max_length=100)
    
class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True)
    role = models.CharField(max_length=15,unique=True)
    department = models.CharField(max_length=100)


class Appoinment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    patient_email = models.CharField(max_length=50)
    patient_phone = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    app_date = models.DateField()
    app_time = models.TimeField()


class Attendance(models.Model):
    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Employee', 'Employee'),
    ]
    
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)  # Doctor, Nurse, Employee
    person_id = models.PositiveIntegerField()  # Stores the ID of Doctor, Nurse, or Employee
    check_in_time = models.DateTimeField(default=now, null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Checked In', 'Checked In'), ('Checked Out', 'Checked Out')], default='Checked In')
    att_date = models.DateField()
    
    def __str__(self):
        return f"{self.role} (ID: {self.person_id}) - {self.status}"