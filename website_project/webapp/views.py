from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list,
                 'insert_me': 'Hello my name is Ayush Sahu'}
    return render(request, 'webapp/index.html', context=date_dict)
