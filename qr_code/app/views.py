from django.shortcuts import render
from .models import Website
# Create your views here.

def index(request):
    name="Welcome to"
    obj = Website.objects.get(id=2)
    context={
        'name': name,
        'obj':obj,
    }
    
    return render(request,'index.html',context)