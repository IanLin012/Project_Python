from django.db import models
from django.core.exceptions import ValidationError

class Person(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()

    def clean(self):
        if self.height < 140 or self.height > 200:
            raise ValidationError('Height must be between 140 and 200 cm')
        if self.weight < 30 or self.weight > 120:
            raise ValidationError('Weight must be between 30 and 120 kg')