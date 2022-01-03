from django.shortcuts import render , redirect

def index(request):
    if request.method == 'GET':
        contexto = {'titulo' : 'Login/Registro' }
        return render(request , 'index.html' , contexto)

