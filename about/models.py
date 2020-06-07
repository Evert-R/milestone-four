from django.db import models

# Create your models here.


class clients(models.Model):
    """
    Add a client to the list on the about page
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
