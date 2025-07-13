from django.db import models

# Create your models here.
class studentModel(models.Model):
    reg_no = models.IntegerField()
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.name