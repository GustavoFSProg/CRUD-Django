from django.db import models

class Usuarios(models.Model):
    name = models.TextField() 
    email = models.TextField() 
    senha = models.TextField() 

    def __str__(self) -> str:
            return self.name
