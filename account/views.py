import imp
import re

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator

from account.utils import detect

from .forms import *
from .models import contact, video


def MainHome(request):
    return render(request, 'HomeApp/home.html')



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'account/register.html', {'form': form})

def contact_us(request):
    if request.method == "POST":
        contact1 = contact()
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('number')
        subject1 = request.POST.get('subject')
        contact1.name = name1
        contact1.email = email1
        contact.number = phone1
        contact1.subject = subject1
        contact1.save()
        uuser = contact1.name
        messages.success(request, f'Hi {uuser}, your message is saved. our team will talk to you very soon...')

        return redirect('Mainhome')
        

    return render(request,'account/contact.html')

@login_required()
def profile(request):
    return render(request, 'account/profile.html')

@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
        else:
            print('something went wrong')          
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'account/edit.html', context)


@login_required()
def  videos(request):
    if request.method == "GET":
        da = video.objects.all
        return render(request,'account/video.html',{'da':da})


@login_required()
def  playvideo(request,movie_id):
    if request.method == "GET":
        videoplay = video.objects.get(uuid = movie_id)
        
        return render(request,'account/playvideo.html',{'videoplay':videoplay})


        
@login_required()
def some_function(request):
    if request.method == 'GET':
        detect()
        return HttpResponse("Sucess")
    



method_decorator(login_required,name = 'dispatch')
class moviedetails(View):
    def get(self,request,movie_id, *args, **kwargs):
        movie = video.objects.get(uuid = movie_id)

        return  render(request,'account/moviedetails.html',{'movie':movie})






