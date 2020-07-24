from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
# classes converted to html, provided by Django

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    context = {
        'user_form':user_form ,
        'profile_form':profile_form
    }
    return render(request, 'users/profile.html', context)

