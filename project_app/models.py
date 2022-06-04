from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
