from django.shortcuts import render
from app.models import *
# Create your views here.

def page(request):
	return render(request,'page.html', {'name': 'daniel'})

def login(request):
	return render(request,'page.html', {'name': 'connor'})

