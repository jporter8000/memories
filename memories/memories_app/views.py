from django.shortcuts import render
from memories_app.forms import PeopleForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

# utm_source=Facebook&utm_medium=FB_Feed&utm_campaign={{campaign.name}}&utm_content={{ad.name}}
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

    adsource = request.GET.get('utm_source')
    admedium = request.GET.get('utm_medium')
    adcampaign = request.GET.get('utm_campaign')
    adcontent = request.GET.get('utm_content')
    
    print('adsource = ' + str(adsource))
    print('admedium = ' + str(admedium))
    print('adcampaign = ' + str(adcampaign))
    print('adcontent = ' + str(adcontent))
    my_dict={'form':form, 'adsource':adsource, 'admedium':admedium, 'adcampaign':adcampaign, 'adcontent':adcontent}
    return render(request,'memories_app/index.html',context=my_dict)