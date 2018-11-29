from django.db import models
from model_utils.models import TimeStampedModel

from partners.models import Customer


class Zone(TimeStampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return ', '.join([self.customer.name, self.name])


class Site(models.Model):

    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    # def fqurl(self):
    #     customer = self.zone.customer
    #     client = customer.client
    #     return ' '.join(map(str, [customer.id, client.id, self.zone.id, self.id]))

    def __str__(self):
        return self.name + ' in ' + self.zone.name

