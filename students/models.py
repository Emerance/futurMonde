from django.db import models
from django.conf import settings

from core.models import User # Importation de la classe User depuis le fichier core/models.py pour l'utiliser comme classe de base pour le modèle Student.
# Create your models here.

class Student(models.Model): # Définition du modèle Student qui hérite de la classe Person.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True) # Champ pour la relation OneToOne avec le modèle User, avec suppression en cascade et clé primaire.
    student_code = models.CharField(max_length=20, unique=True, verbose_name="Matricule") # Champ pour l'identifiant unique de l'étudiant.

    class Meta:
        abstract = False # Indique que cette classe doit être créée dans la base de données.

    def __str__(self):
        return f"{self.student_code} - {self.user.get_full_name()}" # Méthode pour représenter l'objet Student sous forme de chaîne de caractères, incluant l'ID étudiant et le nom complet.

class Parent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True) # Champ pour la relation OneToOne avec le modèle User, avec suppression en cascade et clé primaire.

    def __str__(self):
        return f"{self.user.get_full_name()}" # Méthode pour représenter l'objet Parent sous forme de chaîne de caractères, incluant le nom complet.

class ParentShip(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE) # Champ pour la relation ForeignKey avec le modèle Parent, avec suppression en cascade.
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # Champ pour la relation ForeignKey avec le modèle Student, avec suppression en cascade.

    class Meta:
        unique_together = ('parent', 'student') # Définition d'une contrainte d'unicité sur la combinaison parent-étudiant.

    def __str__(self):
        return f"{self.parent.user.get_full_name()} - {self.student.user.get_full_name()}" # Méthode pour représenter l'objet ParentShip sous forme de chaîne de caractères, incluant les noms complets du parent et de l'étudiant.
    
