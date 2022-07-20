from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse,reverse_lazy
from .forms import CreateUserForm
from .models import Blog,Title,Category,Comment
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
    total_likes = fullblog.total_likes()

    liked = False
    if fullblog.likes.filter(id=request.user.id).exists():
        liked=True
    if request.method =='POST':
        comment = request.POST['comment']
        Comment.objects.create(post=fullblog,name = request.user,body=comment)
        print(comment)
        return HttpResponseRedirect(request.path_info)
    return render(request,'single-standard.html',{'fullblog':fullblog,'total_likes':total_likes,'liked':liked})

# Like blog

def like_blog(request,id):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        like=Blog.objects.get(id = post_id)

        liked = False
        if like.likes.filter(id=request.user.id).exists():
            like.likes.remove(request.user)
            liked=False
        else:
            like.likes.add(request.user)
            liked =True
        return redirect('selected_blog',id)
        # return HttpResponseRedirect(reverse('selected_blog',args=[str(id)]))

# Search Button

def search(request):
    if request.method =='POST':
        searchTxt = request.POST['search']
        search = Blog.objects.filter(Q(title__title__icontains=searchTxt)|Q(author__username__icontains=searchTxt)|Q(category__category__icontains=searchTxt)|Q(keyword__icontains=searchTxt))
        print(search)
    return render(request,'index.html',{'bloglist':search})
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
    return redirect('login')