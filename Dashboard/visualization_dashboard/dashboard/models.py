from django.db import models

class DataRecord(models.Model):
    intensity = models.IntegerField()
    likelihood = models.IntegerField()
    relevance = models.IntegerField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    pest = models.CharField(max_length=100)
    swot = models.CharField(max_length=100)
