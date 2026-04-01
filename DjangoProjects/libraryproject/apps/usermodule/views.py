from django.http import HttpResponse
from django.shortcuts import render 
# Create your views here.

def index(request):
    return render(request, "usermodule/index.html",
                   { 'name' : request.GET.get('name', 'Anon') }) # index
    name = request.GET.get('name', 'Anon')
    return HttpResponse(f"Hello, {name}! Welcome to the users module!")
