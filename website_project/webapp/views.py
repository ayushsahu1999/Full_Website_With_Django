from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Topic, Webpage, AccessRecord, User
from . import forms

# Create your views here.
def index(request):
    return render(request, 'webapp/index.html')

def form_name_view(request):
    form = forms.FormName
    if (request.method == 'POST'):
        form = forms.FormName(request.POST)
        if form.is_valid():
            # do something with it
            print ('Validation Success!')
            print ('Name: ' + form.cleaned_data['name'])
            print ('Email: ' + form.cleaned_data['email'])
            print ('Text: ' + form.cleaned_data['text'])

    return render(request, 'webapp/form_page.html', {'form': form})


def accrec(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list,
                 'insert_me': 'Hello my name is Ayush Sahu'}
    return render(request, 'webapp/access_records.html', context=date_dict)

def users(request):
    first_names = User.objects.order_by('first_name')
    name_dict = {'names': first_names}
    return render(request, 'webapp/users.html', context=name_dict)
