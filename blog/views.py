from django.shortcuts import render
from django.http import HttpResponse


posts = [{
    "author": 'jane Doe',
    "title": 'blog post 2',
    "content": "second post",
    "date": "november 2, 2018"
},
{
    "author": 'asdf Doe',
    "title": 'asdf post 2',
    "content": "asdf post",
    "date": "asdf 2, 2018"
}]


# these functions handle the logic for each page
def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "yoooooo!"})





def store(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/store.html', context)







# def about(request):
#     return HttpResponse('<h1>About</h1>')
