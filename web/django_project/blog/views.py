from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Iluha Gasanov',
        'title': 'Зига ой зага ой',
        'content': 'govno',
        'date_posted': 'August 23, 2013'

    },
    {
        'author': 'Ilias Gasanov',
        'title': 'ПРОСРАЛ ЖЫЗНЬ',
        'content': 'govnishe',
        'date_posted': 'August 2, 1488'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


