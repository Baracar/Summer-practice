from django.db import models


class Metrics(models.Model):
    host = models.CharField(max_length=40)
    minTime = models.FloatField(null=True)
    maxTime = models.FloatField(null=True)
    meanTime = models.FloatField(null=True)
    counter = models.IntegerField(null=True)


class Request(models.Model):
    host = models.CharField(max_length=40)
    time = models.FloatField()
    method = models.CharField(max_length=10)
    version = models.CharField(max_length=15)
    timeStamp = models.DateTimeField(auto_now_add=True)


class RequestCount(models.Model):
    host = models.CharField(max_length=40)
    method = models.CharField(max_length=10)
    version = models.CharField(max_length=15)
    counter = models.IntegerField(default=0)