from django.db import models
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self):
        return ', '.join([self.name, self.address])


class Customer(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)


    def __str__(self):
        return ', '.join([self.name, self.address]) + ' client of ' + self.client.name

