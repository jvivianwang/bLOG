from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'My first post',
        'content': 'Blog one content',
        'date_created': 'August 5, 2019'
    },
    {
        'author': 'Kelly White',
        'title': 'Second post',
        'content': 'Blog two content',
        'date_created': 'March 17, 2020'
    }
]



# Create your views here.

def home(request):
    # render(request, subdirInTemplpate/filename)
    context = {'posts': posts}
    return render(request,'blog/home.html', context)



def about(request):
    return render(request,'blog/about.html')

