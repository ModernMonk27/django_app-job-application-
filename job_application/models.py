from django.db import models

# Create your models here.
class Form(models.Model):

    name = models.CharField(max_length=80)
    email = models.EmailField()
    experience =
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


