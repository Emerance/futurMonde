from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # Définition du modèle User qui hérite de la classe AbstractUser de Django.
    ROLE_CHOICES = [
        ('STAFF', 'Personnel adminstratif'),
        ('STUDENT', 'Etudiant'),
        ('TEACHER', 'Enseignant'),
        ('PARENT', 'Parent d\'élève'),   
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Rôle")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Date de naissance")
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Numéro de téléphone")
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name="Adresse")
    password = models.CharField(max_length=128, blank=True, verbose_name="Mot de passe")
    
    def __str__(self):
        return f"{self.last_name.upper()} {self.first_name} " # Méthode pour représenter l'objet User sous forme de chaîne de caractères.

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" # Méthode pour obtenir le nom complet de l'utilisateur.

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name