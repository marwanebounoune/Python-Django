from django.db import models
from datetime import datetime

class ListClients(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom