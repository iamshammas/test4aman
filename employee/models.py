from django.db import models


class employeeModel(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name
    