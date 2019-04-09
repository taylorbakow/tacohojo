from django.db import models
from django.conf import settings
from decimal import Decimal
# Create your models here.

class Opioids(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    DrugName = models.TextField()
    IsOpioid = models.BooleanField()
    AvgPerscribed = models.DecimalField(max_digits=6, decimal_places=2)

class Drugs_Details(models.Model):
    DrugID = models.ForeignKey('Opioids', on_delete=models.CASCADE)
    PrescriberID = models.ForeignKey('Prescriber', on_delete=models.CASCADE)
    QtyPrescribed = models.IntegerField(default=0)

class Prescriber(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    Fname = models.TextField()
    Lname = models.TextField()
    Gender = models.TextField(db_index=True, max_length=1, choices=GENDER_CHOICES)
    Credentials = models.TextField()
    Specialty = models.TextField()
    OpioidPrescriber = models.BooleanField()
    StateAbbrev_id = models.ForeignKey('States', on_delete=models.CASCADE, db_column='StateAbbrev_id')
    TotalPrescription = models.IntegerField()
    
class States(models.Model):
    StateAbbrev_id = models.CharField(primary_key=True, max_length = 2, db_column='StateAbbrev_id')
    StateName = models.TextField()
    Population = models.IntegerField()
    Deaths = models.IntegerField()