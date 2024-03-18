from django.shortcuts import render
from django.http import HttpResponse

def vistorias(resquest):
    return render(resquest, 'vistorias.html')