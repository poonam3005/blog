from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from blogapp.models import Blog
from .forms import CreateUserForm
from .models import Blog,Title,Category
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
# Create your views here.

def index(request):
    bloglist=Blog.objects.all()
    print(request.user,"loged in")
    return render(request,'index.html',{'bloglist':bloglist})

# Selected Bolg

def selected_blog(request,id):
    fullblog = Blog.objects.get(id=id)
    return render(request,'single-standard.html',{'fullblog':fullblog})

# Upload Blog

def upload_blog(request):
    if request.method =='POST':
        title = request.POST['title']
        category = request.POST['category']
        entryTxt = request.POST['entryTxt']
        Desc = request.POST['Desc']
        keyword = request.POST['keyword']
        image = request.FILES['Uploadimage']
        
        try:
            title = Title.objects.get(title = title)
            category = Category.objects.get(category=category)
            Blog.objects.create(author=request.user,title=title,category=category,entryTxt=entryTxt,Desc=Desc,keyword=keyword,image=image)
        except:

            print("Title or Categoty")
        return redirect('index')

    return render(request,'upload-blog.html')


def update(request, id):
    b = Blog.objects.get(id=id)

    if request.method=="POST":
        b.delete()
        
        
        title=request.POST.get('title')
        category=request.POST.get('category')
        desc=request.POST.get('desc')
        entryTxt = request.POST.get['entryTxt']
        keyword=request.POST.get('keyword')
        image = request.FILES.get('image')

        b1=Blog(title=title,category=category,desc=desc,keyword=keyword,entryTxt=entryTxt,image=image)
        b1.save()
        return redirect('/')
    else:
        return render(request, "update.html",{'b1': b1})


def delete(request, id):
    e = Blog.objects.get(id=id)
    e.delete()
    return HttpResponseRedirect('/')

# ---------- Registration -------------

def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Creates Successfully' + user)

    context = {'form' : form}
    return render(request,'registration.html', context)

# ---------- login -------------

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')
    return render(request,'login.html')


# ---------- logout -------------

def logoutuser(request):
    logout(request)
    return render(request, 'login.html')



def searchbar(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Blog.objects.filter(Q(title__icontains=search_post) & Q(category__icontains=search_post))
    else:
        # If not searched, return default posts
        posts = Blog.objects.all().order_by("-date")
    return render(request, 'index.html', {'posts':posts})