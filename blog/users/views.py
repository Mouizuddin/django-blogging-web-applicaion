from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_reg(request):
    if request.method=='POST':
        user_form = RegForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request,f'Thank you {username} your data is done!')
            return redirect('blog_home')
    else:
        user_form = RegForm()
    
    return render(request , 'users/register.html' , {'user_form': user_form , 'title':'Register'})


@login_required
def profile(request):
    return render(request , 'users/profile.html' , {'title':'Profile'})