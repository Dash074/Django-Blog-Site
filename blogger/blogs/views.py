from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import Post  # There is no error here
from blogs.models import Category  # There is no error here


# Create your views here.
def home(request):
    # load all the posts from db
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    # print(posts)

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})


def about(request):
    cat = Category.objects.all()
    posts = Post.objects.all()
    return render(request, "about.html", {'cat': cat, 'posts': posts})


def add_post(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "about.html", {'cat': cat, 'posts': posts})


from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed


def admin_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/admin')  # Redirect to admin index page after logout
    else:
        return HttpResponseNotAllowed(['POST'])  # Return 405 Method Not Allowed for non-POST requests
