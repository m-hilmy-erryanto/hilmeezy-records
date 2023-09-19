from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    genre = models.CharField(max_length=255)
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
