from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)    
    diagnosis = models.CharField(max_length=255)
    treatment_plan = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'{self.patient.name} - {self.diagnosis}'
