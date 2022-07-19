from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index' ),
    path('registration', views.registration, name='registration' ),
    path('login', views.loginuser, name='login' ),
    path('logout', views.logoutuser, name='logout' ),
<<<<<<< HEAD
    path('search', views.searchbar, name='search' ),
    path('selected_blog', views.selected_blog,name='selected_blog'),
=======
    path('selected_blog/<id>', views.selected_blog,name='selected_blog'),
    path('upload-blog',views.upload_blog,name='upload-blog')
>>>>>>> 497069e09a7e8ee8d81a90369793e7dc5e15f6e8
]