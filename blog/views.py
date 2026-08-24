from django.shortcuts import render

def index(request):
    # Cette fonction renvoie le template 'index.html'
    return render(request, 'index.html')