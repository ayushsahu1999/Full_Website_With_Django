from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Topic, Webpage, AccessRecord, User
from . import forms
from webapp.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    dict = {'text': 'I am testing hello function'}
    return render(request, 'webapp/index.html', context=dict)

def form_name_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'webapp/form_page.html', {'user_form': user_form,
                                                     'profile_form': profile_form,
                                                     'registered': registered})


def accrec(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list,
                 'insert_me': 'Hello my name is Ayush Sahu'}
    return render(request, 'webapp/access_records.html', context=date_dict)

def users(request):
    form = forms.NewUser()

    if request.method == 'POST':
        form = forms.NewUser(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print ("Error form invalid")
    return render(request, 'webapp/users.html', {'form': form})
