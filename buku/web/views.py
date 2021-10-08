from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404 ,redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from . import models
from . import forms
from django.contrib.auth import login ,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from  . import tokens


"""
Area Daftar
"""
def signup(request):
    form = forms.CreateForms()
    if request.method == "POST":
        form = forms.CreateForms(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            subject = 'Aktivasi Dari Django'
            message = render_to_string('token.html',{
                'user':user,
                'domain':get_current_site(request).domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':tokens.account_activation_token.make_token(user)
            })
            user.email_user(subject,message)
            return redirect('login')
    context ={
        'forms' : form,
    }
    if request.method == "GET":

        if request.user.is_authenticated:
            return redirect('index')

    return render(request, 'signup.html', context)


"""
Kirim link activation
"""
def activate(request,uidb64,token):
    uid = force_text(urlsafe_base64_decode(uidb64).decode())
    user= User.objects.get(pk=uid)
    if user is not None and tokens.account_activation_token.check_token(user,token):
        user.is_active = True
        user.email_active = True
        user.save()
        login(request,user)
        return redirect('index')
    else:
        messages.error(request, 'Kesalahan Aktivation')
        return redirect('login')


"""
Area Login
"""
def buatlogin(request):
    if request.method == "POST":
        userlogin = request.POST['username']
        passwordlogin = request.POST['password']
        user = authenticate(request, username=userlogin, password=passwordlogin)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Password Yang Kamu Masukan Salah')
            return redirect('login')

    if request.method == "GET":
        if request.user.is_authenticated:
            # logika Ketika sudah login
            return redirect('index')
        else:
            # logika belum login
            return render(request, 'login.html', )


"""
Area Logout
"""
@login_required(login_url=settings.LOGIN_URL)
def logoutview(request):
    logout(request)
    return redirect('index')


"""
Area CRUD
"""
#Create
@login_required(login_url=settings.LOGIN_URL)
def create(request):
    form = forms.postForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect('index')
    context = {
        'forms': form
    }

    return render(request, 'create.html', context)

#Read/detail
def detail(request, slug):
    all = get_object_or_404(models.Post, slug=slug)

    context = {
        'detail_id': all
    }
    return render(request, 'views.html', context)

#Update
@login_required(login_url=settings.LOGIN_URL)
def update(request, update):
    update = get_object_or_404(models.Post, id=update)

    # validasi kepemilikian
    if request.user.id != update.user.id:
        return render(request, 'error.html')

    form = forms.postForm(request.POST or None, request.FILES or None, instance=update)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'forms': form
    }
    return render(request, 'ubahbuku.html', context)

#Delete
@login_required(login_url=settings.LOGIN_URL)
def delete(request, delete):
        models.Post.objects.filter(id=delete).delete()
        return redirect('index')


"""
Area Home/Index
"""
@login_required(login_url=settings.LOGIN_URL,)
def index(request):
    cat = models.Category.objects.all()
    all = models.Post.objects.all()

    context ={
        'category': cat,
        'semua': all
    }

    return render(request, 'home.html', context)


"""
Area Category
"""
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














