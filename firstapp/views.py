from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic, Webpage, AccessRecord
from .import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    
    return render(request, 'firstapp/index.html', context=date_dict)

def index2(request):
    return render(request, 'firstapp/index2.html')


def form_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            #Do something 
            print('validation success!')
            print('Name: ',form.cleaned_data['name'])
            print('Email: ',form.cleaned_data['email'])
            print('Text: ',form.cleaned_data['text'])

    return render(request, 'form.html', {'form':form})


