from django.shortcuts import render

# Connexion avec la base de données et récupération des étudiants
#from .db_students import students

from .models import Student

def students_list(request):
    list_students = Student.objects.select_related('user').all()
    return render(request, 'students/list_students.html', context={'list_students': list_students})
