from django.shortcuts import render
from . models import Data
# Create your views here.
def index(request):
    if 'q' in request.GET:
        q =request.GET['q']
        data = Data.objects.filter(first_name__icontains=q)
    else:
       data = Data.objects.all()
    context ={
        'data': data
    }
    return render(request,'index.html',context)