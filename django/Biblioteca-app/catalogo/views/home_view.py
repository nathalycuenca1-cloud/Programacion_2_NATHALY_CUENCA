from django.shortcuts import render, redirect
from catalogo.views.home_view import login_required

@login_required
def home(request):
    return render(request, 'catalogo/inicio.html')