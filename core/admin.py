from django.contrib import admin
from .models import User # Importation du modèle User depuis le fichier models.py pour l'enregistrer dans l'interface d'administration de Django.

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin): # Définition de la classe UserAdmin pour personnaliser l'affichage du modèle User dans l'interface d'administration.
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff') # Définition des champs à afficher dans la liste des utilisateurs.
    search_fields = ('username', 'email', 'first_name', 'last_name') # Définition des champs sur lesquels la recherche peut être effectuée dans l'interface d'administration.
    list_filter = ('role', 'is_staff') # Définition des champs sur lesquels les filtres peuvent être appliqués dans l'interface d'administration.

def has_add_permission(self, request): # Définition de la méthode pour vérifier si l'utilisateur a la permission d'ajouter un nouvel utilisateur.
    return False # Retourne False pour empêcher l'ajout d'un nouvel utilisateur via l'interface d'administration.