from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    genre = models.CharField(max_length=255)
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    image = models.URLField(blank=True, null=True)
    # picture = models.ImageField(null=True, upload_to = "photo/")
