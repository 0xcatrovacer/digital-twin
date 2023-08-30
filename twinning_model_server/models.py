from django.db import models

# Create your models here.


class Data(models.Model):
    name = models.CharField(max_length=100, )
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    pass


class Field(models.Model):
    name = models.CharField(max_length=100)
    data = models.ManyToManyField(Data)

    def __str__(self):
        return self.name

    pass


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    fields = models.ManyToManyField(Field)

    def __str__(self):
        return self.name
