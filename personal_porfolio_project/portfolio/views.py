from django.shortcuts import render
from .models import project
# Create your views here.

def home(request):
    model_elements = project.objects.all()
    return render(request,'portfolio/home.html',{'model_elements':model_elements})
