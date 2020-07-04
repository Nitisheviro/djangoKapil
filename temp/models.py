from django.db import models

# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return self.name + ' ' + str(self.total)

    @property
    def total(self):
        return self.age * 100