from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', context={'user': request.user})