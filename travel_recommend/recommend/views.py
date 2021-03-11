from .models import Tuser
from django.shortcuts import render

# Create your views here.
def showme(*args):
    rate = Tuser.objects.all()
    print(rate)

showme()