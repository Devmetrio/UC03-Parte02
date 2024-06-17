from django.shortcuts import render,redirect

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html') 