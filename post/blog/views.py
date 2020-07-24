from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    # render(request, subdirInTemplpate/filename)
    context = {'posts': Post.objects.all()}
    return render(request,'blog/home.html', context)



def about(request):
    return render(request,'blog/about.html')

