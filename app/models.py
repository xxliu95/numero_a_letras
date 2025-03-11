from django.db import models

class Texto(models.Model):
    numero = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero
