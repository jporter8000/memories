from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict={}
    return render(request,'memories_app/index.html',context=my_dict)