from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Dar',
        'title': 'Post 1',
        'content': 'Lots of usless text',
        'date_posted': 'August, 6, 2020'
    },
    {
        'author': 'Binod',
        'title': 'Post 2',
        'content': 'More useless text but by Binod',
        'date_posted': 'August, 7, 2020'
    }
]

def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
