from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    email = models.EmailField()
    date = models.CharField(max_length=55)
    application_aim = models.TextField()


    def __str__(self):
        return str(self.name)
