from django.shortcuts import render
from basicapp.forms import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context_dict = {'text':'Hello World', 'number':100}
    return render(request, 'basicapp/index.html', context_dict)

def other(request):
    return render(request, 'basicapp/other.html')

def relative(request):
    return render(request, 'basicapp/relative_url.html')

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

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
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basicapp/registration.html', 
                    {'user_form':user_form, 
                    'profile_form':profile_form, 
                    'registered':registered})

def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Someone tried to Login and Failed!")
            print("Username {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'basicapp/login.html', {})
