from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"You've been succssfully logged in as { username }")
            login(request, new_user)
            return redirect('/') 
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html',{'form':form})

def profileUpdate(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"profile updated successfully")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'account/update.html', context)
   
 

@login_required
def profile(request):
	return render(request, 'account/profile.html')