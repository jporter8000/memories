from django.shortcuts import render
from memories_app.forms import PeopleForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    # form=PeopleForm()
    if request.method == "POST":
        form=PeopleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form=PeopleForm()
            return HttpResponseRedirect('/')  #this takes user back to home page so we don't have duplicate entry when they refresh or backspace
        else:
            print('error input wrong')
            form=PeopleForm()
    else:
            form=PeopleForm()

    my_dict={'form':form}
    return render(request,'memories_app/index.html',context=my_dict)