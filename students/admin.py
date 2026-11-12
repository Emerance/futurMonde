from django.contrib import admin

from .models import Student # Importation du modèle Student depuis le fichier models.py pour l'enregistrer dans l'interface d'administration de Django.

# Register your models here.
@admin.register(Student) # Enregistrement du modèle Student dans l'interface d'administration de Django.
class StudentAdmin(admin.ModelAdmin): # Définition de la classe StudentAdmin qui hérite de la classe ModelAdmin de Django.
    list_display = (
        'student_code', 
        'last_name_student', 
        'first_name_student', 
        'phone_number_student', 
        'birth_date_student', 
        'email_student', 
        'address_student'
        ) # Définition des champs à afficher dans la liste des étudiants dans l'interface d'administration.
    search_fields = ('student_code', 'user__first_name', 'user__last_name') # Définition des champs à utiliser pour la recherche dans l'interface d'administration.
    list_filter = ('student_code', 'user__first_name', 'user__last_name') # Définition des champs à utiliser pour le filtrage dans l'interface d'administration.

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
    
    def last_name_student(self, obj): # Définition de la méthode pour obtenir le nom de famille de l'étudiant.
        return obj.user.get_last_name() # Retourne le nom de famille de l'étudiant à partir de l'objet User associé.  
    last_name_student.short_description = 'Nom de famille' # Définition du nom affiché pour la colonne dans l'interface d'administration.

    def first_name_student(self, obj):
        return obj.user.get_first_name()    
    first_name_student.short_description = 'Prénom' 

    def phone_number_student(self, obj): 
        return obj.user.phone_number
    phone_number_student.short_description = 'Numéro de téléphone'
    
    def birth_date_student(self, obj):
        return obj.user.birth_date
    birth_date_student.short_description = 'Date de naissance'
    
    def email_student(self, obj):
        return obj.user.email
    email_student.short_description = 'Adresse e-mail'

    def address_student(self, obj):
        return obj.user.address
    address_student.short_description = 'Adresse'