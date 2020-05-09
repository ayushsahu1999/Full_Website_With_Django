from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me': 'Hello my name is Ayush Sahu'}
    return render(request, 'webapp/index.html', context=my_dict)
