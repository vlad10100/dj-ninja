from django.db import models

class Department(models.Model):
    department = models.CharField(max_length=250)

    def __str__(self):
        return self.department


class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birthdate = models.DateField(null=True, blank=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        output = f"{self.first_name} {self.last_name}"
        return output


        