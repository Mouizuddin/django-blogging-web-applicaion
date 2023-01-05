from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    dummy_data = [{'author': 'dummy name' , 'blog_title':'dummy title' , 'blog_content':'dummy_content' , 'date':'dummy date'}]
    return render(request , 'blog_app/home.html', context={'details': Post.objects.all() , 'title':'Home'})


def about(request):
    return render(request , 'blog_app/about.html', context={'title':'About'})