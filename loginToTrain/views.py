from django.shortcuts import render
# Create your views here.
from static.page12306 import main


def index(request):
    return render(request,'index.html')

def login(request):
    main()
    return render(request,'index.html')