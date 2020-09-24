from django.shortcuts import render
from memories_app.forms import PeopleForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from random import randint

value = randint(0, 10)
print(value)

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

    # Variables pulled from URL parameters
    # sample Facebook parameters:  utm_source=Facebook&utm_medium=FB_Feed&utm_campaign={{campaign.name}}&utm_content={{ad.name}}
    adsource = request.GET.get('utm_source')
    admedium = request.GET.get('utm_medium')
    adcampaign = request.GET.get('utm_campaign')
    adcontent = request.GET.get('utm_content')
    sitetype = request.GET.get('sitetype')

    # Change contnet on the home page as a function of sitetype url parameter
    maintitle = "Create Highlights of Your Loved Ones"
    subtitle = "Don't Miss Anymore Memories"
    mainbackgroundimage = "images/slider-1-1920x900.jpg"


    # Pass variables to the index page
    my_dict={'form':form, 'adsource':adsource, 'admedium':admedium, 'adcampaign':adcampaign, 
        'adcontent':adcontent, 'sitetype':sitetype, 'subtitle':subtitle, 'maintitle':maintitle, 'mainbackgroundimage':mainbackgroundimage}
    return render(request,'memories_app/index.html',context=my_dict)


def doggos(request):
    value = randint(0, 1)
    if value==0:
        maintitle2 = "Make Doggos Highlights"
        subtitle2 = "Create Videos of Your Loved Ones"
        mainbackgroundimage2 = "images/dog-with-stick.jpg"
        adset = "value0"
    elif value==1:
        maintitle2 = "Make Doggos Highlights"
        subtitle2 = "Share Videos of Your Loved Ones"
        mainbackgroundimage2 = "images/dog-with-stick.jpg"
        adset = "value1"

    
    my_dict2={'maintitle2':maintitle2, 'subtitle2':subtitle2, 'mainbackgroundimage2':mainbackgroundimage2, 'adset':adset}
    return render(request,'memories_app/doggos.html',context=my_dict2)




def doggostest(request):
    value = randint(0, 1)
    if value==0:
        maintitle2 = "Make Doggos Highlights"
        subtitle2 = "Create Videos of Your Loved Ones"
        mainbackgroundimage2 = "images/dog-with-stick.jpg"
        adset = "value0test"
    elif value==1:
        maintitle2 = "Make Doggos Highlights"
        subtitle2 = "Share Videos of Your Loved Ones"
        mainbackgroundimage2 = "images/dog-with-stick.jpg"
        adset = "value1test"

    
    my_dict3={'maintitle2':maintitle2, 'subtitle2':subtitle2, 'mainbackgroundimage2':mainbackgroundimage2, 'adset':adset}
    return render(request,'memories_app/doggostest.html',context=my_dict3)