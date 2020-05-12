from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse, HttpResponseRedirect
from webapp.models import Topic, Webpage, AccessRecord, User
from . import forms
from webapp.forms import UserForm, UserProfileInfoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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


class AccRecListView(ListView):
    context_object_name = 'access_records'
    model = AccessRecord
    template_name = 'webapp/access_records.html'



# def accrec(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records': webpages_list,
#                  'insert_me': 'Hello my name is Ayush Sahu'}
#     return render(request, 'webapp/access_records.html', context=date_dict)

class UsersCreateView(CreateView):
    fields = ('first_name', 'last_name', 'email')
    model = User
    template_name = 'webapp/users.html'

class UsersListView(ListView):
    model = User
    template_name = 'webapp/user_list.html'

class UsersDetailView(DetailView):
    model = User
    template_name = 'webapp/user_detail.html'

class UsersUpdateView(UpdateView):
    fields = ('first_name', 'last_name', 'email')
    model = User
    template_name = 'webapp/users.html'

class UsersDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("webapp:userlist")


# class UsersDetailView(DetailView):
#     # context_object_name = 'user_detail'
#     model = User
#     # template_name = 'basic_app/users.html'


# def users(request):
#     form = forms.NewUser()
#
#     if request.method == 'POST':
#         form = forms.NewUser(request.POST)
#         if form.is_valid():
#             form.save(commit = True)
#             return index(request)
#         else:
#             print ("Error form invalid")
#     return render(request, 'webapp/users.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not Active")

        else:
            print ("Someone tried to login & failed")
            print ("Username: {} and Password: {}".format(username, password))

            return HttpResponse("invalid login")

    else:
        return render(request, 'webapp/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")
