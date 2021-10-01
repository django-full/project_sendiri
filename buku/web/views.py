
from django.shortcuts import render, get_object_or_404 ,redirect
from . import models
from . import forms
from django.contrib.auth import login ,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm




def index(request):
    cat = models.Category.objects.all()
    all = models.Post.objects.all()
    context ={
        'category': cat,
        'semua': all
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            # logika user
            template = 'home.html'
        else:
            # logika anymous
            template = 'indexanymous.html'
    return render(request, template, context)

    return render(request, 'home.html', context)


def detail(request, slug):
    all = get_object_or_404(models.Post, slug=slug)

    context = {
        'detail_id': all
    }
    return render(request, 'views.html', context)


@login_required(login_url=settings.LOGIN_URL)
def category(request, categories):
    cat = models.Category.objects.all()
    categori = models.Category.objects.all()
    obj = models.Post.objects.filter(categories__nama__contains=categories)
    context = {
        'category': cat,
        'title': categories,
        'semua': categori,
        'objs': obj,

    }
    return render(request, 'category.html', context)


@login_required(login_url=settings.LOGIN_URL)
def create(request):
    form = forms.postForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'forms': form
    }

    return render(request, 'create.html', context)


@login_required(login_url=settings.LOGIN_URL)
def update(request, update):
    update = get_object_or_404(models.Post, id=update)
    form = forms.postForm(request.POST or None, request.FILES or None, instance=update)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'forms': form
    }

    return render(request, 'ubahbuku.html', context)


@login_required(login_url=settings.LOGIN_URL)
def delete(request, delete):
    models.Post.objects.filter(id=delete).delete()
    return redirect('index')


def buatlogin(request):
    context = {

    }
    if request.method == "POST":
        userlogin = request.POST['username']
        passwordlogin = request.POST['password']
        user = authenticate(request, username=userlogin, password=passwordlogin)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    if request.method == "GET":
        if request.user.is_authenticated:
            # logika user
            return redirect('index')
        else:
            # logika Anymous
            return render(request, 'login.html', context)


@login_required(login_url=settings.LOGIN_URL)
def logoutview(request):
    logout(request)
    return redirect('index')


def signup(request):
    form = forms.CreateForms()
    if request.method == "POST":
        form = forms.CreateForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context ={
        'formss' : form
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'signup.html', context)





