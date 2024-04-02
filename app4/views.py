from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string_res(request):
    return HttpResponse('this is string response')

def index(request):
    return render(request,'index.html')
 