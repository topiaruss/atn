from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    creation_date = models.DateTimeField('date created')

    def __str__(self):
        return ', '.join([self.name, self.address])


class Customer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    creation_date = models.DateTimeField('date created')


    def __str__(self):
        return ', '.join([self.name, self.address]) + ' client of ' + self.client.name

