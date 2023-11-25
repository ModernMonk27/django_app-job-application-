from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=80,null=True)
    email = models.EmailField(null=True)
    experience = models.CharField(max_length=80, null=True)
    self_intro = models.CharField(max_length=80, null=True)
    preference = models.CharField(max_length=80,null=True)

    def __str__(self):
        return f"{self.name}{self.experience}"
